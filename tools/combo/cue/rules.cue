// AUTHORED, not generated. Mirror of pkl/Rules.pkl so the two models describe the same ruleset.
package crystron

#CardFacts: close({
	kind:      "main" | "synchro" | "xyz" | "link" | "spell" | "trap"
	level:     int & >=0
	tuner:     bool
	race:      string
	attribute: string
})

// NOTE: maxMaterials/maxTuners/requiresRace use sentinel DEFAULTS rather than being optional.
// CUE cannot compare a field against "absent" inside a comprehension, so an optional field would
// have to be guarded some other way. Pkl expresses these as nullable and tests `!= null`.
// First divergence forced by the language rather than by the ruleset.
#MaterialRule: close({
	summonType:             "synchro" | "xyz" | "link"
	minMaterials:           int & >=1
	maxMaterials:           int | *99
	minTuners:              int | *0
	maxTuners:              int | *99
	sameLevel:              bool | *false
	levelsMustTotal:        bool | *false
	requiresRace:           string | *""
	materialsMustBeSynchro: bool | *false
	altSummon:              string | *""
})

requirements: [string]: #MaterialRule
requirements: {
	"Crystron Eleskeletus": {summonType: "synchro", minMaterials: 2, minTuners: 1, maxTuners: 1, levelsMustTotal: true}
	"Centur-Ion Legatia":   {summonType: "synchro", minMaterials: 2, minTuners: 1, maxTuners: 1, levelsMustTotal: true}
	"F.A. Dawn Dragster":   {summonType: "synchro", minMaterials: 2, minTuners: 1, maxTuners: 1, levelsMustTotal: true}
	"Crystron Quariongandrax": {summonType: "synchro", minMaterials: 3, minTuners: 2, levelsMustTotal: true}

	"Infinitrack River Stormer": {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true}
	"Cyber Dragon Nova":         {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true, requiresRace: "Machine"}
	"Cyber Dragon Infinity":     {summonType: "xyz", minMaterials: 3, maxMaterials: 3, sameLevel: true, requiresRace: "Machine", altSummon: "using Cyber Dragon Nova you control as material"}
	"Superdreadnought Rail Cannon Gustav Max":            {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true}
	"Number 81: Superdreadnought Rail Cannon Super Dora": {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true}
	"Superdreadnought Rail Cannon Flying Launcher":       {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true}
	"Superdreadnought Rail Cannon Gustav Rocket":         {summonType: "xyz", minMaterials: 3, maxMaterials: 3, sameLevel: true, altSummon: "discard 1 and use a Gustav Max you control"}
	"Superdreadnought Rail Cannon Juggernaut Liebe":      {summonType: "xyz", minMaterials: 3, maxMaterials: 3, sameLevel: true, altSummon: "use 1 Rank 10 Machine Xyz you control"}
	"Divine Arsenal AA-ZEUS - Sky Thunder":               {summonType: "xyz", minMaterials: 2, maxMaterials: 2, sameLevel: true, altSummon: "use 1 Xyz you control, if an Xyz battled"}

	"Clockwork Knight":            {summonType: "link", minMaterials: 1, maxMaterials: 1, requiresRace: "Machine"}
	"Qliphort Genius":             {summonType: "link", minMaterials: 2, maxMaterials: 2, requiresRace: "Machine"}
	"Double Headed Anger Knuckle": {summonType: "link", minMaterials: 2, maxMaterials: 2, requiresRace: "Machine"}
	"Ancient Gear Ballista":       {summonType: "link", minMaterials: 2, maxMaterials: 2, requiresRace: "Machine"}
}

decks: [string]: [string]: int
decks: {
	amelia: {
		"Crystron Tristaros": 1, "Crystron Citree": 1, "Crystron Smiger": 1
		"Crystron Thystvern": 1, "Crystron Sulfefnir": 2, "Crystron Sulfador": 2
		"Crystron Inclusion": 3, "Crystron Cluster": 1
		"Night Train Blue Traveler": 3, "Scrap Recycler": 3
		"Heavy Freight Train Derricrane": 1, "Heavy Armored Knight Babeldecker": 1
		"Flying Pegasus Railroad Stampede": 1, "Therion \"King\" Regulus": 1
		"Spell Canceller": 1, "Exceptional Schedule": 3, "Urgent Schedule": 2
		"Revolving Switchyard": 1, "Called by the Grave": 1, "Crossout Designator": 1
		"Triple Tactics Talent": 1, "Forbidden Droplet": 3
		"Ash Blossom & Joyous Spring": 3, "Maxx \"C\"": 1, "Droll & Lock Bird": 2
		"Mulcharmy Fuwalos": 3
		"Crystron Eleskeletus": 2, "Crystron Quariongandrax": 1, "Centur-Ion Legatia": 1
		"F.A. Dawn Dragster": 1, "Infinitrack River Stormer": 1
		"Superdreadnought Rail Cannon Gustav Max": 1
		"Number 81: Superdreadnought Rail Cannon Super Dora": 1
		"Superdreadnought Rail Cannon Flying Launcher": 1
		"Superdreadnought Rail Cannon Gustav Rocket": 1
		"Superdreadnought Rail Cannon Juggernaut Liebe": 1
		"Clockwork Knight": 1, "Qliphort Genius": 1
		"Double Headed Anger Knuckle": 1, "Ancient Gear Ballista": 1
	}
	yukinon: {
		"Crystron Tristaros": 1, "Crystron Smiger": 1
		"Crystron Sulfefnir": 2, "Crystron Sulfador": 3
		"Crystron Inclusion": 3, "Crystron Cluster": 1
		"Night Train Blue Traveler": 3, "Scrap Recycler": 3
		"Heavy Freight Train Derricrane": 1, "Heavy Armored Knight Babeldecker": 1
		"Therion \"King\" Regulus": 1
		"Exceptional Schedule": 3, "Urgent Schedule": 2, "Revolving Switchyard": 1
		"Foolish Burial": 1, "Called by the Grave": 1, "Crossout Designator": 1
		"Triple Tactics Talent": 1, "Barrage Blast": 1
		"Ash Blossom & Joyous Spring": 3, "Maxx \"C\"": 1
		"Ghost Belle & Haunted Mansion": 2, "Mulcharmy Fuwalos": 3
		"Crystron Eleskeletus": 1, "Centur-Ion Legatia": 1, "F.A. Dawn Dragster": 1
		"Infinitrack River Stormer": 1, "Cyber Dragon Nova": 1, "Cyber Dragon Infinity": 1
		"Superdreadnought Rail Cannon Gustav Max": 1
		"Number 81: Superdreadnought Rail Cannon Super Dora": 1
		"Superdreadnought Rail Cannon Flying Launcher": 1
		"Superdreadnought Rail Cannon Gustav Rocket": 1
		"Superdreadnought Rail Cannon Juggernaut Liebe": 1
		"Divine Arsenal AA-ZEUS - Sky Thunder": 1
		"Clockwork Knight": 1, "Qliphort Genius": 1, "Double Headed Anger Knuckle": 1
	}
}
