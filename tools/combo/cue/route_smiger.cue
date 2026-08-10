// 2026-08-10: Route 4, the Crystron Smiger disruption plan. Ends on a SMALL board with a tuner
// still in hand, which is correct for this deck rather than a failed turn. No Xyz: Smiger locks
// Machine SYNCHRO. AMELIA BUILD, because it runs two Crystron tuners so one can be held back.
// Must stay identical in content to pkl/RouteSmiger.pkl.
package crystron

routeSmiger: #Route & {
	name:  "Crystron Smiger, the disruption plan"
	build: "amelia"
	opening: ["Crystron Inclusion", "Crystron Smiger", "Crystron Tristaros"]
	steps: [
		{n: 1, card: "Crystron Inclusion", action: "activate", from: "hand", to: "field",
			oncePerTurn: "Crystron Inclusion:activate",
			text:        "Activate Inclusion, add 1 Crystron card from deck."},

		{n: 2, card: "Crystron Cluster", action: "search", from: "deck", to: "hand",
			text: "Take the continuous trap rather than a monster; the monsters are already here."},

		{n: 3, card: "Crystron Smiger", action: "normal-summon", from: "hand", to: "field",
			text: "Normal summon Smiger."},

		{n: 4, card: "Crystron Inclusion", action: "destroy", from: "field", to: "gy",
			text: "Smiger destroys your own Inclusion, which turns on its GY revive later."},

		{n: 5, card: "Crystron Citree", action: "special-summon", from: "deck", to: "field",
			appliesLock: "machine-synchro",
			oncePerTurn: "Crystron Smiger:summon",
			text:        "Smiger summons a Crystron TUNER from deck. Locks Machine SYNCHRO: no Xyz, no Link."},

		{n: 6, card: "Crystron Cluster", action: "activate", from: "hand", to: "field",
			text: "SET Crystron Cluster. Live from the opponent's turn onward."},
	]
}
