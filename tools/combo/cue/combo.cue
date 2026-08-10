// Master Duel combo route model. CUE side of the bake-off.
// Same ruleset as pkl/Combo.pkl, so the comparison is language versus language.
package crystron

import (
	"list"
	"strings"
)

#Zone: "hand" | "deck" | "field" | "gy" | "banished" | "extra" | "opponent-field" | "attached"

#Lock: "none" | "machine" | "machine-synchro"

#Action: "activate" | "normal-summon" | "special-summon" | "synchro" | "xyz" | "link" | "search" | "mill" | "destroy" | "banish"

#Step: close({
	n:      int & >0
	card:   #CardName
	action: #Action
	text:   string & !=""
	from:   #Zone
	// "" means the card does not move. CUE cannot test a field for absence inside a
	// comprehension, so this is a sentinel rather than an optional field.
	to: #Zone | *""
	materials: [...#CardName] | *[]
	result:             string | *""
	appliesLock:        #Lock | *"none"
	oncePerTurn:        string | *""
	oncePerDuel:        string | *""
	grantsNormalSummon: int | *0
	usesAltSummon:      bool | *false
	// 2026-08-10: The Level this card BECOMES when an effect changes it. 0 means unchanged.
	// Revolving Switchyard summons a Level 4 EARTH Machine and makes it Level 10; without this
	// the model rejects a correct Rank 10 line because the material is still Level 4 on paper.
	becomesLevel: int | *0
})

#Route: {
	name:  string & !=""
	build: "amelia" | "yukinon"
	opening: [...#CardName]
	steps: [...#Step]

	_deck: decks[build]
	_deckKeys: [for k, _ in _deck {k}]

	// R2. Card must be in this build's decklist.
	_deckErrors: [
		for s in steps if !list.Contains(_deckKeys, s.card) {
			"step \(s.n): \(s.card) is not in the \(build) decklist"
		},
	]

	// R3. One Normal Summon per turn plus anything granted.
	_nsUsed: len([for s in steps if s.action == "normal-summon" {s}])
	_nsGranted: list.Sum([for s in steps {s.grantsNormalSummon}])
	_nsErrors: [
		if _nsUsed > 1+_nsGranted {
			"route uses \(_nsUsed) Normal Summons but only \(1+_nsGranted) are available"
		},
	]

	// R3b. A Normal Summon must come from the HAND.
	// 2026-08-10: found while writing route_flying_launcher. The zone check only asserts the
	// claimed zone matches the tracked one, so "Normal Summon Scrap Recycler from the deck"
	// passed: Recycler really WAS in the deck. Matching a claim is not the claim being legal.
	_nsZoneErrors: [
		for s in steps if s.action == "normal-summon" && s.from != "hand" {
			"step \(s.n): \(s.card) is Normal Summoned from \(s.from), but a Normal Summon must come from the hand"
		},
	]

	// R4/R5/R6. Material composition.
	//
	// 2026-08-10: iterates `for i, s in steps` rather than over a pre-filtered list, because the
	// effective-Level lookup needs the step's INDEX to know which Level changes happened before it.
	// CUE has no functions, so the lookup is inlined per material.
	_matErrors: list.FlattenN([
		for i, s in steps if list.Contains(["synchro", "xyz", "link"], s.action) && !s.usesAltSummon {
			let r = requirements[s.result]
			let n = len(s.materials)
			let t = len([for m in s.materials if cards[m].tuner {m}])
			// Effective Level per material: the last becomesLevel set before this step, else printed.
			let lv = [
				for m in s.materials {
					let changes = [for j, u in steps if j < i && u.card == m && u.becomesLevel != 0 {u.becomesLevel}]
					[if len(changes) > 0 {changes[len(changes)-1]}, cards[m].level][0]
				},
			]
			let total = list.Sum(lv)
			let want = cards[s.result].level
			list.Concat([
				[if n < r.minMaterials {"step \(s.n): \(s.result) needs at least \(r.minMaterials) materials, got \(n)"}],
				[if n > r.maxMaterials {"step \(s.n): \(s.result) takes at most \(r.maxMaterials) materials, got \(n)"}],
				[if t < r.minTuners {"step \(s.n): \(s.result) needs at least \(r.minTuners) Tuner(s), got \(t)"}],
				[if t > r.maxTuners {"step \(s.n): \(s.result) takes at most \(r.maxTuners) Tuner(s), got \(t)"}],
				[if r.levelsMustTotal && total != want {"step \(s.n): materials total \(total), but \(s.result) is Level \(want)"}],
				// Joined by hand so the string matches Pkl's exactly; see the note in Combo.pkl.
				[if r.sameLevel && len([for l in lv if l != want {l}]) > 0 {"step \(s.n): \(s.result) is Rank \(want) but materials are Levels \(strings.Join([for l in lv {"\(l)"}], ", "))"}],
				[if r.requiresRace != "" && len([for m in s.materials if cards[m].race != r.requiresRace {m}]) > 0 {"step \(s.n): \(s.result) requires \(r.requiresRace) materials"}],
			])
		},
	], 1)

	_summonSteps: [for s in steps if list.Contains(["synchro", "xyz", "link"], s.action) && !s.usesAltSummon {s}]

	// R7. The Extra Deck lock.
	_lockErrors: list.FlattenN([
		for s in _summonSteps {
			let synchroLocks = [for t in steps if t.n < s.n && t.appliesLock == "machine-synchro" {t}]
			let machineLocks = [for t in steps if t.n < s.n && t.appliesLock == "machine" {t}]
			list.Concat([
				[if len(synchroLocks) > 0 && s.action != "synchro" {
					"step \(s.n): \(s.action) summon of \(s.result) is illegal. \(synchroLocks[0].card) applied the Machine Synchro lock at step \(synchroLocks[0].n)"
				}],
				[if len(synchroLocks) > 0 && cards[s.result].race != "Machine" {
					"step \(s.n): \(s.result) is not a Machine, blocked by the lock from step \(synchroLocks[0].n)"
				}],
				[if len(machineLocks) > 0 && cards[s.result].race != "Machine" {
					"step \(s.n): \(s.result) is not a Machine, blocked by the Machine lock from step \(machineLocks[0].n)"
				}],
			])
		},
	], 1)

	// R8. Once per turn and once per Duel.
	// CUE has no `distinct`, so duplicates need the "report only at the first occurrence" trick:
	// count all matches, and emit only when no earlier index also matched. Pkl says `.distinct`.
	_optKeys: [for s in steps if s.oncePerTurn != "" {s.oncePerTurn}]
	_optErrors: [
		for i, k in _optKeys
		if len([for k2 in _optKeys if k2 == k {k2}]) > 1
		if len([for j, k2 in _optKeys if k2 == k && j < i {j}]) == 0 {
			"once per turn effect used \(len([for k2 in _optKeys if k2 == k {k2}])) times: \(k)"
		},
	]

	_opdKeys: [for s in steps if s.oncePerDuel != "" {s.oncePerDuel}]
	_opdErrors: [
		for i, k in _opdKeys
		if len([for k2 in _opdKeys if k2 == k {k2}]) > 1
		if len([for j, k2 in _opdKeys if k2 == k && j < i {j}]) == 0 {
			"ONCE PER DUEL effect used \(len([for k2 in _opdKeys if k2 == k {k2}])) times: \(k)"
		},
	]

	// R9. Zone tracking. Has to live inside #Route because of CUE's lexical scoping.
	_initZones: {
		for k, _ in _deck if !list.Contains(opening, k) {
			(k): [if list.Contains(["synchro", "xyz", "link"], cards[k].kind) {"extra"}, "deck"][0]
		}
		for c in opening {(c): "hand"}
	}

	// 2026-08-10: State accumulates by INDEX, not by recursion.
	//
	// The first attempt used a recursive definition (`#ZoneFold & {inSteps: list.Drop(...)}`) and
	// silently applied only the FIRST step. The cause was a self-reference: inside that struct
	// literal, `inSteps` resolves to the field being defined THERE, not the outer one, so the tail
	// was never passed. Binding the tail to a `let` first fixes the self-reference and then hits
	// CUE's `structural cycle` detector, which rejects recursive definitions of this shape outright.
	//
	// Indexed accumulation has neither problem: finite keys, each derived from the previous, so
	// there is no recursion for the cycle detector to reject. Verified against the Pkl fold.
	//
	// The route is first flattened into ATOMIC MOVES, because a single step can move several cards
	// (the acting card plus every material). Accumulating over moves rather than steps keeps this
	// to one accumulation instead of one nested inside another.
	_matZoneOf: [for s in steps {[if s.action == "xyz" {"attached"}, "gy"][0]}]

	_stepMoves: [
		for i, s in steps {
			list.Concat([
				[if s.to != "" {{card: s.card, zone: s.to}}],
				[for m in s.materials {{card: m, zone: _matZoneOf[i]}}],
			])
		},
	]

	_allMoves: list.FlattenN(_stepMoves, 1)

	// How many moves happen before step i, so a step can look up the state as it was on entry.
	_moveOffset: [for i, _ in steps {list.Sum([for j, ms in _stepMoves if j < i {len(ms)}])}]

	_moveStates: {
		"0": _initZones
		for i, mv in _allMoves {
			"\(i+1)": {
				let prev = _moveStates["\(i)"]
				for k, v in prev if k != mv.card {(k): v}
				(mv.card): mv.zone
			}
		}
	}

	_zonesBefore: [for i, _ in steps {_moveStates["\(_moveOffset[i])"]}]

	// FINDING 2: a missing key is a HARD ERROR in CUE, and it kills the whole evaluation rather
	// than producing a finding. Pkl says `getOrNull(x) ?? "nowhere tracked"`. CUE needs the keys
	// materialised and a Contains guard, plus the `[if cond {a}, b][0]` trick to get a fallback.
	_zoneErrors: [
		for i, s in steps
		let keys = [for k, _ in _zonesBefore[i] {k}]
		let z = [if list.Contains(keys, s.card) {_zonesBefore[i][s.card]}, "nowhere tracked"][0]
		if z != s.from {
			"step \(s.n): \(s.card) is claimed to act from \(s.from), but it is in \(z)"
		},
	]

	// R9b. Materials must be on the field when consumed.
	_matZoneErrors: list.FlattenN([
		for i, s in steps {
			let keys = [for k, _ in _zonesBefore[i] {k}]
			[
				for m in s.materials
				let mz = [if list.Contains(keys, m) {_zonesBefore[i][m]}, "nowhere tracked"][0]
				if mz != "field" {
					"step \(s.n): material \(m) is not on the field, it is in \(mz)"
				},
			]
		},
	], 1)

	errors: list.Concat([_deckErrors, _nsErrors, _nsZoneErrors, _matErrors, _lockErrors, _optErrors, _opdErrors, _zoneErrors, _matZoneErrors])
}
