// Line checker for Master Duel combo lines.
// CUE can't play the game; it checks the bookkeeping that we kept getting wrong:
//   - every card is in the deck and in the card database
//   - at most one Normal Summon
//   - each once-per-turn effect is used once
//   - a monster isn't used after it left the field (Tributed, used as material, ...)
//     unless something brought it back
//   - summon locks (Plant only, Plant or Dragon, Moonlit's Plant Xyz only, Cactus) allow every later summon
//   - Dark Law: no step that sends a card to your GY
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
	level?: int // Level, Rank or Link rating
	// Names of the card's effects. Each one is once per turn unless listed in notOpt.
	effects: [...string] | *[]
	notOpt: [...string] | *[]
	// Effects that send a card to your GY. Dark Law (and Macro-style cards) block these.
	gyEffects: [...string] | *[]
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
	steps: [...#Step]
	end: {
		mmz: [...string]
		emz: [...string] | *[]
	}

	let _deck = decks[deck]
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
			for x in uses
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

		// Dark Law: nothing can be sent to your GY.
		[if darkLaw for i, s in steps
			let n = strings.Split(s.card, "#")[0]
			if s.sendsToGY || (s.effect != "" && cards[n] != _|_ && list.Contains(cards[n].gyEffects, s.effect)) {
				"step \(i+1): \(n) sends a card to the GY, blocked by Dark Law"
			}],

		// Deck counts: no more copies taken from the Deck than the deck runs (minus copies in the starting hand).
		[for n, _ in {for y in _taken {(y): true}}
			let used = len([for y in _taken if y == n {y}]) + len([for h in hand if strings.Split(h, "#")[0] == n {h}])
			let have = *_deck.main[n] | 0
			if used > have {"takes \(used) \(n) (hand + Deck) but \(deck) runs \(have)"}],

		// Zones.
		[if len(end.mmz) > 5 {"end board uses \(len(end.mmz)) Main Monster Zones (max 5)"}],
		[if len(end.emz) > 2 {"end board uses \(len(end.emz)) Extra Monster Zones (max 2)"}],
	])
}

lines: [string]: #Line

// What check.sh prints.
report: {for k, l in lines {(k): {status: l.status, violations: l.violations}}}
