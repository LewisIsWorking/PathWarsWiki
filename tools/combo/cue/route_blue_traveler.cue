// 2026-08-10: Route 2, the Night Train Blue Traveler line, going-first branch.
// AMELIA BUILD ONLY: it needs Revolving Switchyard's summon effect, which requires a Level 4
// EARTH Machine with 1800+ ATK in the deck. Yukinon has none, so this route cannot exist there.
// Must stay identical in content to pkl/RouteBlueTraveler.pkl.
package crystron

routeBlueTraveler: #Route & {
	name:  "Night Train Blue Traveler into a rank 10"
	build: "amelia"
	opening: ["Night Train Blue Traveler", "Scrap Recycler"]
	steps: [
		{n: 1, card: "Night Train Blue Traveler", action: "activate", from: "hand", to: "gy",
			oncePerTurn: "Night Train Blue Traveler:search",
			text:        "Discard it to add Revolving Switchyard from deck."},

		{n: 2, card: "Revolving Switchyard", action: "search", from: "deck", to: "hand",
			text: "Added by Blue Traveler."},

		{n: 3, card: "Revolving Switchyard", action: "activate", from: "hand", to: "field",
			text: "Activate the field spell. Its own effect is NOT spent yet."},

		{n: 4, card: "Scrap Recycler", action: "normal-summon", from: "hand", to: "field",
			text: "Normal summon Recycler to get a second EARTH machine into the GY."},

		{n: 5, card: "Heavy Freight Train Derricrane", action: "mill", from: "deck", to: "gy",
			text: "Recycler on summon sends 1 Machine from deck to the GY."},

		{n: 6, card: "Night Train Blue Traveler", action: "special-summon", from: "gy", to: "field",
			appliesLock: "machine",
			oncePerDuel: "Night Train Blue Traveler:revive",
			text:        "Blue Traveler's GY effect. ONCE PER DUEL. Locks Machine, so Xyz stays legal."},

		{n: 7, card: "Heavy Freight Train Derricrane", action: "special-summon", from: "gy", to: "field",
			text: "The other half of that revive: it summons BOTH."},

		{n: 8, card: "Flying Pegasus Railroad Stampede", action: "special-summon", from: "deck", to: "field",
			becomesLevel: 10,
			oncePerTurn:  "Revolving Switchyard:effect",
			text:         "Switchyard effect B, off a level 10 being summoned. It BECOMES level 10. Costs you all battle damage this turn."},

		{n: 9, card: "Superdreadnought Rail Cannon Gustav Rocket", action: "xyz", from: "extra", to: "field",
			result: "Superdreadnought Rail Cannon Gustav Rocket",
			materials: ["Night Train Blue Traveler", "Heavy Freight Train Derricrane", "Flying Pegasus Railroad Stampede"],
			text: "Three level 10s. Flying Pegasus only counts because step 8 changed its Level."},
	]
}
