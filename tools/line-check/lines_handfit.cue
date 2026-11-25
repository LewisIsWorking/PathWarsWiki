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
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Kanzashi the Rikka Queen", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", consumes: ["Rikka Petal"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Kanzashi the Rikka Queen", action: "effect", effect: "revive", summons: "Predaplant Bal Teah"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Rikka Queen Strenna", action: "xyz", zone: "extra", consumes: ["Rikka Princess", "Predaplant Bal Teah"]},
		{card: "Rikka Queen Strenna", action: "effect", effect: "add", detach: 1, note: "detach Rikka Princess, add Primrose from the GY"},
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
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Kanzashi the Rikka Queen"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", consumes: ["opp:Imsety, Glory of Horus"], note: "detach 2: send King's Sarcophagus + Walls, then Tribute Imsety"},
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

// 25 Nov 2026, ranked vs bilotahn (Machina), going 2nd into Machina Fortress (2500), 3 cards in hand.
// Rikka page Sample Hand 4. Fortress punishes targeting and battle, so Glamour Tributes it through Konkon.
lines: "Machina: Hand 4 lethal (Dracaena, Lilizard, Glamour x2, Predaprimitive x2)": {
	source: "Rikka page Sample Hand 4, 25 Nov 2026 (Ash and Ghost Belle stopped it live)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Princess Dracaena, the Thirsting Tree", "Predaplant Lilizard", "Rikka Glamour", "Rikka Glamour#2", "Predaprimitive", "Predaprimitive#2"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Princess Dracaena, the Thirsting Tree", action: "special_summon", zone: "hand", effect: "summon_self", fromDeck: ["Rikka Princess"], note: "send Rikka Princess"},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaprimitive"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila", "Predaplant Lilizard"]},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard", note: "Ghost Belle negated this live"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila", action: "effect", zone: "gy", effect: "gy", note: "Predator Counter on Fortress (no target on Fortress's own text: it isn't targeted)"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive"},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Princess Dracaena, the Thirsting Tree"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Glamour", action: "activate", zone: "hand", effect: "activate", consumes: ["opp:Machina Fortress"], fromDeck: ["Rikka Black Princess", "Mudan the Rikka Fairy"], note: "Konkon: Tribute Fortress instead of a Plant"},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Petal"], attach: ["Rikka Petal"], note: "ATTACH Petal, or Strenna has no material and no Hyperyton"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Queen Strenna"], lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "Primrose to hand, Hellebore to GY"},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "Attack Position"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Black Princess#2", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Black Princess#2"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#3", fromDeck: ["Rikka Black Princess"]},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#3": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#3", "Hellebore the Rikka Fairy"]},
	]
	end: {
		mmz: ["Rikka Sacred Queen Strenna", "Sacred Tree Beast, Hyperyton", "Primrose the Rikka Fairy Duo", "Teardrop the Rikka Queen"]
		emz: ["Aromaseraphy Jasmine"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Aromaseraphy Jasmine"]}
}

// What went wrong live vs Machina: Sacred Queen Strenna's detach summoned Rikka Queen Strenna without
// attaching a Rikka monster (the attach is optional), so her float had no material: no Hyperyton.
lines: "KNOWN BAD: Machina, Rikka Queen Strenna Tributed with no material": {
	source: "Rikka page game log, 25 Nov 2026 (most likely cause of the missing Hyperyton)"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: []
	startField: ["Rikka Sacred Queen Strenna"]
	steps: [
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", note: "no attach"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", consumes: ["Rikka Queen Strenna"], lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "set by Konkon"},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
	]
	end: mmz: ["Rikka Sacred Queen Strenna", "Sacred Tree Beast, Hyperyton"]
}

// The counting mistake behind several live lines: Hellebore's revive (and Primrose's, Jasmine's and
// Sacred Queen Strenna's summons) are in Defence, so they can't attack. Same board as the Machina fix.
lines: "KNOWN BAD: lethal counted with Defence-position Hellebore and Primrose": {
	source: "Coaching mistakes to avoid, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Rikka Black Princess", "Primrose the Rikka Fairy Duo"]
	startField: ["Rikka Sacred Queen Strenna"]
	steps: [
		{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Black Princess"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"]},
	]
	end: mmz: ["Rikka Sacred Queen Strenna", "Hellebore the Rikka Fairy", "Primrose the Rikka Fairy Duo", "Rikka Black Princess#2"]
	lethal: {lp: 7000, attackers: ["Rikka Sacred Queen Strenna", "Hellebore the Rikka Fairy", "Primrose the Rikka Fairy Duo"]}
}

// 25 Nov 2026, ranked vs trampaslocas (Elfnote), turn 4: their Elfnote Seraphim Strelitzia (a Plant) and
// our Cactus Bouncer are both up, so NEITHER player can Special Summon. Instant Fusion is a Special Summon
// (the trap the turn 4 notes warn about; Super Poly is locked the same way).
lines: "KNOWN BAD: Elfnote turn 4, Instant Fusion under Cactus + Strelitzia": {
	source: "Rikka page Sample Hand 5, turn 4 notes"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Hellebore the Rikka Fairy", "Predaprimitive"]
	startField: ["Cactus Bouncer"]
	startLocks: ["no_special"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Instant Fusion"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides"},
	]
	end: mmz: ["Cactus Bouncer", "Predaplant Ambulomelides"]
}

lines: "Elfnote turn 4: Predaprimitive under Cactus + Strelitzia (Normal Summon only)": {
	source: "Claude, 25 Nov 2026; Lewis played it with Super Poly #2 instead of Instant Fusion"
	status: "proven"
	deck:   "PredaRikka"
	hand: ["Hellebore the Rikka Fairy", "Predaprimitive"]
	startField: ["Cactus Bouncer"]
	startLocks: ["no_special"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand", note: "Attack Position: a face-down Set doesn't trigger the search"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaplant Lilizard"]},
	]
	end: mmz: ["Cactus Bouncer", "Predaplant Longinephila"]
}

// 25 Nov 2026, Elfnote turn 8. LP 5400 vs 8000. Their field: Elfnote Lucina + S:P Little Knight (EMZ).
// Hand: Lilizard, Moonlit Waters; Hellebore in the GY; field empty.
lines: "Elfnote turn 8 lethal: Moonlit Waters + Lilizard, Hellebore in GY": {
	source: "Rikka page Sample Hand 5, turn 8 (Little Knight + Rikka Princess stopped it live)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaplant Lilizard", "Rikka Moonlit Waters"]
	steps: [
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Mudan the Rikka Fairy", "Rikka Black Princess"], note: "add Mudan, send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Black Princess"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
		{card: "Rikka Petal", action: "effect", effect: "take", lock: "plant", fromDeck: ["Primrose the Rikka Fairy Duo"]},
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Petal"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess#2"], note: "Attack Position"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Mudan the Rikka Fairy"], attach: ["Mudan the Rikka Fairy"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["opp:Elfnote Lucina"], fromDeck: ["Rikka Princess", "Cactus Bouncer"], note: "Konkon Tributes Lucina; the Level 4 Plant can be any one left"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton", note: "Attack Position"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Teardrop the Rikka Queen", action: "effect", effect: "tribute", detach: 1, consumes: ["opp:S:P Little Knight"]},
		{card: "Predaplant Lilizard", action: "normal_summon", zone: "hand"},
	]
	end: mmz: ["Rikka Sacred Queen Strenna", "Sacred Tree Beast, Hyperyton", "Teardrop the Rikka Queen", "Predaplant Lilizard"]
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Predaplant Lilizard"], bonus: {"Teardrop: Little Knight Tributed": 200}}
}

// What happened live: Little Knight went for Mudan; Rikka Princess negated it by Tributing PRIMROSE,
// which the Teardrop Xyz still needed. Rule: Tribute a Plant the rest of the line doesn't need.
lines: "KNOWN BAD: Elfnote turn 8, Rikka Princess Tributes Primrose": {
	source: "Rikka page game log, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Rikka Princess", "Predaplant Lilizard"]
	startField: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]
	steps: [
		{card: "Rikka Princess", action: "effect", zone: "hand", effect: "negate", consumes: ["Primrose the Rikka Fairy Duo"], note: "negate Little Knight"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
	]
	end: mmz: ["Teardrop the Rikka Queen"]
}

// 25 Nov 2026 (~12:00), ranked, going 1st vs unknown deck (they surrendered turn 1).
// Hand: Mudan, Instant Fusion, Triple Tactics Talent, Predaprimitive, Moonlit Waters.
// The full line we should have sent on the first screenshot. Predap Extra Deck summons
// (Fusion, Synchro, Link) all happen BEFORE Moonlit Waters (its lock: Plant Xyz only).
lines: "Hand 6: Mudan + Instant Fusion + Predaprimitive + Moonlit Waters + TTT": {
	source: "Claude, 25 Nov 2026 (from the proven Predaprimitive line + Line 1)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Mudan the Rikka Fairy", "Instant Fusion", "Triple Tactics Talent", "Predaprimitive", "Rikka Moonlit Waters"]
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Instant Fusion", action: "activate", zone: "hand", effect: "activate", summons: "Predaplant Ambulomelides", note: "pay 1000 LP"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self"},
		{card: "Predaplant Ambulomelides", action: "effect", effect: "tribute", consumes: ["Predaplant Ambulomelides"], summons: "Predaplant Longinephila#2", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila#2", action: "effect", effect: "search", fromDeck: ["Predaprimitive"], note: "spare: Super Poly discard"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila#2", "Predaplant Lilizard"], note: "Main Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila#2", action: "effect", zone: "gy", effect: "gy", note: "banish: Predator Counter on Lilizard"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive", note: "into the zone Jasmine will point to"},
		{card: "Aromaseraphy Jasmine", action: "link", zone: "extra", consumes: ["Predaplant Bal Teah", "Predaplant Lilizard"]},
		{card: "Aromaseraphy Jasmine", action: "effect", effect: "tribute", consumes: ["Predaplant Byblisp"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", fromHand: ["Predaplant Longinephila"], summons: "Mudan the Rikka Fairy#2", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Mudan the Rikka Fairy#2", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Petal"], note: "no search (Mudan's search is used)"},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy#2", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", attach: ["Rikka Black Princess"], fromDeck: ["Rikka Black Princess"], note: "attach Black Princess #3, keep Rikka Princess for Glamour"},
		{card: "Kanzashi the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess#2"]},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Sacred Queen Strenna"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "chain to Glamour: attach Moonlit Waters (a Spell)"},
		{card: "Kanzashi the Rikka Queen", action: "effect", effect: "revive", summons: "Rikka Sacred Queen Strenna", note: "detach 1: Sacred Queen Strenna back from the GY, effects negated"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
	]
	end: {
		mmz: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Kanzashi the Rikka Queen", "Rikka Sacred Queen Strenna", "Cactus Bouncer"]
		emz: ["Aromaseraphy Jasmine"]
	}
}

// The live advice on the first screenshot: "Moonlit Waters: add Black Princess, send Black Princess #2".
// Moonlit takes 2 Rikka monsters from the DECK with the same Level and DIFFERENT names.
// With Mudan #1 in hand, the only other Level 6 was Mudan #2, so Mudan went to the GY.
lines: "KNOWN BAD: Hand 6, Moonlit Waters takes two Black Princess": {
	source: "Live advice, 25 Nov 2026 (~12:00)"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Mudan the Rikka Fairy", "Instant Fusion", "Triple Tactics Talent", "Predaprimitive", "Rikka Moonlit Waters"]
	steps: [
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Rikka Black Princess", "Rikka Black Princess"]},
	]
	end: mmz: []
}
