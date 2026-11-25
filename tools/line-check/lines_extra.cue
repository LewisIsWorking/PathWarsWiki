// Extra Deck routes: Link bridges (Jasmine, Sylvan Dancepione) for low-resource turns, plus
// known-bad Extra Deck mistakes. Card text checked on ProjectIgnis BabelCDB, 25 Nov 2026.
// All UNTESTED. Same steps as Rikka.md "Extra Deck routes".
package lines

import "list"

// The Jasmine bridge: any 3 Plant monsters (2 for Jasmine, 1 under its arrow) become
// Black Princess + Mudan, then the Rikka finish (R). Needs: no Moonlit Waters yet (its lock
// stops Jasmine), the Extra Monster Zone free, Mudan's search unused.
lines: "Jasmine bridge: any 3 Plants on the field": {
	source: "Claude, 25 Nov 2026, from card text (proven Predap line's Jasmine step + Line 1)"
	status: "untested"
	deck:   "PredaRikka"
	hand: []
	startField: ["Predaplant Lilizard", "Predaplant Byblisp", "Predaplant Longinephila"]
	steps: list.Concat([[
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Lilizard", "Predaplant Byblisp"], note: "Extra Monster Zone, the 3rd Plant under an arrow (Byblisp to the GY also searches a Predaplant)"},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Longinephila"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Aromaseraphy Jasmine"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "Tribute Jasmine (or a spare Plant from the hand, then Jasmine stays)"},
	], _rikkaTail])
	end: mmz: _tailEnd
}

// Instant Fusion + Mudan: Jasmine turns Ambulomelides + Lilizard + Mudan into Black Princess + Mudan #2.
// Also works late game with no Predaplant left in the Deck, as long as Lilizard is in the GY
// (Ambulomelides adds it from the GY): the Ryuuku turn-5 hand (S17) without the dead Predaprimitive.
lines: "Instant Fusion + Mudan (Jasmine bridge; late game too, Lilizard from the GY)": {
	source: "Claude, 25 Nov 2026, from card text (S17 re-check)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Instant Fusion", "Mudan the Rikka Fairy"]
	steps: [
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaplant Lilizard"], note: "add Lilizard (from the GY if the Deck has none)"},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self", note: "you control Ambulomelides"},
		{card: "Mudan the Rikka Fairy", action: "normal_summon", zone: "hand", note: "in a zone Jasmine will point to"},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"], note: "Moonlit waits until after Jasmine"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Ambulomelides", "Predaplant Lilizard"], note: "Extra Monster Zone, pointing at Mudan"},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Mudan the Rikka Fairy"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Aromaseraphy Jasmine"], summons: "Mudan the Rikka Fairy#2", fromDeck: ["Mudan the Rikka Fairy"], note: "no search (used)"},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy#2", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "CL1"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"], note: "CL2"},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"], lock: "plant", note: "CL3"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#2": 8}},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Primrose: attach Mudan from the GY"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#2", "Hellebore the Rikka Fairy"]},
	]
	end: mmz: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Primrose the Rikka Fairy Duo"]
}

// --- Known-bad Extra Deck mistakes: these PASS only when the checker catches the problem. ---

lines: "KNOWN BAD: Jasmine after Moonlit Waters": {
	source: "Extra Deck audit, 25 Nov 2026: Moonlit's lock allows only Plant Xyz from the Extra Deck"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Rikka Moonlit Waters"]
	startField: ["Predaplant Lilizard", "Predaplant Byblisp"]
	steps: [
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Lilizard", "Predaplant Byblisp"]},
	]
	end: emz: ["Aromaseraphy Jasmine"]
	end: mmz: []
}

lines: "KNOWN BAD: Jasmine with a non-Plant": {
	source: "Extra Deck audit, 25 Nov 2026: Jasmine and Dancepione need 2 Plant monsters"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: []
	startField: ["Starving Venom Fusion Dragon", "Predaplant Lilizard"]
	steps: [
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Starving Venom Fusion Dragon", "Predaplant Lilizard"]},
	]
	end: emz: ["Aromaseraphy Jasmine"]
	end: mmz: []
}

lines: "KNOWN BAD: Dancepione's excavated Plant as Link Material": {
	source: "Extra Deck audit, 25 Nov 2026: Dancepione's summons can't be Link Material"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: []
	startField: ["Predaplant Lilizard", "Predaplant Byblisp", "Predaplant Longinephila"]
	steps: [
		{card: "Sylvan Dancepione", action: "link", zone: "extra", consumes: ["Predaplant Lilizard", "Predaplant Byblisp"]},
		{card: "Sylvan Dancepione", action: "effect", effect: "excavate", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], noLink: ["Rikka Black Princess"], note: "excavated a Black Princess"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Rikka Black Princess", "Predaplant Longinephila"]},
	]
	end: mmz: ["Sylvan Dancepione", "Aromaseraphy Jasmine"]
}

lines: "KNOWN BAD: Jasmine and Dancepione both in Extra Monster Zones": {
	source: "Extra Deck audit, 25 Nov 2026: one Extra Monster Zone per player"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: []
	startField: ["Predaplant Lilizard", "Predaplant Byblisp", "Predaplant Longinephila", "Princess Dracaena, the Thirsting Tree"]
	steps: [
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Lilizard", "Predaplant Byblisp"]},
		{card: "Sylvan Dancepione", action: "link", zone: "extra", consumes: ["Predaplant Longinephila", "Princess Dracaena, the Thirsting Tree"]},
	]
	end: emz: ["Aromaseraphy Jasmine", "Sylvan Dancepione"]
	end: mmz: []
}

// Garura first: a DRAWN Super Poly on two of their monsters with the same Type and Attribute
// (different names) removes both, before any lock (Garura is a Winged Beast: Predaprimitive's
// Plant/Dragon lock and every Rikka lock stop it). Then Predaprimitive adds Super Poly #2 to hold.
#GaruraFirst: {
	X:       string
	Y:       string
	discard: string
	out: [
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: [discard], consumes: ["opp:\(X)", "opp:\(Y)"], summons: "Garura, Wings of Resonant Life", note: "FIRST card. Discard \(discard); \(X) + \(Y) → Garura. Nobody can respond"},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"], note: "add Super Poly #2: hold it for their turn"},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila", "Predaplant Lilizard"], note: "Main Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Predaplant Lilizard"], note: "Tribute LILIZARD (Bal Teah attacks for more)"},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], lock: "plant"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess", "Hellebore the Rikka Fairy"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen"], note: "on top of Teardrop: 3 materials, Attack Position"},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", note: "their turn or before attacks: send their set cards"},
	]
}
_garuraEnd: ["Garura, Wings of Resonant Life", "Teardrop the Rikka Sacred Queen", "Primrose the Rikka Fairy Duo", "Predaplant Bal Teah"]
_garuraLethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Garura, Wings of Resonant Life", "Predaplant Bal Teah"], bonus: {"Garura doubles its battle damage": 1500}}

lines: "Machina going 2nd, drawn Super Poly: Garura on Fortress + Air Raider": {
	source: "Claude, 25 Nov 2026, Extra Deck audit (card text; both are EARTH Machines)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Super Polymerization", "Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Purulia", "Ash Blossom & Joyous Spring"]
	oppField: ["Machina Fortress", "Machina Air Raider"]
	steps: (#GaruraFirst & {X: "Machina Fortress", Y: "Machina Air Raider", discard: "Mulcharmy Purulia"}).out
	end: mmz: _garuraEnd
	lethal: _garuraLethal
}

lines: "Cyber Dragon going 2nd, drawn Super Poly: Garura on Infinity + Cyber Dragon": {
	source: "Claude, 25 Nov 2026, Extra Deck audit (card text; both are LIGHT Machines, Infinity can't respond to Super Poly. NOT Nova: sent to the GY by your effect, it summons a Machine Fusion)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Super Polymerization", "Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring"]
	oppField: ["Cyber Dragon Infinity", "Cyber Dragon"]
	steps: (#GaruraFirst & {X: "Cyber Dragon Infinity", Y: "Cyber Dragon", discard: "Mulcharmy Fuwalos"}).out
	end: mmz: _garuraEnd
	lethal: _garuraLethal
}

lines: "KNOWN BAD: Garura after Predaprimitive": {
	source: "Extra Deck audit, 25 Nov 2026: Garura is a Winged Beast; Predaprimitive allows only Plant or Dragon"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Super Polymerization", "Mulcharmy Purulia"]
	oppField: ["Machina Fortress", "Machina Air Raider"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: ["Mulcharmy Purulia"], consumes: ["opp:Machina Fortress", "opp:Machina Air Raider"], summons: "Garura, Wings of Resonant Life"},
	]
	end: mmz: ["Garura, Wings of Resonant Life"]
}
