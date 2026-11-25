// Going-first lookup table for Lewis's PredaRikka list (25 Nov 2026).
// One line per opening starter (and the common 2-card pairs), so the live coach can paste a
// checked full combo instead of building one under the timer. Card text checked on BabelCDB.
// All UNTESTED unless marked proven. Same steps as Rikka.md "Going first: lookup table".
package lines

import "list"

// Rikka half used by several lines (Line 1 from step 4): Mudan and Black Princess are on the field,
// Mudan's search unused, Konkon not yet found.
// End: Teardrop, Hyperyton, Sacred Queen Strenna, Primrose, Konkon, set Sheet; Rikka Princess in the GY.
_rikkaTail: [
	{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
	{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
	{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
	{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"], note: "attach Rikka Princess"},
	{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
	{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
	{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "CL1"},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"], note: "CL2"},
	{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"], lock: "plant", note: "CL3"},
	{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#2": 8}},
	{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Primrose: attach Mudan from the GY"},
	{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#2", "Hellebore the Rikka Fairy"]},
]
_tailEnd: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Primrose the Rikka Fairy Duo"]

lines: "1st: Rikka Petal alone (Line 1)": {
	source: "Line 1 (Yusodus 1c Petal/Glamour), PredaRikka copy counts"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Rikka Petal"]
	steps: list.Concat([[
		{card: "Rikka Petal", action: "normal_summon", zone: "hand"},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"], note: "send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	], _rikkaTail])
	end: mmz: _tailEnd
}

lines: "1st: Rikka Glamour alone (Glamour adds Petal, then Line 1)": {
	source: "Line 1 (Yusodus 1c Petal/Glamour)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Rikka Glamour"]
	steps: list.Concat([[
		{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", fromDeck: ["Rikka Petal"], note: "no Tribute: add Petal only"},
		{card: "Rikka Petal", action: "normal_summon", zone: "hand"},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	], _rikkaTail])
	end: mmz: _tailEnd
}

// Black Princess + any spare Plant in hand: Line 1 from step 4, Normal Summon unused.
// Spare = Longinephila, Dracaena, Byblisp, Lilizard or Mudan. NOT Hellebore or Primrose (Moonlit needs both
// in the Deck) and not Cactus (see "Black Princess alone (+ Cactus)").
for spare in ["Predaplant Byblisp", "Predaplant Longinephila", "Princess Dracaena, the Thirsting Tree", "Predaplant Lilizard", "Mudan the Rikka Fairy"] {
	lines: "1st: Black Princess + spare Plant (\(spare))": {
		source: "Line 1 / Line B start (Yusodus)"
		status: "untested"
		deck:   "PredaRikka"
		hand: ["Rikka Black Princess", spare]
		steps: list.Concat([[
			{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
			{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", fromHand: [spare], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "Tribute the spare Plant FROM HAND"},
		], _rikkaTail])
		end: mmz: _tailEnd
	}
}

// Black Princess with no other Plant: weak. Teardrop + Primrose (+ Cactus if you hold it).
for nm, extra in {"alone": [], "+ Cactus": ["Cactus Bouncer"]} {
	lines: "1st: Black Princess \(nm)": {
		source: "Claude, 25 Nov 2026, from card text"
		status: "untested"
		deck:   "PredaRikka"
		hand: list.Concat([["Rikka Black Princess"], extra])
		steps: list.Concat([[
			{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
			{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Black Princess"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "Tribute herself"},
			{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
			{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
			{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
			{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
			{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Mudan the Rikka Fairy"]},
			{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"], lock: "plant"},
			{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#2": 8}},
			{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#2", "Hellebore the Rikka Fairy"]},
		], [for c in extra {card: c, action: "normal_summon", zone: "hand", lock: "no_special", note: "Cactus last"}]])
		end: mmz: list.Concat([["Teardrop the Rikka Queen", "Primrose the Rikka Fairy Duo"], extra])
	}
}

// Mudan alone: Normal Summon it (Attack). Primrose brings Petal, Petal finds Black Princess.
lines: "1st: Mudan alone": {
	source: "Claude, 25 Nov 2026, from card text"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Mudan the Rikka Fairy"]
	steps: [
		{card: "Mudan the Rikka Fairy", action: "normal_summon", zone: "hand", note: "Attack position"},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Mudan the Rikka Fairy"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Petal", fromDeck: ["Rikka Petal"], lock: "plant", note: "Primrose + PETAL"},
		{card: "Rikka Petal", action: "effect", effect: "take", lock: "plant", fromDeck: ["Rikka Black Princess"], note: "ADD Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy#2", fromDeck: ["Mudan the Rikka Fairy"], note: "no search (used)"},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy#2", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"]},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Hellebore the Rikka Fairy", "Primrose the Rikka Fairy Duo"]},
		{card: "Teardrop the Rikka Queen", action: "effect", effect: "tribute", detach: 1, consumes: ["Rikka Queen Strenna"], note: "detach 1, Tribute Rikka Queen Strenna"},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
	]
	end: mmz: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna"]
}

// Moonlit Waters alone: Line A in PredaRikka (1 Rikka Princess): Strenna gets Black Princess,
// Glamour adds Rikka Princess + Cactus, Rikka Princess stays in hand (her negate works from hand).
lines: "1st: Moonlit Waters alone (Line A, PredaRikka)": {
	source: "Line A (Yusodus 1c June Moon, Bouncer), PredaRikka copy counts"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Rikka Moonlit Waters"]
	steps: [
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Mudan the Rikka Fairy", "Rikka Black Princess"], note: "no Tribute: add Mudan, send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Black Princess"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"], note: "Tribute herself"},
		{card: "Rikka Petal", action: "effect", effect: "take", lock: "plant", fromDeck: ["Primrose the Rikka Fairy Duo"], note: "add Primrose"},
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Petal"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"], note: "CL1"},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Hellebore the Rikka Fairy", fromDeck: ["Hellebore the Rikka Fairy"], lock: "plant", note: "CL2"},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Hellebore the Rikka Fairy": 6}},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Hellebore the Rikka Fairy"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Black Princess"], attach: ["Rikka Black Princess#2"], note: "attach BLACK PRINCESS (not Rikka Princess)"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Sacred Queen Strenna"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Glamour: attach Moonlit Waters (Spell)"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special", note: "keep Rikka Princess in hand"},
	]
	end: mmz: ["Sacred Tree Beast, Hyperyton", "Hellebore the Rikka Fairy", "Primrose the Rikka Fairy Duo", "Cactus Bouncer"]
}

// Instant Fusion alone: the proven Predaprimitive line, entered from Instant Fusion.
lines: "1st: Instant Fusion alone (Predaprimitive line, Cactus)": {
	source: "Yusodus, MDM 'Predarikka: 1c Primitive/Instant (Bouncer)', Instant Fusion start"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Instant Fusion"]
	steps: [
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare Predap card"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila", "Predaplant Lilizard"]},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into a zone Jasmine will point to"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Aromaseraphy Jasmine"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Kanzashi the Rikka Queen", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Petal"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Kanzashi the Rikka Queen", action: "effect", effect: "revive", summons: "Predaplant Bal Teah"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Rikka Queen Strenna", action: "xyz", zone: "extra", consumes: ["Rikka Princess", "Predaplant Bal Teah"]},
		{card: "Rikka Queen Strenna", action: "effect", effect: "add", detach: 1, note: "detach Rikka Princess, add Primrose from the GY"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
	]
	end: mmz: ["Cactus Bouncer", "Kanzashi the Rikka Queen", "Rikka Queen Strenna", "Rikka Sacred Queen Strenna"]
}

// Predap half into Jasmine, then Jasmine brings Black Princess and the Rikka tail runs.
// Shared by Dracaena alone and Longinephila alone (both spend the Normal Summon on Longinephila).
_jasmineToTail: [
	{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"], note: "Extra Monster Zone; arrows down-left and down-right"},
]

lines: "1st: Dracaena alone": {
	source: "Claude, 25 Nov 2026, from card text (Predap half of the proven line + Line 1)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Princess Dracaena, the Thirsting Tree"]
	steps: list.Concat([[
		{card: "Princess Dracaena, the Thirsting Tree", action: "special_summon", zone: "hand", effect: "summon_self", sendsToGY: true, lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp"], note: "send Byblisp"},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Lilizard", "Instant Fusion"], note: "send LILIZARD, add Instant Fusion"},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", note: "add Lilizard from the GY"},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self", note: "you control Longinephila"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"], note: "no search (Longinephila's is used)"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Extra Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
	], _jasmineToTail, [
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Longinephila"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], note: "Longinephila must be under an arrow"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Princess Dracaena, the Thirsting Tree"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	], _rikkaTail])
	end: {
		mmz: _tailEnd
		emz: ["Aromaseraphy Jasmine"]
	}
}

lines: "1st: Longinephila alone": {
	source: "Claude, 25 Nov 2026, from card text (proven Predaprimitive line + Line 1)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaplant Longinephila"]
	steps: list.Concat([[
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"], note: "no search (used)"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Extra Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter on Bal Teah"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into a zone Jasmine will point to"},
	], _jasmineToTail, [
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Predaplant Longinephila"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	], _rikkaTail])
	end: {
		mmz: _tailEnd
		emz: ["Aromaseraphy Jasmine"]
	}
}

// Predaprimitive + Moonlit Waters (or Glamour: then Konkon sets Moonlit instead).
// Predap half first (Instant Fusion, Bal Teah, Jasmine come before Moonlit's Plant Xyz lock).
_primitiveHalf: [
	{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
	{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
	{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
	{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaplant Longinephila"], note: "spare"},
	{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
	{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"]},
	{card: "Predaplant Longinephila#2", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare"},
	{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Extra Monster Zone"},
	{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
	{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
	{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter on Bal Teah"},
	{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into a zone Jasmine will point to"},
	{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
	{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
	{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
	{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
	{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "Tribute Petal (keeps zones free)"},
	{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
	{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
]
_primitiveRikka: [
	{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Black Princess"], attach: ["Rikka Black Princess#2"], note: "attach BLACK PRINCESS: Glamour needs Rikka Princess"},
	{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
	{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "CL1"},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"], note: "CL2"},
	{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#3", fromDeck: ["Rikka Black Princess"], lock: "plant", note: "CL3"},
	{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#3": 8}, note: "do NOT attach with Hyperyton yet"},
	{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#3", "Hellebore the Rikka Fairy"]},
]
_primitiveFinish: [
	{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Glamour: attach Moonlit Waters (Spell material)"},
	{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special", note: "keep Rikka Princess in hand"},
]
_primitiveEnd: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Primrose the Rikka Fairy Duo", "Cactus Bouncer"]

lines: "1st: Predaprimitive + Moonlit Waters": {
	source: "Claude, 25 Nov 2026 (proven Predaprimitive line + Line 1 + Line A)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters"]
	steps: list.Concat([_primitiveHalf, [
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "AFTER Jasmine. No Tribute: add Primrose, send Hellebore"},
	], _primitiveRikka, [{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Aromaseraphy Jasmine"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Tribute Jasmine: add Rikka Princess + Cactus"}], _primitiveFinish])
	end: {mmz: _primitiveEnd}
}

lines: "1st: Predaprimitive + Glamour": {
	source: "Claude, 25 Nov 2026 (proven Predaprimitive line + Line 1 + Line A)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Glamour"]
	steps: list.Concat([_primitiveHalf, [
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
	], _primitiveRikka, [{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", consumes: ["Aromaseraphy Jasmine"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Tribute Jasmine: add Rikka Princess + Cactus"}], _primitiveFinish])
	end: {mmz: _primitiveEnd}
}

// Instant Fusion + Moonlit Waters / Glamour: same as the Predaprimitive versions, entered from Instant Fusion.
_ifHalf: [
	{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
	{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
	{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
	{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
	{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
	{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila", fromDeck: ["Predaplant Longinephila"]},
	{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare"},
	{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila", "Predaplant Lilizard"], note: "Extra Monster Zone"},
	{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
	{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
	{card: "Predaplant Longinephila", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter on Bal Teah"},
	{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into a zone Jasmine will point to"},
	{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
	{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
	{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
	{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
	{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "Tribute Petal (keeps zones free)"},
	{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
	{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
]

lines: "1st: Instant Fusion + Moonlit Waters": {
	source: "Claude, 25 Nov 2026 (proven Predaprimitive line + Line 1 + Line A)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Instant Fusion", "Rikka Moonlit Waters"]
	steps: list.Concat([_ifHalf, [
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "AFTER Jasmine. No Tribute: add Primrose, send Hellebore"},
	], _primitiveRikka, [{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Aromaseraphy Jasmine"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Tribute Jasmine: add Rikka Princess + Cactus"}], _primitiveFinish])
	end: {mmz: _primitiveEnd}
}

lines: "1st: Instant Fusion + Glamour": {
	source: "Claude, 25 Nov 2026 (proven Predaprimitive line + Line 1 + Line A)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Instant Fusion", "Rikka Glamour"]
	steps: list.Concat([_ifHalf, [
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
	], _primitiveRikka, [{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", consumes: ["Aromaseraphy Jasmine"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Tribute Jasmine: add Rikka Princess + Cactus"}], _primitiveFinish])
	end: {mmz: _primitiveEnd}
}

// Dracaena / Longinephila + a Rikka Spell in hand. Same as the 1-card line, but Rikka Queen Strenna gets
// Black Princess, and Glamour Tributes Jasmine for Rikka Princess + Cactus (Cactus stays in hand: the
// Normal Summon went on Longinephila). Hyperyton attaches the Spell instead of Mudan.
_dracPrefix: list.Concat([[
		{card: "Princess Dracaena, the Thirsting Tree", action: "special_summon", zone: "hand", effect: "summon_self", sendsToGY: true, lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp"], note: "send Byblisp"},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Lilizard", "Instant Fusion"], note: "send LILIZARD, add Instant Fusion"},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", note: "add Lilizard from the GY"},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self", note: "you control Longinephila"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"], note: "no search (Longinephila's is used)"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Extra Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
	], _jasmineToTail, [
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Longinephila"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], note: "Longinephila must be under an arrow"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Princess Dracaena, the Thirsting Tree"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	]])
_longiPrefix: list.Concat([[
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"], note: "no search (used)"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Extra Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter on Bal Teah"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into a zone Jasmine will point to"},
	], _jasmineToTail, [
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Predaplant Longinephila"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	]])
_rikkaTailG: {
	moonlitZone: string
	glamourZone: string
	konkonSets: string
	steps: [
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: [konkonSets]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Black Princess"], attach: ["Rikka Black Princess#3"], note: "attach BLACK PRINCESS: Glamour needs Rikka Princess"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: moonlitZone, effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "CL1"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"], note: "CL2"},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"], lock: "plant", note: "CL3"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#2": 8}, note: "do NOT attach with Hyperyton yet"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#2", "Hellebore the Rikka Fairy"]},
		{card: "Rikka Glamour", action: "activate", zone: glamourZone, effect: "activate", consumes: ["Aromaseraphy Jasmine"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Tribute Jasmine: add Rikka Princess + Cactus (both stay in hand)"},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Glamour: attach Moonlit Waters (Spell material)"},
	]
}
for st, pre in {"Dracaena": _dracPrefix, "Longinephila": _longiPrefix} {
	for sp, t in {
		"Moonlit Waters": {moonlitZone: "hand", glamourZone: "field", konkonSets: "Rikka Glamour", card: "Rikka Moonlit Waters"}
		"Glamour": {moonlitZone: "field", glamourZone: "hand", konkonSets: "Rikka Moonlit Waters", card: "Rikka Glamour"}
	} {
		let tail = (_rikkaTailG & {moonlitZone: t.moonlitZone, glamourZone: t.glamourZone, konkonSets: t.konkonSets}).steps
		lines: "1st: \(st) + \(sp)": {
			source: "Claude, 25 Nov 2026 (\(st) alone + Line A's Glamour finish)"
			status: "untested"
			deck:   "PredaRikka"
			hand: [[if st == "Dracaena" {"Princess Dracaena, the Thirsting Tree"}, "Predaplant Longinephila"][0], t.card]
			steps: list.Concat([pre, tail])
			end: mmz: _tailEnd
		}
	}
}
