// Master Duel combo route model. CUE side of the bake-off.
// Same ruleset as pkl/Combo.pkl, so the comparison is language versus language.
package crystron

import "list"

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

	// R4/R5/R6. Material composition.
	_summonSteps: [for s in steps if list.Contains(["synchro", "xyz", "link"], s.action) && !s.usesAltSummon {s}]
	_matErrors: list.FlattenN([
		for s in _summonSteps {
			let r = requirements[s.result]
			let n = len(s.materials)
			let t = len([for m in s.materials if cards[m].tuner {m}])
			let total = list.Sum([for m in s.materials {cards[m].level}])
			let want = cards[s.result].level
			list.Concat([
				[if n < r.minMaterials {"step \(s.n): \(s.result) needs at least \(r.minMaterials) materials, got \(n)"}],
				[if n > r.maxMaterials {"step \(s.n): \(s.result) takes at most \(r.maxMaterials) materials, got \(n)"}],
				[if t < r.minTuners {"step \(s.n): \(s.result) needs at least \(r.minTuners) Tuner(s), got \(t)"}],
				[if t > r.maxTuners {"step \(s.n): \(s.result) takes at most \(r.maxTuners) Tuner(s), got \(t)"}],
				[if r.levelsMustTotal && total != want {"step \(s.n): materials total \(total), but \(s.result) is Level \(want)"}],
				[if r.sameLevel && len([for m in s.materials if cards[m].level != want {m}]) > 0 {"step \(s.n): \(s.result) is Rank \(want) but materials are not all that Level"}],
				[if r.requiresRace != "" && len([for m in s.materials if cards[m].race != r.requiresRace {m}]) > 0 {"step \(s.n): \(s.result) requires \(r.requiresRace) materials"}],
			])
		},
	], 1)

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

	_zonesBefore: [
		for i, _ in steps {
			(#ZoneFold & {inSteps: list.Slice(steps, 0, i), acc: _initZones}).out
		},
	]

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

	errors: list.Concat([_deckErrors, _nsErrors, _matErrors, _lockErrors, _optErrors, _opdErrors, _zoneErrors, _matZoneErrors])
}
