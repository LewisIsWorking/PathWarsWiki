// 2026-08-10: Route 3, Exceptional Schedule into Centur-Ion Legatia.
// The Diagram Token is not modelled as a step: a Token is not a card in the vocabulary, and its
// only job is to satisfy Urgent Schedule's activation condition, which this model does not check.
// Must stay identical in content to pkl/RouteSchedule.pkl.
package crystron

routeSchedule: #Route & {
	name:  "Exceptional Schedule into Centur-Ion Legatia"
	build: "yukinon"
	opening: ["Exceptional Schedule", "Crystron Smiger"]
	steps: [
		{n: 1, card: "Exceptional Schedule", action: "activate", from: "hand", to: "gy",
			oncePerTurn: "Exceptional Schedule:search",
			text:        "Add Urgent Schedule, then hand the opponent a level 10 Diagram Token."},

		{n: 2, card: "Urgent Schedule", action: "search", from: "deck", to: "hand",
			text: "Searched by Exceptional Schedule."},

		{n: 3, card: "Urgent Schedule", action: "activate", from: "hand", to: "gy",
			oncePerTurn: "Urgent Schedule:summon",
			text:        "Live because the token means the opponent controls more monsters than you."},

		{n: 4, card: "Scrap Recycler", action: "special-summon", from: "deck", to: "field",
			text: "The level 4 or lower EARTH machine. Effects NEGATED, so it does NOT mill."},

		{n: 5, card: "Night Train Blue Traveler", action: "special-summon", from: "deck", to: "field",
			text: "The level 5 or higher EARTH machine. Also negated."},

		{n: 6, card: "Crystron Smiger", action: "normal-summon", from: "hand", to: "field",
			text: "Normal summon Smiger to fetch a tuner."},

		{n: 7, card: "Scrap Recycler", action: "destroy", from: "field", to: "gy",
			text: "Smiger targets a face-up card YOU control and destroys it."},

		{n: 8, card: "Crystron Tristaros", action: "special-summon", from: "deck", to: "field",
			appliesLock: "machine-synchro",
			oncePerTurn: "Crystron Smiger:summon",
			text:        "Smiger summons a Crystron tuner from deck. Locks Machine SYNCHRO: no Xyz this turn."},

		{n: 9, card: "Centur-Ion Legatia", action: "synchro", from: "extra", to: "field",
			result: "Centur-Ion Legatia",
			materials: ["Night Train Blue Traveler", "Crystron Tristaros"],
			text: "10 + 2 = 12. On summon: draw 1, destroy the opponent's highest ATK monster, which is the token you gave them."},
	]
}
