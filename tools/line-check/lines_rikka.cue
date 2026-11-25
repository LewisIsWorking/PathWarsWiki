// Pure Rikka lines (deck RikkaM1). Same steps as the Rikka wiki page.
package lines

lines: "Line A: Moonlit Waters alone (Hyperyton + Cactus)": {
	source: "Yusodus, MDM 'Pure Rikka: 1c June Moon' (Bouncer branch)"
	status: "proven"
	deck:   "RikkaM1"
	hand: ["Rikka Moonlit Waters"]
	steps: [
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Mudan the Rikka Fairy", "Rikka Black Princess"], note: "no Tribute: add Mudan, send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Black Princess"], summons: "Rikka Petal", fromDeck: ["Rikka Petal"], note: "Tribute herself"},
		{card: "Rikka Petal", action: "effect", effect: "take", lock: "plant", fromDeck: ["Primrose the Rikka Fairy Duo"], note: "add Primrose"},
		{card: "Mudan the Rikka Fairy", action: "special_summon", zone: "hand", effect: "summon_self", consumes: ["Rikka Petal"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Hellebore the Rikka Fairy", fromDeck: ["Hellebore the Rikka Fairy"], lock: "plant"},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Hellebore the Rikka Fairy": 6}, note: "Hellebore -2 (to 6)"},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Hellebore the Rikka Fairy"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"], note: "attach Rikka Princess"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Sacred Queen Strenna"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "attach Moonlit Waters (Spell material)"},
		{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
		{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
	]
	end: mmz: ["Sacred Tree Beast, Hyperyton", "Hellebore the Rikka Fairy", "Primrose the Rikka Fairy Duo", "Rikka Princess", "Cactus Bouncer"]
}

_lineBSteps: [
	{card: "Rikka Black Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
	{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", fromHand: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
	{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
	{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
	{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Glamour"]},
	{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"]},
	{card: "Rikka Glamour", action: "activate", zone: "field", effect: "activate", consumes: ["Rikka Queen Strenna"], fromDeck: ["Rikka Princess", "Cactus Bouncer"]},
	{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
	{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
	{card: "Rikka Princess", action: "special_summon", zone: "hand", effect: "summon_self", lock: "plant"},
	{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "attach Mudan from the GY"},
	{card: "Cactus Bouncer", action: "normal_summon", zone: "hand", lock: "no_special"},
]


lines: "Line B: Black Princess + any Plant (Hyperyton + Cactus)": {
	source: "Yusodus, MDM 'Pure Rikka: 1.5c Black Princess (Bouncer)'"
	status: "proven"
	deck:   "RikkaM1"
	hand: ["Rikka Black Princess", "Rikka Petal"]
	steps: _lineBSteps
	end: mmz: ["Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Rikka Princess", "Cactus Bouncer"]
}

// 25 Nov 2026, Rhino game 2: Line B in PredaRikka. Sacred Queen Strenna attaches Rikka Princess,
// then Glamour adds Rikka Princess, but PredaRikka runs only 1. Attach Petal or Black Princess instead.
lines: "KNOWN BAD: Line B in PredaRikka (one Rikka Princess)": {
	source: "Claude, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Rikka Black Princess", "Rikka Petal"]
	steps: _lineBSteps
	end: mmz: ["Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Rikka Princess", "Cactus Bouncer"]
}

lines: "Line 1: Rikka Petal alone (Teardrop + Hyperyton)": {
	source: "Yusodus, MDM 'Pure Rikka: 1c Petal/Glamour'; won turn 3 (solo, 21 Nov 2026)"
	status: "proven"
	deck:   "RikkaM1"
	hand: ["Rikka Petal"]
	steps: [
		{card: "Rikka Petal", action: "normal_summon", zone: "hand"},
		{card: "Rikka Petal", action: "effect", effect: "take", sendsToGY: true, lock: "plant", fromDeck: ["Rikka Black Princess"], note: "send Black Princess"},
		{card: "Rikka Black Princess", action: "special_summon", zone: "gy", effect: "summon_self", lock: "plant"},
		{card: "Rikka Black Princess", action: "effect", effect: "tribute_summon", consumes: ["Rikka Petal"], summons: "Mudan the Rikka Fairy", fromDeck: ["Mudan the Rikka Fairy"]},
		{card: "Mudan the Rikka Fairy", action: "effect", effect: "search", fromDeck: ["Rikka Konkon"]},
		{card: "Rikka Konkon", action: "activate", zone: "hand", effect: "activate"},
		{card: "Rikka Konkon", action: "effect", effect: "set", lock: "plant", fromDeck: ["Rikka Moonlit Waters"]},
		{card: "Rikka Sacred Queen Strenna", action: "xyz", zone: "extra", consumes: ["Mudan the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "summon_xyz", detach: 2, summons: "Rikka Queen Strenna", fromDeck: ["Rikka Princess"], attach: ["Rikka Princess"]},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "field", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Rikka Queen Strenna"]},
		{card: "Rikka Queen Strenna", action: "effect", zone: "gy", effect: "tributed", summons: "Sacred Tree Beast, Hyperyton"},
		{card: "Rikka Sacred Queen Strenna", action: "effect", effect: "set_trap", fromDeck: ["Rikka Sheet"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess#2", fromDeck: ["Rikka Black Princess"], lock: "plant"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess#2": 8}},
		{card: "Sacred Tree Beast, Hyperyton", action: "effect", effect: "attach", note: "attach Mudan from the GY"},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Rikka Black Princess#2", "Hellebore the Rikka Fairy"]},
	]
	end: mmz: ["Teardrop the Rikka Queen", "Sacred Tree Beast, Hyperyton", "Rikka Sacred Queen Strenna", "Primrose the Rikka Fairy Duo"]
}
