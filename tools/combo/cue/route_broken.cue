// 2026-08-10: FIXTURE, not a real line. Must stay identical in content to
// pkl/routes/RouteBroken.pkl - the runner diffs the two models' findings against each other.
package crystron

routeBroken: #Route & {
	name:  "Broken on purpose"
	build: "yukinon"
	opening: ["Crystron Smiger", "Night Train Blue Traveler"]
	steps: [
		// A: Smiger applies the Machine SYNCHRO lock.
		{n: 1, card: "Crystron Smiger", action: "normal-summon", from: "hand", to: "field", appliesLock: "machine-synchro", text: "Normal summon Smiger."},
		// B: a second Normal Summon with nothing granting one, and from the DECK.
		{n: 2, card: "Scrap Recycler", action: "normal-summon", from: "deck", to: "field", text: "Illegal second Normal Summon."},
		// C: revived from the GY before anything put it there.
		{n: 3, card: "Crystron Tristaros", action: "special-summon", from: "gy", to: "field", text: "Claims to revive a card still in the deck."},
		// D: Xyz after the Machine Synchro lock, with materials that are not on the field.
		{
			n: 4, card: "Superdreadnought Rail Cannon Gustav Max", action: "xyz", from: "extra", to: "field"
			result: "Superdreadnought Rail Cannon Gustav Max"
			materials: ["Night Train Blue Traveler", "Heavy Freight Train Derricrane"]
			text: "Blue Traveler is still in hand, Derricrane is still in the deck."
		},
		// E: Synchro maths wrong, and zero Tuners among the materials.
		{
			n: 5, card: "Crystron Eleskeletus", action: "synchro", from: "extra", to: "field"
			result: "Crystron Eleskeletus"
			materials: ["Crystron Smiger", "Scrap Recycler"]
			text: "3 + 3 = 6, but Eleskeletus is Level 7, and neither material is a Tuner."
		},
		// F: not in the Yukinon decklist at all.
		{n: 6, card: "Crystron Citree", action: "search", from: "deck", to: "hand", text: "Not in this build."},
		// G: a once per DUEL effect used twice.
		{n: 7, card: "Night Train Blue Traveler", action: "special-summon", from: "gy", to: "field", oncePerDuel: "Night Train Blue Traveler:revive", text: "First use."},
		{n: 8, card: "Night Train Blue Traveler", action: "special-summon", from: "gy", to: "field", oncePerDuel: "Night Train Blue Traveler:revive", text: "Second use of a once per DUEL effect."},
		// H: an ALTERNATE summon after the Machine Synchro lock. An alt summon bypasses the
		// MATERIAL rule; it does not bypass the LOCK.
		{
			n: 9, card: "Superdreadnought Rail Cannon Juggernaut Liebe", action: "xyz", from: "extra", to: "field"
			result:        "Superdreadnought Rail Cannon Juggernaut Liebe"
			usesAltSummon: true
			materials: ["Superdreadnought Rail Cannon Gustav Max"]
			text: "Climbing off Gustav Max, which is still illegal under the lock from step 1."
		},
	]
}
