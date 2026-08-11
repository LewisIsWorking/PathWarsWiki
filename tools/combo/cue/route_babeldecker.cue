// 2026-08-10: Route 5, the Babeldecker turn 2 kill. Takes the plain two-material line rather than
// Babeldecker's own "rank 10 using only itself" effect, because that needs the opponent to have
// activated something, which the model does not check.
// Must stay identical in content to pkl/RouteBabeldecker.pkl.
package crystron

routeBabeldecker: #Route & {
	name:  "Babeldecker into Juggernaut Liebe"
	build: "amelia"
	opening: ["Heavy Armored Knight Babeldecker", "Heavy Freight Train Derricrane"]
	steps: [
		{n: 1, card: "Heavy Armored Knight Babeldecker", action: "normal-summon", from: "hand", to: "field",
			text: "Normal summon WITHOUT tributing, despite being level 10."},

		{n: 2, card: "Heavy Freight Train Derricrane", action: "special-summon", from: "hand", to: "field",
			oncePerTurn: "Heavy Armored Knight Babeldecker:summon",
			text:        "Babeldecker on summon: special summon 1 EARTH machine from HAND. Derricrane's ATK/DEF halve."},

		{n: 3, card: "Superdreadnought Rail Cannon Gustav Max", action: "xyz", from: "extra", to: "field",
			result: "Superdreadnought Rail Cannon Gustav Max",
			materials: ["Heavy Armored Knight Babeldecker", "Heavy Freight Train Derricrane"],
			text: "Two level 10s. Detach Derricrane for the 2000 burn and it ALSO destroys a card."},

		{n: 4, card: "Superdreadnought Rail Cannon Juggernaut Liebe", action: "xyz", from: "extra", to: "field",
			result:        "Superdreadnought Rail Cannon Juggernaut Liebe",
			usesAltSummon: true,
			materials: ["Superdreadnought Rail Cannon Gustav Max"],
			text: "Alternate summon: use 1 rank 10 Machine Xyz you control, transferring its materials. Take the Gustav Max burn BEFORE this."},
	]
}
