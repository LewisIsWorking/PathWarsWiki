// Going-second breaks per matchup (25 Nov 2026). All UNTESTED until played.
// Card text checked against ProjectIgnis BabelCDB, 25 Nov 2026. Plans and baits: Speed sheet + Rikka page.
//
// The core (#Core): two removals BEFORE any Rikka lock, then the Rikka half.
//   1. Predaprimitive (Super Poly) -> Byblisp -> Normal Summon Longinephila -> Lilizard -> Bal Teah -> Lilizard back + draw.
//   2. Longinephila (GY) puts a Predator Counter on their monster A (no target: it becomes Level 1).
//      Byblisp revives. Predaplant Daredevil's own summon Tributes A + Byblisp. A summon procedure,
//      not an activation: Infinity, Baronne, Dominus Impulse and Chaos can't negate it.
//   3. Lilizard makes their monster B DARK (skip if B is DARK already). Super Poly: B + Lilizard -> Starving Venom. No responses.
//   4. Moonlit Waters (Primrose, send Hellebore) -> Hellebore Tributes Bal Teah -> Primrose + Black Princess
//      -> Teardrop (Venom + Hellebore), Teardrop #2 (Primrose + Black Princess at Level 8) -> Teardrop the Rikka Sacred Queen.
//   5. Sacred Queen: detach up to 3, send that many Spells/Traps, then Tribute their monster C (if any).
//   Attack: Sacred Queen 3200 + Teardrop 2800 (+200 if C was Tributed) + Daredevil 2200 = 8200 (8400).
// Needs: Predaprimitive + Moonlit Waters + 1 card to discard. The 4th/5th cards are free.
package lines

#Core: {
	A:       string // their monster for Daredevil (Predator Counter + Tribute)
	B:       string // their monster for Starving Venom
	darkenB: bool   // false when B is DARK already (Imsety, Dark Law, Chaos, Unclaspare, Chimeratech Fortress)
	C:       string | *"" // their monster for Sacred Queen's Tribute
	discard: string
	out: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"], note: "sending Byblisp is the cost: if it's negated, Byblisp still searches"},
		{card: "Predaplant Byblisp", action: "effect", zone: "gy", effect: "search", fromDeck: ["Predaplant Longinephila"]},
		{card: "Predaplant Longinephila", action: "normal_summon", zone: "hand"},
		{card: "Predaplant Longinephila", action: "effect", effect: "search", fromDeck: ["Predaplant Lilizard"]},
		{card: "Predaplant Lilizard", action: "special_summon", zone: "hand", effect: "summon_self", note: "skip the Polymerization add (the deck has none)"},
		{card: "Predaplant Bal Teah", action: "synchro", zone: "extra", consumes: ["Predaplant Longinephila", "Predaplant Lilizard"], note: "Main Monster Zone"},
		{card: "Predaplant Bal Teah", action: "effect", effect: "revive", summons: "Predaplant Lilizard"},
		{card: "Predaplant Lilizard", action: "effect", effect: "draw"},
		{card: "Predaplant Longinephila", action: "effect", zone: "gy", effect: "gy", counter: "opp:\(A)", note: "banish it: Predator Counter on \(A) (no target), it becomes Level 1"},
		{card: "Predaplant Byblisp", action: "special_summon", zone: "gy", effect: "revive"},
		{card: "Predaplant Daredevil", action: "special_summon", zone: "extra", consumes: ["opp:\(A)", "Predaplant Byblisp"], note: "Daredevil's own summon: Tribute \(A) (has the counter) + Byblisp. Extra Monster Zone"},
		if darkenB {{card: "Predaplant Lilizard", action: "effect", effect: "dark", makesDark: "opp:\(B)", note: "\(B) becomes DARK"}},
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: [discard], consumes: ["opp:\(B)", "Predaplant Lilizard"], summons: "Starving Venom Fusion Dragon", note: "discard \(discard); nobody can respond"},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute: add Primrose, send Hellebore. Plant Xyz only from here"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Predaplant Bal Teah"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], lock: "plant", note: "Bal Teah was Tributed: Primrose + Black Princess, Defence"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Starving Venom Fusion Dragon", "Hellebore the Rikka Fairy"], note: "Attack Position"},
		{card: "Teardrop the Rikka Queen#2", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Rikka Black Princess"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen#2"], note: "3 materials after the transfer. Attack Position"},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", consumes: [if C != "" {"opp:\(C)"}], note: "detach up to 3: send their Spells/Traps (pick the set ones that hurt), then Tribute \(C)"},
	]
}

lines: "Horus going 2nd: Daredevil on Hapi, Venom on Imsety, Sacred Queen Tributes Duamutef": {
	source: "Claude, 25 Nov 2026 (card text; rules reading on Daredevil's Tribute marked in the Rikka page)"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Imsety, Glory of Horus", "Hapi, Guidance of Horus", "Duamutef, Blessing of Horus"]
	steps: (#Core & {A: "Hapi, Guidance of Horus", B: "Imsety, Glory of Horus", darkenB: false, C: "Duamutef, Blessing of Horus", discard: "Mulcharmy Fuwalos"}).out
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
		emz: ["Predaplant Daredevil"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Teardrop the Rikka Queen", "Predaplant Daredevil"], bonus: {"Teardrop: Duamutef Tributed": 200}}
}

lines: "Machina going 2nd: Daredevil on Fortress, Venom on Air Raider": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Purulia", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Machina Fortress", "Machina Air Raider"]
	steps: (#Core & {A: "Machina Fortress", B: "Machina Air Raider", darkenB: true, discard: "Mulcharmy Purulia"}).out
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
		emz: ["Predaplant Daredevil"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Teardrop the Rikka Queen", "Predaplant Daredevil"]}
}

lines: "Cyber Dragon going 2nd: Daredevil on Infinity, Venom on Chimeratech Fortress (no Clockwork Night)": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Cyber Dragon Infinity", "Chimeratech Fortress Dragon"]
	steps: (#Core & {A: "Cyber Dragon Infinity", B: "Chimeratech Fortress Dragon", darkenB: false, discard: "Mulcharmy Fuwalos"}).out
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
		emz: ["Predaplant Daredevil"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Teardrop the Rikka Queen", "Predaplant Daredevil"]}
}

lines: "Elfnote going 2nd: Daredevil on Baronne, Venom on Lucina": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Baronne de Fleur", "Elfnote Lucina"]
	steps: (#Core & {A: "Baronne de Fleur", B: "Elfnote Lucina", darkenB: true, discard: "Mulcharmy Fuwalos"}).out
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
		emz: ["Predaplant Daredevil"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Teardrop the Rikka Queen", "Predaplant Daredevil"]}
}

// Sky Striker: usually Zero alone in the Extra Monster Zone + 4 sets. Daredevil takes Zero (a summon procedure:
// Zero can still answer the Predator Counter with its own Tribute, which puts Raye + Roze in their Main zones and
// turns their Sky Striker Spells off). No second monster, so Super Poly is SET for their turn: Raye (DARK) +
// your DARK Predaplant -> Starving Venom.
lines: "Sky Striker going 2nd: Daredevil on Zero, Sacred Queen sends 3 sets, Super Poly held": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring", "Dominus Impulse"]
	oppField: ["Sky Striker Ace = Zero"]
	steps: [
		for i, s in (#Core & {A: "Sky Striker Ace = Zero", B: "-", darkenB: false, discard: "-"}).out if i < 11 {s},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Predaplant Lilizard"], note: "Tribute Lilizard, keep Bal Teah (1900) as an attacker"},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], lock: "plant"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Hellebore the Rikka Fairy", "Rikka Black Princess"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", note: "detach 3: send 3 of their set cards (they can chain set Quick-Plays, but they're gone either way)"},
		{card: "Super Polymerization", action: "set", zone: "hand", note: "for their turn: Raye + Bal Teah or Daredevil -> Starving Venom"},
	]
	end: {
		mmz: ["Predaplant Bal Teah", "Teardrop the Rikka Sacred Queen", "Primrose the Rikka Fairy Duo"]
		emz: ["Predaplant Daredevil"]
	}
	// Not lethal from 8000: Sacred Queen 3200 + Daredevil 2200 + Bal Teah 1900 = 7300.
	lethal: {lp: 7300, attackers: ["Teardrop the Rikka Sacred Queen", "Predaplant Daredevil", "Predaplant Bal Teah"]}
}

// HERO (Rhino): Dark Law stops Predaprimitive, so this needs a NATURAL Super Poly. Super Poly first:
// Dark Law + Chaos are both DARK -> Starving Venom, no responses. Then the Predap engine is live.
lines: "HERO going 2nd: natural Super Poly on Dark Law + Chaos, Daredevil on Chaos #2, Sacred Queen Tributes Wingman": {
	source: "Claude, 25 Nov 2026"
	status: "untested"
	deck:   "PredaRikka"
	hand: ["Super Polymerization", "Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Fuwalos", "Ash Blossom & Joyous Spring"]
	oppField: ["Masked HERO Dark Law", "Contrast HERO Chaos", "Contrast HERO Chaos#2", "Elemental HERO Shining Neos Wingman"]
	steps: [
		{card: "Super Polymerization", action: "activate", zone: "hand", effect: "activate", fromHand: ["Mulcharmy Fuwalos"], consumes: ["opp:Masked HERO Dark Law", "opp:Contrast HERO Chaos"], summons: "Starving Venom Fusion Dragon", note: "FIRST, before any search. Discard Fuwalos (Dark Law banishes it)"},
		for i, s in (#Core & {A: "Contrast HERO Chaos#2", B: "-", darkenB: false, discard: "-"}).out if i < 11 {s},
		{card: "Rikka Moonlit Waters", action: "activate", zone: "hand", effect: "activate", lock: "extra_plant_xyz", fromDeck: ["Primrose the Rikka Fairy Duo", "Hellebore the Rikka Fairy"], note: "no Tribute"},
		{card: "Hellebore the Rikka Fairy", action: "special_summon", zone: "gy", effect: "revive", consumes: ["Predaplant Bal Teah"]},
		{card: "Primrose the Rikka Fairy Duo", action: "special_summon", zone: "hand", effect: "tribute_trigger", summons: "Rikka Black Princess", fromDeck: ["Rikka Black Princess"], lock: "plant"},
		{card: "Primrose the Rikka Fairy Duo", action: "effect", effect: "level", setLevel: {"Rikka Black Princess": 8}},
		{card: "Teardrop the Rikka Queen", action: "xyz", zone: "extra", consumes: ["Starving Venom Fusion Dragon", "Hellebore the Rikka Fairy"]},
		{card: "Teardrop the Rikka Queen#2", action: "xyz", zone: "extra", consumes: ["Primrose the Rikka Fairy Duo", "Rikka Black Princess"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "xyz", zone: "extra", rankUp: true, consumes: ["Teardrop the Rikka Queen#2"]},
		{card: "Teardrop the Rikka Sacred Queen", action: "effect", effect: "send_tribute", consumes: ["opp:Elemental HERO Shining Neos Wingman"], note: "detach: send Neos Fusion / sets, then Tribute Wingman (it can't be destroyed, but it can be Tributed)"},
	]
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen", "Predaplant Lilizard"]
		emz: ["Predaplant Daredevil"]
	}
	lethal: {lp: 8000, attackers: ["Teardrop the Rikka Sacred Queen", "Teardrop the Rikka Queen", "Predaplant Daredevil", "Predaplant Lilizard"], bonus: {"Teardrop: Wingman Tributed": 200}}
}

// Checks that the new Fusion-material rules work.
lines: "KNOWN BAD: Starving Venom with a LIGHT monster (Lilizard's DARK skipped)": {
	source: "Checker test, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Predaprimitive", "Rikka Moonlit Waters", "Mulcharmy Purulia"]
	oppField: ["Machina Fortress", "Machina Air Raider"]
	steps: (#Core & {A: "Machina Fortress", B: "Machina Air Raider", darkenB: false, discard: "Mulcharmy Purulia"}).out
	end: {
		mmz: ["Teardrop the Rikka Queen", "Teardrop the Rikka Sacred Queen"]
		emz: ["Predaplant Daredevil"]
	}
}

lines: "KNOWN BAD: Daredevil's Tribute summon with no Predator Counter": {
	source: "Checker test, 25 Nov 2026"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: []
	startField: ["Predaplant Byblisp"]
	oppField: ["Sky Striker Ace = Zero"]
	steps: [
		{card: "Predaplant Daredevil", action: "special_summon", zone: "extra", consumes: ["opp:Sky Striker Ace = Zero", "Predaplant Byblisp"]},
	]
	end: emz: ["Predaplant Daredevil"]
}

// 25 Nov 2026, vs Ryuuku (Horus), turn 5: LP 2500, empty field. Hand: Cactus Bouncer, Mudan, Instant Fusion, Predaprimitive.
// Byblisp, both Longinephila and Lilizard were already out of the Deck, so Predaprimitive had nothing to send.
lines: "KNOWN BAD: Ryuuku turn 5, Predaprimitive with no Predap card left in the Deck": {
	source: "Live game, 25 Nov 2026 (~12:45)"
	status: "known_bad"
	deck:   "PredaRikka"
	hand: ["Cactus Bouncer", "Mudan the Rikka Fairy", "Instant Fusion", "Predaprimitive"]
	deckGone: {"Predaplant Byblisp": 1, "Predaplant Longinephila": 2, "Predaplant Lilizard": 1}
	steps: [
		{card: "Predaprimitive", action: "activate", zone: "hand", effect: "activate", lock: "plant_or_dragon", fromDeck: ["Predaplant Byblisp", "Super Polymerization"]},
	]
	end: mmz: []
}
