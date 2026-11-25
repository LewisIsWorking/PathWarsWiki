// Super Poly targets added 25 Nov 2026 (evening): Mudragon of the Swamp and Predaplant Dragostapelia.
// Card text checked on ProjectIgnis BabelCDB. All UNTESTED until played.
//
// Mudragon (Wyrm, WATER, 1900): 2 monsters with the same Attribute but different Types. A Wyrm, so
// every lock in the deck stops it (Predaprimitive, Dracaena, Petal, Black Princess, Konkon, Primrose,
// Rikka Princess, Moonlit): Super Poly FIRST, like Garura. Then its Quick Effect can make it WATER, so
// they can't target it or your WATER Rikka monsters.
// Dragostapelia (Plant, DARK, Level 8, 2700): 1 Fusion Monster + 1 DARK monster. A Plant, so it still
// works after Petal / Black Princess / Konkon / Primrose / Predaprimitive (only Moonlit stops it).
// Their DARK Fusions (Dragoon, Dark Law, Chaos, Chimeratech Fortress) are a 2-for-1.
package lines

import "list"

// Mudragon first, then the Garura-first turn (Predaprimitive engine, Moonlit, Teardrop the Rikka Sacred Queen).
#MudragonFirst: {
	X:       string
	Y:       string
	discard: string
	out: list.Concat([[
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: [discard], consumes: ["opp:\(X)", "opp:\(Y)"], summons: "Mudragon of the Swamp", note: "FIRST card. Discard \(discard); \(X) + \(Y) → Mudragon. Nobody can respond"},
	], (#GaruraFirst & {X: "x", Y: "y", discard: "d"}).out[1:]])
}
_mudragonEnd: ["Mudragon of the Swamp", "Teardrop the Rikka Sacred Queen", "Primrose the Rikka Fairy Duo", "Predaplant Bal Teah"]

lines: "Elfnote going 2nd, drawn Super Poly: Mudragon on Power Patron + Strelitzia": {
	source: "Claude, 25 Nov 2026 (card text; both FIRE: Power Patron is a Fiend, Strelitzia a Plant, so Garura can't but Mudragon can)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Super Polymerization", "Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Purulia", "Ash Blossom & Joyous Spring"]
	oppField: ["Elfnote Power Patron", "Elfnote Seraphim Strelitzia"]
	steps: (#MudragonFirst & {X: "Elfnote Power Patron", Y: "Elfnote Seraphim Strelitzia", discard: "Mulcharmy Purulia"}).out
	end: mmz: _mudragonEnd
	// Not lethal: Sacred Queen 3200 + Mudragon 1900 + Bal Teah 1900 = 7000 into an empty field.
}

lines: "Sky Striker going 2nd, drawn Super Poly: Mudragon on Zero + Roze": {
	source: "Claude, 25 Nov 2026 (card text; both LIGHT: Zero is a Machine, Roze a Warrior. Zero can't Tribute itself in response to Super Poly)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Super Polymerization", "Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring"]
	oppField: ["Sky Striker Ace = Zero", "Sky Striker Ace - Roze"]
	steps: (#MudragonFirst & {X: "Sky Striker Ace = Zero", Y: "Sky Striker Ace - Roze", discard: "Mulcharmy Fuwalos"}).out
	end: mmz: _mudragonEnd
	// Not lethal (7000). Teardrop the Rikka Sacred Queen sends their set Spells/Traps on their turn or before attacks.
}

// Dragostapelia AFTER the Plant lock: Line 1 (Petal alone) up to Black Princess's Tribute, then Super Poly
// on their DARK Fusion + another DARK monster, then the Rikka finish. Natasha's Horus / Dragoon board.
lines: "Natasha going 2nd: Petal line, then Super Poly on Dragoon + Imsety → Dragostapelia (after the Plant lock)": {
	source: "Claude, 25 Nov 2026 (card text; Dragoon is a DARK Fusion, Imsety is DARK. Dragoon can't negate Super Poly: no responses)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Rikka Petal", "Super Polymerization", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Red-Eyes Dark Dragoon", "Imsety, Glory of Horus", "Duamutef, Blessing of Horus"]
	steps: list.Concat([[
		{card: "Rikka Petal", action: "normal_summon", zone: "hand"},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"], note: "send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: ["Mulcharmy Fuwalos"], consumes: ["opp:Red-Eyes Dark Dragoon", "opp:Imsety, Glory of Horus"], summons: "Predaplant Dragostapelia", note: "BEFORE Moonlit Waters. Discard Fuwalos; Dragoon + Imsety → Dragostapelia (a Plant: fine under Petal's lock). Nobody can respond"},
		{card: "Predaplant Dragostapelia", action: "effect", effect: "counter", counter: "opp:Duamutef, Blessing of Horus", note: "Quick Effect, any time: Predator Counter on Duamutef; its activated effects are negated. Save it for their turn if they have more monsters to come"},
	], _rikkaTail])
	end: mmz: list.Concat([_tailEnd, ["Predaplant Dragostapelia"]])
}

lines: "KNOWN BAD: Mudragon after Predaprimitive": {
	source: "25 Nov 2026: Mudragon is a Wyrm; Predaprimitive allows only Plant or Dragon"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Super Polymerization", "Mulcharmy Purulia"]
	oppField: ["Elfnote Power Patron", "Elfnote Seraphim Strelitzia"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: ["Mulcharmy Purulia"], consumes: ["opp:Elfnote Power Patron", "opp:Elfnote Seraphim Strelitzia"], summons: "Mudragon of the Swamp"},
	]
	end: mmz: ["Mudragon of the Swamp"]
}

lines: "KNOWN BAD: Dragostapelia with no Fusion material (Raye + Lilizard)": {
	source: "25 Nov 2026: Dragostapelia needs a FUSION monster + a DARK monster; Raye and Lilizard are both Main Deck monsters"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Rikka Black Princess", "Super Polymerization", "Hellebore the Rikka Fairy"]
	startField: ["Predaplant Lilizard"]
	oppField: ["Sky Striker Ace - Raye"]
	steps: [
		{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: ["Hellebore the Rikka Fairy"], consumes: ["opp:Sky Striker Ace - Raye", "Predaplant Lilizard"], summons: "Predaplant Dragostapelia"},
	]
	end: mmz: ["Rikka Black Princess", "Predaplant Dragostapelia"]
}
