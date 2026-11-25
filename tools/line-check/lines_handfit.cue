// Lines fitted to exact hands from real games. All UNTESTED until played as written.
package lines

// 25 Nov 2026, Rhino game 3 opening hand (going first version). The proven Predaprimitive line,
// with two upgrades: Black Princess Tributes the spare Longinephila from the hand (Jasmine stays),
// and Moonlit Waters Tributes Rikka Queen Strenna for Hyperyton before Cactus.
lines: "Line C: Predaprimitive + Konkon + Longinephila hand": {
	source: "Claude, 25 Nov 2026 (from the proven Predaprimitive line)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaplant Longinephila", "Princess Dracaena, the Thirsting Tree", "Predaprimitive", "Predaprimitive#2", "Rikka Konkon"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Princess Dracaena, the Thirsting Tree"], note: "Longinephila is already in hand; take a spare"},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"]},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into the zone Jasmine will point to"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", fromHand: ["Predaplant Longinephila"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"], note: "UPGRADE: Tribute Longinephila from hand, keep Jasmine"},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Glamour"], note: "Konkon is already in hand"},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", summons: "Kanzashi the Rikka Queen", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", consumes: ["Rikka Petal"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Kanzashi the Rikka Queen", action: "effect", effect: "revive", summons: "Predaplant Bal Teah"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Rikka Queen Strenna", action: "xyz", zone: "extra", consumes: ["Rikka Princess", "Predaplant Bal Teah"]},
		{card: "Rikka Queen Strenna", action: "effect", effect: "add", note: "detach Rikka Princess, add Primrose from the GY"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Queen Strenna"], lock: "extra_plant_xyz", fromDeck: ["Rikka Black Princess", "Mudan the Rikka Fairy"], note: "UPGRADE: add Black Princess, send Mudan; decline Primrose's trigger"},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
	]
	end: {
		mmz: ["Cactus Bouncer", "Kanzashi the Rikka Queen", "Rikka Sacred Queen Strenna", "Sacred Tree Beast, Hyperyton"]
		emz: ["Aromaseraphy Jasmine"]
	}
}

// 24 Nov 2026, going second into Horus (4 Sons, King's Sarcophagus, Walls of the Imperial Tomb).
// The corrected order. Teardrop the Rikka Sacred Queen detaches 2 to send BOTH Sarcophagi.
lines: "Horus break: Petal + Mudan + Black Princess hand": {
	source: "Claude, 24 Nov 2026 (corrected); Lewis won turn 3 with a version of it"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Rikka Petal", "Predaplant Longinephila", "Mudan the Rikka Fairy", "Rikka Black Princess", "Dominus Impulse"]
	steps: [
		{card: "Rikka Petal", action: "normal_summon", zone: "hand"},
		{card: "Rikka Petal", action: "effect", effect: "take", lock: "plant", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Petal"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Hellebore the Rikka Fairy", fromDeck: ["Hellebore the Rikka Fairy"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", summons: "Kanzashi the Rikka Queen"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", note: "detach 2: send King's Sarcophagus + Walls, then Tribute Imsety"},
	]
	end: mmz: ["Rikka Sacred Queen Strenna", "Kanzashi the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
}

// 25 Nov 2026, Rhino game 1, going first: Rikka Princess already summoned; hand Mudan, Rikka Sheet, Ash x2.
lines: "Rikka Princess on field + Mudan + Sheet": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Mudan the Rikka Fairy", "Rikka Sheet", "Ash Blossom & Joyous Spring", "Ash Blossom & Joyous Spring#2"]
	startField: ["Rikka Princess"]
	steps: [
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Princess"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Mudan the Rikka Fairy"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], lock: "plant"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess", "Hellebore the Rikka Fairy"]},
		{card: "Rikka Sheet", action: "set", zone: "hand"},
	]
	end: mmz: ["Teardrop the Rikka Queen", "Primrose the Rikka Fairy Duo"]
}
