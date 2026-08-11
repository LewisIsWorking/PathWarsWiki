// 2026-08-10: Route 1, the Crystron Inclusion one-card line. Must stay identical in content to
// pkl/routes/RouteInclusion.pkl; check-combos.ps1 diffs the two models' findings and fails if
// they disagree, which is what stops the two copies drifting apart.
package crystron

routeInclusion: #Route & {
	name:  "Crystron Inclusion, one card"
	build: "amelia"
	opening: ["Crystron Inclusion"]
	steps: [
		{n: 1, card: "Crystron Inclusion", action: "activate", from: "hand", to: "field",
			oncePerTurn: "Crystron Inclusion:activate",
			text:        "Activate Inclusion. On activation, add 1 Crystron card from deck."},

		{n: 2, card: "Crystron Sulfador", action: "search", from: "deck", to: "hand",
			text: "Added by Inclusion."},

		{n: 3, card: "Crystron Inclusion", action: "destroy", from: "field", to: "gy",
			text: "Sulfador targets Inclusion, the Crystron card you control, and destroys it."},

		{n: 4, card: "Crystron Sulfador", action: "special-summon", from: "hand", to: "field",
			appliesLock: "machine",
			oncePerTurn: "Crystron Sulfador:summon",
			text:        "Sulfador summons itself. Locks Machine, so Xyz stays legal."},

		{n: 5, card: "Crystron Tristaros", action: "mill", from: "deck", to: "gy",
			text: "Sulfador on summon sends 2 differently named Crystron cards to the GY."},

		{n: 6, card: "Crystron Sulfefnir", action: "mill", from: "deck", to: "gy",
			text: "The second of the two."},

		{n: 7, card: "Crystron Inclusion", action: "banish", from: "gy", to: "banished",
			oncePerTurn: "Crystron Inclusion:revive",
			text:        "Banish Inclusion from the GY to pay for its revive."},

		{n: 8, card: "Crystron Tristaros", action: "special-summon", from: "gy", to: "field",
			text: "Inclusion revives Tristaros."},

		{n: 9, card: "Crystron Eleskeletus", action: "synchro", from: "extra", to: "field",
			result: "Crystron Eleskeletus",
			materials: ["Crystron Sulfador", "Crystron Tristaros"],
			text: "5 + 2 = 7. On summon, add a Crystron card from GY or banishment."},
	]
}
