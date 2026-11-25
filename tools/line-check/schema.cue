// Line checker for Master Duel combo lines.
// CUE can't play the game; it checks the bookkeeping that we kept getting wrong:
//   - every card is in the deck and in the card database
//   - at most one Normal Summon
//   - each once-per-turn effect is used once
//   - a monster isn't used after it left the field (Tributed, used as material, ...)
//     unless something brought it back
//   - summon locks (Plant only, Plant or Dragon, Moonlit's Plant Xyz only, Cactus) allow every later summon
//   - Dark Law: no step that sends a card to your GY
//   - Droll: no step that must add from the Deck once Droll resolved
//   - Moonlit Waters takes 2 Deck monsters with the same Level and different names
//   - an Xyz effect that needs material (Rikka Queen Strenna's float) still has some
//   - lethal: only Attack-position monsters on the end board count, and the ATK adds up
//   - locks already on from an earlier turn (Cactus Bouncer + any Plant on either field)
//   - the end board fits: 5 Main Monster Zones, 2 Extra Monster Zones
// Run ./check.sh from this folder.
package lines

import (
	"list"
	"strings"
)

#Frame: "main" | "fusion" | "synchro" | "xyz" | "link"

#Card: {
	frame: #Frame | *"main"
	kind:  "monster" | "spell" | "trap"
	race: string | *""
	attr: string | *"" // Attribute (DARK, LIGHT, ...): Fusion material checks
	level?: int // Level, Rank or Link rating
	tuner: bool | *false
	// Names of the card's effects. Each one is once per turn unless listed in notOpt.
	effects: [...string] | *[]
	notOpt: [...string] | *[]
	// Effects that send a card to your GY. Dark Law (and Macro-style cards) block these.
	gyEffects: [...string] | *[]
	// Effects that must add a card from the Deck to the hand. Under Droll & Lock Bird,
	// Master Duel won't let you activate them (tested with Moonlit Waters, 25 Nov 2026).
	addEffects: [...string] | *[]
	// Effects that Special Summon in Defence Position (the card itself, or the monster in the step's `summons`).
	defEffects: [...string] | *[]
	// Effects that only work while this Xyz Monster has material (Rikka Queen Strenna's "if Tributed with material").
	needsMaterial: [...string] | *[]
	// Effects that take 2 monsters from the Deck with the same Level but different names
	// (Moonlit Waters: add 1, send the other). Both come from the Deck, never the hand.
	pairEffects: [...string] | *[]
	atk?: int
}

cards: [string]: #Card

#Deck: [string]: int & >0

decks: [string]: {
	main:  #Deck
	extra: #Deck
}

// Summon locks a step applies for the rest of the turn.
#Lock: "plant" | "plant_or_dragon" | "extra_plant_xyz" | "no_special"

#Action: "normal_summon" | "special_summon" | "activate" | "effect" | "xyz" | "synchro" | "link" | "fusion" | "set"

// Actions that put the step's own card on the field.
_enterActions: ["normal_summon", "special_summon", "activate", "xyz", "synchro", "link", "fusion", "set"]
// Actions that Special Summon the step's own card.
_specialActions: ["special_summon", "xyz", "synchro", "link", "fusion"]

#Step: {
	// Card instance: the card name, plus "#2" etc. when you have more than one copy in play.
	card:   string
	action: #Action
	// Which of the card's effects this step uses (see cards.cue). Needed for "effect" and "activate".
	effect: string | *""
	// Where the card is when this step happens. Only "field" steps are checked for
	// "used after it left the field".
	zone: *"field" | "hand" | "gy" | "deck" | "extra"
	// Instance this step Special Summons when it isn't the step's own card
	// (e.g. Black Princess's effect summoning Mudan from the Deck).
	summons: string | *""
	// Field monsters that leave the field in this step: Tributes, materials, costs.
	// Prefix the opponent's cards with "opp:" (e.g. Konkon Tributing "opp:Masked HERO Dark Law").
	consumes: [...string] | *[]
	// Cards Tributed or discarded from the hand (not checked).
	fromHand: [...string] | *[]
	// Cards this step takes from the Deck (adds, sends, attaches, summons).
	// The line can't take more copies of a card than the deck runs.
	fromDeck: [...string] | *[]
	// The summon lock this step applies for the rest of the turn.
	lock: #Lock | *""
	// This step sends a card to your GY (e.g. Petal sending instead of adding).
	sendsToGY: bool | *false
	// Level changes this step makes, e.g. Primrose: {"Hellebore the Rikka Fairy": 6}.
	setLevel: [string]: int
	// Xyz Summon on top of another Xyz (Teardrop the Rikka Sacred Queen over Teardrop): skip the material Level check.
	rankUp: bool | *false
	// Materials this step attaches to the monster in `summons` (Sacred Queen Strenna's optional attach).
	attach: [...string] | *[]
	// Materials this step detaches from the step's own card.
	detach: int | *0
	// Lilizard: the monster this step makes DARK until the end of the turn (e.g. "opp:Sky Striker Ace = Zero").
	makesDark: string | *""
	// Longinephila (GY): the monster this step puts a Predator Counter on (it becomes Level 1).
	counter: string | *""
	// Monsters this step summons that can't be Link Material (Sylvan Dancepione's excavated Plants).
	noLink: [...string] | *[]
	note?: string
}

#Line: {
	name:   string
	source: string
	status: "proven" | "untested" | "known_bad"
	deck:   string
	hand: [...string]
	// Cards already on your field before the line starts.
	startField: [...string] | *[]
	darkLaw: bool | *false
	// Droll & Lock Bird resolved before this step (1-based); 0 = no Droll.
	drollFrom: int | *0
	// Summon locks already on when the line starts, e.g. "no_special" for Cactus Bouncer
	// with any other Plant on either field (their Elfnote Strelitzia counts).
	startLocks: [...#Lock] | *[]
	// The opponent's face-up monsters at the start. When given: every "opp:" card the line
	// Tributes or uses must be here, each can leave only once, and lethal needs them all gone.
	oppField: [...string] | *[]
	// Cards no longer in your Deck (drawn, used or sent earlier in the Duel), e.g. {"Predaplant Byblisp": 1}.
	deckGone: [string]: int
	// Optional damage check. attackers: monsters that attack (must be on the end board and
	// not summoned in Defence). bonus: extra ATK (e.g. Teardrop +200 per Tribute).
	lethal?: {
		lp: int
		attackers: [...string]
		bonus: [string]: int
		// Their monsters that stay but don't stop lethal (explain in a note).
		ignore: [...string] | *[]
	}
	steps: [...#Step]
	end: {
		mmz: [...string]
		emz: [...string] | *[]
	}

	let _deck = decks[deck]
	_konkonSteps: [for i, s in steps
		if list.Contains(_konkonUsers, strings.Split(s.card, "#")[0])
		if len([for c in s.consumes if strings.HasPrefix(c, "opp:") {c}]) > 0 {i}]
	_taken: list.Concat([for s in steps {[for x in s.fromDeck {strings.Split(x, "#")[0]}]}])

	violations: list.Concat([
		// Card exists in the database and the deck.
		[for i, s in steps
			let n = strings.Split(s.card, "#")[0]
			if cards[n] == _|_ {"step \(i+1): \(n) is not in cards.cue"}],
		[for i, s in steps
			let n = strings.Split(s.card, "#")[0]
			if _deck.main[n] == _|_ && _deck.extra[n] == _|_ {"step \(i+1): \(n) is not in deck \(deck)"}],
		[for i, s in steps if s.summons != ""
			let n = strings.Split(s.summons, "#")[0]
			if _deck.main[n] == _|_ && _deck.extra[n] == _|_ {"step \(i+1): \(n) is not in deck \(deck)"}],

		// Effect name is one of the card's effects.
		[for i, s in steps if s.effect != ""
			let n = strings.Split(s.card, "#")[0]
			if cards[n] != _|_
			if !list.Contains(cards[n].effects, s.effect) {"step \(i+1): \(n) has no effect called '\(s.effect)'"}],

		// One Normal Summon.
		[if len([for s in steps if s.action == "normal_summon" {s}]) > 1 {"more than one Normal Summon"}],

		// Once-per-turn effects (hard once per turn: by card name, not by copy).
		[for i, s in steps if s.effect != ""
			for j, t in steps if j > i && t.effect != ""
			let a = strings.Split(s.card, "#")[0]
			let b = strings.Split(t.card, "#")[0]
			if a == b && s.effect == t.effect
			if cards[a] != _|_
			if !list.Contains(cards[a].notOpt, s.effect) {"steps \(i+1) and \(j+1): \(a) '\(s.effect)' is once per turn"}],

		// A field card must be on the field: it entered before, and nothing removed it since.
		[for j, t in steps
			let uses = list.Concat([[if t.zone == "field" && !list.Contains(_enterActions, t.action) {t.card}], t.consumes])
			for x in uses if !strings.HasPrefix(x, "opp:")
			let enters = list.Concat([
				[if list.Contains(startField, x) {-1}],
				[for i, s in steps if i < j && ((s.summons != "" && s.summons == x) || (s.card == x && list.Contains(_enterActions, s.action))) {i}],
			])
			let leaves = [for i, s in steps if i < j && list.Contains(s.consumes, x) {i}]
			let lastIn = list.Max(list.Concat([[-2], enters]))
			let lastOut = list.Max(list.Concat([[-2], leaves]))
			if lastIn == -2 || lastOut >= lastIn {
				"step \(j+1): \(x) isn't on the field (never summoned, or it left the field earlier)"
			}],

		// Summon locks.
		[for j, t in steps
			let summoned = list.Concat([[if t.summons != "" {t.summons}], [if list.Contains(_specialActions, t.action) {t.card}]])
			for x in summoned
			let n = strings.Split(x, "#")[0]
			if cards[n] != _|_
			let c = cards[n]
			for i, s in steps if i < j && s.lock != ""
			if (s.lock == "no_special") ||
				(s.lock == "plant" && c.race != "Plant") ||
				(s.lock == "plant_or_dragon" && c.race != "Plant" && c.race != "Dragon") ||
				(s.lock == "extra_plant_xyz" && c.frame != "main" && (c.frame != "xyz" || c.race != "Plant")) {
				"step \(j+1): \(n) breaks the '\(s.lock)' lock from step \(i+1)"
			}],

		// Locks already on from an earlier turn.
		[for j, t in steps
			let summoned = list.Concat([[if t.summons != "" {t.summons}], [if list.Contains(_specialActions, t.action) {t.card}]])
			for x in summoned
			let n = strings.Split(x, "#")[0]
			if cards[n] != _|_
			let c = cards[n]
			for l in startLocks
			if (l == "no_special") ||
				(l == "plant" && c.race != "Plant") ||
				(l == "plant_or_dragon" && c.race != "Plant" && c.race != "Dragon") ||
				(l == "extra_plant_xyz" && c.frame != "main" && (c.frame != "xyz" || c.race != "Plant")) {
				"step \(j+1): \(n) breaks the '\(l)' lock already on at the start"
			}],

		// Xyz material: effects that need material (Rikka Queen Strenna's float) fail at 0.
		[for j, t in steps if t.effect != ""
			let n = strings.Split(t.card, "#")[0]
			if cards[n] != _|_
			if list.Contains(cards[n].needsMaterial, t.effect)
			let enter = list.Max(list.Concat([[-1], [for i, s in steps if i < j && (s.summons == t.card || (s.card == t.card && list.Contains(_specialActions, s.action))) {i}]]))
			let got = list.Sum(list.Concat([
				[for i, s in steps if i >= enter && i < j && s.card == t.card && s.action == "xyz" {len(s.consumes)}],
				[for i, s in steps if i >= enter && i < j && s.summons == t.card {len(s.attach)}],
				[for i, s in steps if i >= enter && i < j && s.card == t.card {-s.detach}],
			]))
			if got <= 0 {"step \(j+1): \(n) has no material left, so '\(t.effect)' does nothing (attach a Rikka monster when you summon it)"}],

		// Lethal: attackers are on the end board, in Attack Position, and the ATK adds up.
		[if lethal != _|_ for a in lethal.attackers if !list.Contains(list.Concat([end.mmz, end.emz]), a) {"lethal: \(a) isn't on the end board"}],
		[if lethal != _|_ for a in lethal.attackers
			let ins = [for i, s in steps if s.summons == a || (s.card == a && list.Contains(_enterActions, s.action)) {i}]
			if len(ins) > 0
			let s = steps[ins[len(ins)-1]]
			let sn = strings.Split(s.card, "#")[0]
			if cards[sn] != _|_ && s.effect != "" && list.Contains(cards[sn].defEffects, s.effect) {
				"lethal: \(a) was summoned in Defence Position (step \(ins[len(ins)-1]+1)) and can't attack"
			}],
		[if lethal != _|_ for a in lethal.attackers if cards[strings.Split(a, "#")[0]].atk == _|_ {"lethal: no ATK for \(a) in cards.cue"}],
		[if lethal != _|_
			let total = list.Sum(list.Concat([
				[for a in lethal.attackers if cards[strings.Split(a, "#")[0]].atk != _|_ {cards[strings.Split(a, "#")[0]].atk}],
				[for _, v in lethal.bonus {v}],
			]))
			if total < lethal.lp {"lethal: attacks total \(total), they have \(lethal.lp) LP"}],

		// Pair takes (Moonlit Waters): exactly 2 cards from the Deck, same Level, different names.
		[for i, s in steps if s.effect != ""
			let n = strings.Split(s.card, "#")[0]
			if cards[n] != _|_
			if list.Contains(cards[n].pairEffects, s.effect)
			let ps = [for x in s.fromDeck {strings.Split(x, "#")[0]}]
			if len(ps) != 2 || ps[0] == ps[len(ps)-1] || (cards[ps[0]] != _|_ && cards[ps[len(ps)-1]] != _|_ && cards[ps[0]].level != cards[ps[len(ps)-1]].level) {
				"step \(i+1): \(n) takes 2 Rikka monsters from the Deck with the same Level and different names (got \(strings.Join(ps, " + ")))"
			}],

		// Dark Law: nothing can be sent to your GY.
		[if darkLaw for i, s in steps
			let n = strings.Split(s.card, "#")[0]
			if s.sendsToGY || (s.effect != "" && cards[n] != _|_ && list.Contains(cards[n].gyEffects, s.effect)) {
				"step \(i+1): \(n) sends a card to the GY, blocked by Dark Law"
			}],

		// Droll: no more adds from the Deck.
		[if drollFrom > 0 for i, s in steps if i+1 >= drollFrom
			let n = strings.Split(s.card, "#")[0]
			if s.effect != "" && cards[n] != _|_ && list.Contains(cards[n].addEffects, s.effect) {
				"step \(i+1): \(n) '\(s.effect)' must add from the Deck, blocked by Droll (from step \(drollFrom))"
			}],

		// Deck counts: no more copies taken from the Deck than the deck runs (minus copies in the starting hand).
		[for n, _ in {for y in _taken {(y): true}}
			let used = len([for y in _taken if y == n {y}]) + len([for h in hand if strings.Split(h, "#")[0] == n {h}])
			let have = (*_deck.main[n] | 0) - (*deckGone[n] | 0)
			if used > have {"takes \(used) \(n) (hand + Deck) but \(deck) runs \(have)"}],

		// Xyz materials: every material's current Level equals the Rank.
		[for j, t in steps if t.action == "xyz" && !t.rankUp
			let n = strings.Split(t.card, "#")[0]
			if cards[n] != _|_
			for m in t.consumes if !strings.HasPrefix(m, "opp:")
			let mn = strings.Split(m, "#")[0]
			if cards[mn] != _|_
			let changed = [for i, s in steps if i < j if s.setLevel[m] != _|_ {s.setLevel[m]}]
			let lv = [if len(changed) > 0 {changed[len(changed)-1]}, cards[mn].level][0]
			if lv != cards[n].level {"step \(j+1): \(mn) is Level \(lv), \(n) needs Rank \(cards[n].level) materials"}],
		[for j, t in steps if t.action == "xyz" && !t.rankUp && len(t.consumes) < 2 {"step \(j+1): Xyz Summon needs 2+ materials"}],

		// Synchro: exactly 1 Tuner, and the Levels add up.
		[for j, t in steps if t.action == "synchro"
			let n = strings.Split(t.card, "#")[0]
			if cards[n] != _|_
			let mats = [for m in t.consumes if cards[strings.Split(m, "#")[0]] != _|_ {
				let changed = [for i, s in steps if i < j if s.setLevel[m] != _|_ {s.setLevel[m]}]
				lv:    [if len(changed) > 0 {changed[len(changed)-1]}, cards[strings.Split(m, "#")[0]].level][0]
				tuner: cards[strings.Split(m, "#")[0]].tuner
			}]
			let total = list.Sum([for x in mats {x.lv}])
			let tuners = len([for x in mats if x.tuner {x}])
			if total != cards[n].level || tuners != 1 {"step \(j+1): \(n) (Level \(cards[n].level)) needs 1 Tuner + non-Tuners adding up; got Level \(total) with \(tuners) Tuner(s)"}],

		// Link: number of materials equals the Link rating (every Link we use takes 1-rating materials).
		[for j, t in steps if t.action == "link"
			let n = strings.Split(t.card, "#")[0]
			if cards[n] != _|_
			if len(t.consumes) != cards[n].level {"step \(j+1): \(n) is Link-\(cards[n].level) but uses \(len(t.consumes)) materials"}],

		// Link materials: Jasmine and Dancepione take 2 Plant monsters; Dancepione's excavated Plants can't be used.
		[for j, t in steps if t.action == "link"
			let n = strings.Split(t.card, "#")[0]
			if _linkRace[n] != _|_
			for m in t.consumes
			let mn = strings.Split(strings.TrimPrefix(m, "opp:"), "#")[0]
			if cards[mn] != _|_ && cards[mn].race != _linkRace[n] {"step \(j+1): \(n) needs 2 \(_linkRace[n]) monsters; \(mn) is a \(cards[mn].race)"}],
		[for j, t in steps if t.action == "link"
			for m in t.consumes
			if len([for i, s in steps if i < j && list.Contains(s.noLink, m) {1}]) > 0 {"step \(j+1): \(m) was summoned by Sylvan Dancepione and can't be Link Material"}],
		// One Extra Monster Zone per player (a second one only through an Extra Link).
		[if len([for x in end.emz if cards[strings.Split(x, "#")[0]] != _|_ {x}]) > 1 {"end board has \(len(end.emz)) monsters in Extra Monster Zones; you can use only 1 (put Fusion/Synchro/Xyz in Main Monster Zones; a second Link goes in a zone the first one points to)"}],

		// Fusion materials (Super Poly, Daredevil's Tribute summon). Lilizard's makesDark and
		// Longinephila's counter (Level 1) count from the step they happen.
		[for j, t in steps
			let fn = strings.Split([if t.summons != "" {t.summons}, t.card][0], "#")[0]
			if _fusionRule[fn] != _|_ && len(t.consumes) > 0
			for m in t.consumes
			let nm = strings.Split(strings.TrimPrefix(m, "opp:"), "#")[0]
			if cards[nm] == _|_ {"step \(j+1): \(nm) (Fusion material) is not in cards.cue"}],
		[for j, t in steps
			let fn = strings.Split([if t.summons != "" {t.summons}, t.card][0], "#")[0]
			if _fusionRule[fn] != _|_ && len(t.consumes) > 0
			let mats = [for m in t.consumes
				let nm = strings.Split(strings.TrimPrefix(m, "opp:"), "#")[0]
				if cards[nm] != _|_ {
					let dk = len([for i, s in steps if i < j && s.makesDark == m {1}]) > 0
					let ct = len([for i, s in steps if i < j && s.counter == m {1}]) > 0
					name:  nm
					opp:   strings.HasPrefix(m, "opp:")
					attr:  [if dk {"DARK"}, cards[nm].attr][0]
					race:  cards[nm].race
					lv1:   ct || (*cards[nm].level | 0) == 1
					ctr:   ct
					preda: strings.HasPrefix(nm, "Predaplant")
				}]
			let rule = _fusionRule[fn]
			let contact = t.card == fn && t.action == "special_summon"
			if len(mats) == len(t.consumes)
			if (len(mats) != 2) ||
				(rule == "dark2" && (mats[0].attr != "DARK" || mats[1].attr != "DARK")) ||
				(rule == "garura" && (mats[0].race != mats[1].race || mats[0].attr != mats[1].attr || mats[0].name == mats[1].name)) ||
				(rule == "daredevil" && !contact && !((mats[0].preda && mats[1].lv1) || (mats[1].preda && mats[0].lv1))) ||
				(rule == "daredevil" && contact && !((mats[0].preda && !mats[0].opp && mats[1].ctr) || (mats[1].preda && !mats[1].opp && mats[0].ctr))) {
				"step \(j+1): \(fn) can't use \(strings.Join([for x in mats {"\(x.name) (\(x.attr) \(x.race))"}], " + ")) (\(_fusionText[rule]))"
			}],

		// Opponent's field.
		[if len(oppField) > 0 for j, t in steps for x in list.Concat([t.consumes, [t.makesDark, t.counter]])
			if strings.HasPrefix(x, "opp:") && !list.Contains(oppField, strings.TrimPrefix(x, "opp:")) {
				"step \(j+1): \(strings.TrimPrefix(x, "opp:")) isn't on their field (oppField)"
			}],
		[for x in oppField
			let n = len([for s in steps for c in s.consumes if c == "opp:\(x)" {1}])
			if n > 1 {"\(x) leaves their field \(n) times"}],
		[for j, t in steps for x in [t.makesDark, t.counter] if strings.HasPrefix(x, "opp:")
			if len([for i, s in steps if i < j for c in s.consumes if c == x {1}]) > 0 {"step \(j+1): \(strings.TrimPrefix(x, "opp:")) already left their field"}],
		[if lethal != _|_ for x in oppField
			if !list.Contains(lethal.ignore, x)
			if len([for s in steps for c in s.consumes if c == "opp:\(x)" {1}]) == 0 {"lethal: \(x) is still on their field"}],

		// Konkon: Tributing their monster for a Rikka cost needs Konkon face-up, once per turn.
		[if len(_konkonSteps) > 1 {"Konkon's replacement Tribute is once per turn (steps \(strings.Join([for i in _konkonSteps {"\(i+1)"}], ", ")))"}],
		[for i in _konkonSteps
			if !list.Contains(startField, "Rikka Konkon")
			if len([for k, s in steps if k < i && s.card == "Rikka Konkon" && s.action == "activate" {1}]) == 0 {
				"step \(i+1): Tributes their monster, but Rikka Konkon isn't face-up yet"
			}],

		// Zones.
		[if len(end.mmz) > 5 {"end board uses \(len(end.mmz)) Main Monster Zones (max 5)"}],
		[if len(end.emz) > 2 {"end board uses \(len(end.emz)) Extra Monster Zones (max 2)"}],
	])
}

// Link Monsters whose materials must be one Type.
_linkRace: {
	"Aromaseraphy Jasmine": "Plant"
	"Sylvan Dancepione":    "Plant"
}

// Fusion Monsters whose materials are checked, and what they need.
_fusionRule: {
	"Starving Venom Fusion Dragon":   "dark2"
	"Garura, Wings of Resonant Life": "garura"
	"Predaplant Daredevil":           "daredevil"
}
_fusionText: {
	dark2:     "needs 2 DARK monsters: use Lilizard's makesDark on the other one"
	garura:    "needs 2 monsters with the same Type and Attribute, different names"
	daredevil: "needs a Predaplant + a Level 1 monster; its Tribute summon needs a Predaplant you control + a monster with a Predator Counter"
}
// Rikka cards whose cost Tributes a Plant you control, so Konkon can Tribute their monster instead.
_konkonUsers: ["Rikka Black Princess", "Mudan the Rikka Fairy", "Rikka Glamour", "Rikka Moonlit Waters", "Hellebore the Rikka Fairy", "Rikka Princess", "Rikka Sheet"]

lines: [N=string]: #Line & {name: *N | string}

// What check.sh prints.
report: {for k, l in lines {(k): {status: l.status, violations: l.violations}}}
