// Card facts the checker needs. Text checked on YGOPRODeck, 24-25 Nov 2026.
// Effect names are our own short labels; each is once per turn unless listed in notOpt.
package lines

cards: {
	// --- Rikka (all WATER Plants) ---
	"Rikka Petal": {kind: "monster", race: "Plant", level: 1, effects: ["take", "revive"], atk: 0} // take: add OR send a Rikka monster (set sendsToGY on the step when sending)
	"Rikka Black Princess": {kind: "monster", race: "Plant", level: 6, effects: ["summon_self", "tribute_summon"], atk: 0} // summon_self (hand or GY) locks to Plants
	"Mudan the Rikka Fairy": {kind: "monster", race: "Plant", level: 6, effects: ["summon_self", "search"], addEffects: ["search"], atk: 1000}
	"Hellebore the Rikka Fairy": {kind: "monster", race: "Plant", level: 8, effects: ["negate", "revive"], atk: 2600, defEffects: ["revive"]}
	"Primrose the Rikka Fairy Duo": {kind: "monster", race: "Plant", level: 8, effects: ["tribute_trigger", "level", "quick_xyz"], atk: 2600, defEffects: ["tribute_trigger"]}
	"Rikka Princess": {kind: "monster", race: "Plant", level: 4, effects: ["summon_self", "negate"], atk: 0}
	"Rikka Konkon": {kind: "spell", effects: ["activate", "set", "replace_tribute"], notOpt: ["activate"]}
	"Rikka Glamour": {kind: "spell", effects: ["activate"], addEffects: ["activate"]}
	"Rikka Moonlit Waters": {kind: "spell", effects: ["activate"], gyEffects: ["activate"], addEffects: ["activate"]}
	"Rikka Sheet": {kind: "trap", effects: ["activate"]}
	"Rikka Queen Strenna": {frame: "xyz", kind: "monster", race: "Plant", level: 4, effects: ["add", "tributed"], atk: 2000, needsMaterial: ["add", "tributed"]}
	"Rikka Sacred Queen Strenna": {frame: "xyz", kind: "monster", race: "Plant", level: 6, effects: ["summon_xyz", "set_trap"], atk: 2000, defEffects: ["summon_xyz"]}
	"Kanzashi the Rikka Queen": {frame: "xyz", kind: "monster", race: "Plant", level: 6, effects: ["revive", "protect"], atk: 2400}
	"Teardrop the Rikka Queen": {frame: "xyz", kind: "monster", race: "Plant", level: 8, effects: ["tribute"], atk: 2800}
	"Teardrop the Rikka Sacred Queen": {frame: "xyz", kind: "monster", race: "Plant", level: 10, effects: ["send_tribute"], atk: 3200}
	"Sacred Tree Beast, Hyperyton": {frame: "xyz", kind: "monster", race: "Plant", level: 9, effects: ["attach", "negate"], atk: 2600}
	"Orea, the Sylvan High Arbiter": {frame: "xyz", kind: "monster", race: "Plant", level: 7, effects: ["look", "excavate"]}

	"Primula the Rikka Fairy": {kind: "monster", race: "Plant", level: 4, effects: ["summon_self", "search"], addEffects: ["search"], atk: 800}
	"Foolish Burial": {kind: "spell", effects: ["activate"], gyEffects: ["activate"]}
	"Crossout Designator": {kind: "spell", effects: ["activate"]}
	"Infinite Impermanence": {kind: "trap", effects: ["activate"], notOpt: ["activate"]}

	// --- Predaplant ---
	"Predaplant Longinephila": {kind: "monster", race: "Plant", level: 1, tuner: true, effects: ["search", "gy"], addEffects: ["search"], atk: 600}
	"Predaplant Byblisp": {kind: "monster", race: "Plant", level: 1, effects: ["search", "revive"], addEffects: ["search"], atk: 0}
	"Predaplant Lilizard": {kind: "monster", race: "Plant", level: 3, effects: ["summon_self", "dark", "draw"], atk: 1200}
	"Princess Dracaena, the Thirsting Tree": {kind: "monster", race: "Plant", level: 1, tuner: true, effects: ["summon_self", "gy"], gyEffects: ["summon_self"], atk: 0}
	"Predaprimitive": {kind: "spell", effects: ["activate", "destroy"], gyEffects: ["activate"], addEffects: ["activate"]}
	"Instant Fusion": {kind: "spell", effects: ["activate"]}
	"Super Polymerization": {kind: "spell", effects: ["activate"], notOpt: ["activate"]}
	"Polymerization": {kind: "spell", effects: ["activate"], notOpt: ["activate"]}
	"Predaplant Ambulomelides": {frame: "fusion", kind: "monster", race: "Plant", level: 5, effects: ["search", "tribute"], addEffects: ["search"], atk: 1000}
	"Predaplant Bal Teah": {frame: "synchro", kind: "monster", race: "Plant", level: 4, tuner: true, effects: ["revive", "fusion"], atk: 1900}
	"Aromaseraphy Jasmine": {frame: "link", kind: "monster", race: "Plant", level: 2, effects: ["tribute", "search"], atk: 1800, defEffects: ["tribute"]}
	"Predaplant Daredevil": {frame: "fusion", kind: "monster", race: "Plant", level: 6, atk: 2200}
	"Starving Venom Fusion Dragon": {frame: "fusion", kind: "monster", race: "Dragon", level: 8, effects: ["atk", "copy", "destroyed"], atk: 2800}
	"Garura, Wings of Resonant Life": {frame: "fusion", kind: "monster", race: "Winged Beast", level: 6, effects: ["draw"]}
	"Crystal Wing Synchro Dragon": {frame: "synchro", kind: "monster", race: "Dragon", level: 8, effects: ["negate"], atk: 3000}
	"Cactus Bouncer": {kind: "monster", race: "Plant", level: 4, atk: 1800} // can't be Special Summoned: use lock "no_special" on its Normal Summon

	// --- Hand traps and tech ---
	"Ash Blossom & Joyous Spring": {kind: "monster", race: "Zombie", level: 3, tuner: true, effects: ["negate"]}
	"Droll & Lock Bird": {kind: "monster", race: "Spellcaster", level: 1, effects: ["activate"]}
	"Maxx \"C\"": {kind: "monster", race: "Insect", level: 2, effects: ["activate"]}
	"Mulcharmy Purulia": {kind: "monster", race: "Aqua", level: 4, effects: ["activate"]}
	"Mulcharmy Fuwalos": {kind: "monster", race: "Spellcaster", level: 4, effects: ["activate"]}
	"Triple Tactics Talent": {kind: "spell", effects: ["activate"]}
	"Forbidden Droplet": {kind: "spell", effects: ["activate"], gyEffects: ["activate"]}
	"Evenly Matched": {kind: "trap", effects: ["activate"], notOpt: ["activate"]}
	"Dominus Impulse": {kind: "trap", effects: ["activate"]}
}
