// PredaRikka lines (deck PredaRikka), plus known-bad plans from real games so the checker proves it catches them.
package lines

lines: "Predaprimitive alone (Cactus lock)": {
	source: "Yusodus, MDM 'Predarikka: 1c Primitive/Instant (Bouncer)'"
	status: "proven"
	deck:   "PredaRikka"
	hand: ["Predaprimitive"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila#2", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "any Predap card"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"]},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Aromaseraphy Jasmine"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", summons: "Kanzashi the Rikka Queen", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Petal"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Kanzashi the Rikka Queen", action: "effect", effect: "revive", summons: "Predaplant Bal Teah"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Rikka Queen Strenna", action: "xyz", zone: "extra", consumes: ["Rikka Princess", "Predaplant Bal Teah"]},
		{card: "Rikka Queen Strenna", action: "effect", effect: "add", note: "detach Rikka Princess, add Primrose from the GY"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
	]
	end: mmz: ["Cactus Bouncer", "Kanzashi the Rikka Queen", "Rikka Queen Strenna", "Rikka Sacred Queen Strenna"]
}

// 24 Nov 2026, going second into Horus. Claude's first plan Xyz'd Black Princess away,
// then used her effect. The checker should flag step 10.
lines: "KNOWN BAD: Horus plan, Black Princess used after Xyz": {
	source: "Claude, 24 Nov 2026 (corrected mid-game)"
	status: "known_bad"
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
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", summons: "Kanzashi the Rikka Queen"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", note: "Konkon Tributes Imsety"},
	]
	end: mmz: ["Kanzashi the Rikka Queen", "Rikka Sacred Queen Strenna", "Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]
}

// 25 Nov 2026, Rhino game 3: going second into Dark Law + Chaos x2. Claude's plan used Predaprimitive
// (blocked: it sends to the GY) and Lilizard's Polymerization search (this deck runs no Polymerization).
lines: "KNOWN BAD: Rhino G3, Predap engine under Dark Law": {
	source: "Claude, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	darkLaw: true
	hand: ["Predaplant Longinephila", "Princess Dracaena, the Thirsting Tree", "Mulcharmy Purulia", "Predaprimitive", "Predaprimitive#2", "Rikka Konkon"]
	steps: [
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate", note: "bait for Chaos"},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self", fromDeck: ["Polymerization"]},
	]
	end: mmz: ["Predaplant Longinephila", "Predaplant Lilizard"]
}

// 25 Nov 2026, ranked vs Sloth (Rikka mirror), going 1st. Searches before Moonlit Waters gave Droll a target;
// Moonlit Waters then couldn't be activated. Lesson: Moonlit Waters first, searches after.
lines: "KNOWN BAD: Sloth, Predaprimitive before Moonlit into Droll": {
	source: "Rikka page game log, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	drollFrom: 3
	hand: ["Princess Dracaena, the Thirsting Tree", "Princess Dracaena, the Thirsting Tree#2", "Triple Tactics Talent", "Predaprimitive", "Rikka Moonlit Waters"]
	steps: [
		{card: "Princess Dracaena, the Thirsting Tree", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant_or_dragon", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"], note: "Droll responds to this add"},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
	]
	end: mmz: ["Princess Dracaena, the Thirsting Tree"]
}
