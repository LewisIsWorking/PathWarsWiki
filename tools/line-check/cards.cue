// Card facts the checker needs. Text checked on YGOPRODeck, 24-25 Nov 2026.
// Effect names are our own short labels; each is once per turn unless listed in notOpt.
package lines

cards: {
	// --- Rikka (all WATER Plants) ---
	"Rikka Petal": {kind: "monster", race: "Plant", attr: "WATER", level: 1, effects: ["take", "revive"], atk: 0} // take: add OR send a Rikka monster (set sendsToGY on the step when sending)
	"Rikka Black Princess": {kind: "monster", race: "Plant", attr: "WATER", level: 6, effects: ["summon_self", "tribute_summon"], atk: 0} // summon_self (hand or GY) locks to Plants
	"Mudan the Rikka Fairy": {kind: "monster", race: "Plant", attr: "WATER", level: 6, effects: ["summon_self", "search"], addEffects: ["search"], atk: 1000}
	"Hellebore the Rikka Fairy": {kind: "monster", race: "Plant", attr: "WATER", level: 8, effects: ["negate", "revive"], atk: 2600, defEffects: ["revive"]}
	"Primrose the Rikka Fairy Duo": {kind: "monster", race: "Plant", attr: "WATER", level: 8, effects: ["tribute_trigger", "level", "quick_xyz"], atk: 2600, defEffects: ["tribute_trigger"]}
	"Rikka Princess": {kind: "monster", race: "Plant", attr: "WATER", level: 4, effects: ["summon_self", "negate"], atk: 0}
	"Rikka Konkon": {kind: "spell", effects: ["activate", "set", "replace_tribute"], notOpt: ["activate"]}
	"Rikka Glamour": {kind: "spell", effects: ["activate"], addEffects: ["activate"]}
	"Rikka Moonlit Waters": {kind: "spell", effects: ["activate"], gyEffects: ["activate"], addEffects: ["activate"], pairEffects: ["activate"]} // 2 Rikka monsters from the DECK, same Level, different names: add 1, send 1
	"Rikka Sheet": {kind: "trap", effects: ["activate"]}
	"Rikka Queen Strenna": {frame: "xyz", kind: "monster", race: "Plant", attr: "WATER", level: 4, effects: ["add", "tributed"], atk: 2000, needsMaterial: ["add", "tributed"]}
	"Rikka Sacred Queen Strenna": {frame: "xyz", kind: "monster", race: "Plant", attr: "WATER", level: 6, effects: ["summon_xyz", "set_trap"], atk: 2000, defEffects: ["summon_xyz"]}
	"Kanzashi the Rikka Queen": {frame: "xyz", kind: "monster", race: "Plant", attr: "WATER", level: 6, effects: ["revive", "protect"], atk: 2400}
	"Teardrop the Rikka Queen": {frame: "xyz", kind: "monster", race: "Plant", attr: "WATER", level: 8, effects: ["tribute"], atk: 2800}
	"Teardrop the Rikka Sacred Queen": {frame: "xyz", kind: "monster", race: "Plant", attr: "WATER", level: 10, effects: ["send_tribute"], atk: 3200}
	"Sacred Tree Beast, Hyperyton": {frame: "xyz", kind: "monster", race: "Plant", attr: "EARTH", level: 9, effects: ["attach", "negate"], atk: 2600}
	"Orea, the Sylvan High Arbiter": {frame: "xyz", kind: "monster", race: "Plant", attr: "DARK", level: 7, effects: ["look", "excavate"]}

	"Primula the Rikka Fairy": {kind: "monster", race: "Plant", attr: "WATER", level: 4, effects: ["summon_self", "search"], addEffects: ["search"], atk: 800}
	"Foolish Burial": {kind: "spell", effects: ["activate"], gyEffects: ["activate"]}
	"Crossout Designator": {kind: "spell", effects: ["activate"]}
	"Infinite Impermanence": {kind: "trap", effects: ["activate"], notOpt: ["activate"]}

	// --- Predaplant ---
	"Predaplant Longinephila": {kind: "monster", race: "Plant", attr: "DARK", level: 1, tuner: true, effects: ["search", "gy"], addEffects: ["search"], atk: 600}
	"Predaplant Byblisp": {kind: "monster", race: "Plant", attr: "DARK", level: 1, effects: ["search", "revive"], addEffects: ["search"], atk: 0}
	"Predaplant Lilizard": {kind: "monster", race: "Plant", attr: "DARK", level: 3, effects: ["summon_self", "dark", "draw"], atk: 1200}
	"Princess Dracaena, the Thirsting Tree": {kind: "monster", race: "Plant", attr: "DARK", level: 1, tuner: true, effects: ["summon_self", "gy"], gyEffects: ["summon_self"], atk: 0}
	"Predaprimitive": {kind: "spell", effects: ["activate", "destroy"], gyEffects: ["activate"], addEffects: ["activate"]}
	"Instant Fusion": {kind: "spell", effects: ["activate"]}
	"Super Polymerization": {kind: "spell", effects: ["activate"], notOpt: ["activate"]}
	"Polymerization": {kind: "spell", effects: ["activate"], notOpt: ["activate"]}
	"Predaplant Ambulomelides": {frame: "fusion", kind: "monster", race: "Plant", attr: "DARK", level: 5, effects: ["search", "tribute"], addEffects: ["search"], atk: 1000}
	"Predaplant Bal Teah": {frame: "synchro", kind: "monster", race: "Plant", attr: "DARK", level: 4, tuner: true, effects: ["revive", "fusion"], atk: 1900}
	"Aromaseraphy Jasmine": {frame: "link", kind: "monster", race: "Plant", attr: "LIGHT", level: 2, effects: ["tribute", "search"], atk: 1800, defEffects: ["tribute"]} // 2 Plants; arrows down-left + down-right
	"Sylvan Dancepione": {frame: "link", kind: "monster", race: "Plant", attr: "WIND", level: 2, effects: ["excavate", "level"], atk: 1200} // 2 Plants; arrows down-left + down-right. excavate: on Link Summon, 1-3 cards, Special Summon up to 2 Plants (not Link material: list them in noLink), rest to GY. level: monsters it points to become a GY Plant's Level (setLevel)
	"Predaplant Daredevil": {frame: "fusion", kind: "monster", race: "Plant", attr: "DARK", level: 6, atk: 2200}
	"Starving Venom Fusion Dragon": {frame: "fusion", kind: "monster", race: "Dragon", attr: "DARK", level: 8, effects: ["atk", "copy", "destroyed"], atk: 2800}
	"Garura, Wings of Resonant Life": {frame: "fusion", kind: "monster", race: "Winged Beast", attr: "DARK", level: 6, effects: ["draw"], atk: 1500} // battle damage involving it is doubled; draws 1 when sent to the GY (e.g. as Xyz material)
	"Predaplant Dragostapelia": {frame: "fusion", kind: "monster", race: "Plant", attr: "DARK", level: 8, effects: ["counter"], atk: 2700} // 1 Fusion Monster + 1 DARK monster. counter: Quick Effect, target 1 of theirs, Predator Counter (it becomes Level 1); their activated monster effects with a counter are negated on resolution
	"Mudragon of the Swamp": {frame: "fusion", kind: "monster", race: "Wyrm", attr: "WATER", level: 4, effects: ["attr"], atk: 1900} // 2 monsters with the same Attribute, different Types. They can't target it or your monsters with its Attribute; attr: Quick Effect, declare an Attribute until end of turn
	"Crystal Wing Synchro Dragon": {frame: "synchro", kind: "monster", race: "Dragon", attr: "WIND", level: 8, effects: ["negate"], atk: 3000}
	"Cactus Bouncer": {kind: "monster", race: "Plant", attr: "EARTH", level: 4, atk: 1800} // can't be Special Summoned: use lock "no_special" on its Normal Summon

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

	// --- Opponents' monsters (Type, Attribute, Level, ATK), for Fusion material and lethal checks.
	// Text checked against ProjectIgnis BabelCDB, 25 Nov 2026. Use them in lines as "opp:<name>".
	// Horus (Natasha, Ryuuku)
	"Imsety, Glory of Horus": {kind: "monster", race: "Spellcaster", attr: "DARK", level: 8, atk: 3000}
	"Duamutef, Blessing of Horus": {kind: "monster", race: "Beast", attr: "WATER", level: 8, atk: 0} // +1200 per Horus monster
	"Hapi, Guidance of Horus": {kind: "monster", race: "Beast-Warrior", attr: "WIND", level: 8, atk: 2400}
	"Qebehsenuef, Protection of Horus": {kind: "monster", race: "Winged Beast", attr: "EARTH", level: 8, atk: 2500}
	"Horus the Black Flame Deity": {kind: "monster", race: "Dragon", attr: "FIRE", level: 8, atk: 3000}
	"Silhouhatte Rabbit": {frame: "link", kind: "monster", race: "Illusion", attr: "LIGHT", level: 2, atk: 1500}
	"Obelisk the Tormentor": {kind: "monster", race: "Divine-Beast", attr: "DIVINE", level: 10, atk: 4000} // can't be targeted
	"Divine Serpent Apophis": {frame: "fusion", kind: "monster", race: "Reptile", attr: "EARTH", level: 6, atk: 2800}
	"Apophis the Swamp Deity": {kind: "monster", race: "Reptile", attr: "EARTH", level: 6, atk: 2000} // Trap that summons itself
	// Sky Striker (ニノマエ, Luke)
	"Sky Striker Ace = Zero": {frame: "link", kind: "monster", race: "Machine", attr: "LIGHT", level: 2, atk: 2000}
	"Sky Striker Ace - Kagari": {frame: "link", kind: "monster", race: "Machine", attr: "FIRE", level: 1, atk: 1500}
	"Sky Striker Ace - Shizuku": {frame: "link", kind: "monster", race: "Machine", attr: "WATER", level: 1, atk: 1500}
	"Sky Striker Ace - Raye": {kind: "monster", race: "Warrior", attr: "DARK", level: 4, atk: 1500}
	"Sky Striker Ace - Roze": {kind: "monster", race: "Warrior", attr: "LIGHT", level: 4, atk: 1500}
	// Machina (bilotahn)
	"Machina Fortress": {kind: "monster", race: "Machine", attr: "EARTH", level: 7, atk: 2500}
	"Machina Citadel": {kind: "monster", race: "Machine", attr: "EARTH", level: 10, atk: 3000}
	"Machina Air Raider": {kind: "monster", race: "Machine", attr: "EARTH", level: 8, atk: 1500}
	"Machina Irradiator": {kind: "monster", race: "Machine", attr: "EARTH", level: 8, atk: 1700}
	"Machina Unclaspare": {kind: "monster", race: "Machine", attr: "DARK", level: 4, atk: 1800}
	"Machina Ruinforce": {kind: "monster", race: "Machine", attr: "DARK", level: 10, atk: 4600}
	// Cyber Dragon (Jack)
	"Cyber Dragon": {kind: "monster", race: "Machine", attr: "LIGHT", level: 5, atk: 2100}
	"Cyber Dragon Infinity": {frame: "xyz", kind: "monster", race: "Machine", attr: "LIGHT", level: 6, atk: 2100} // +200 per material
	"Cyber Dragon Nova": {frame: "xyz", kind: "monster", race: "Machine", attr: "LIGHT", level: 5, atk: 2100}
	"Chimeratech Fortress Dragon": {frame: "fusion", kind: "monster", race: "Machine", attr: "DARK", level: 8, atk: 0} // 1000 per material
	"Cyber Eternity Dragon": {frame: "fusion", kind: "monster", race: "Machine", attr: "LIGHT", level: 10, atk: 2800}
	// Natasha (Dragoon)
	"Red-Eyes Dark Dragoon": {frame: "fusion", kind: "monster", race: "Spellcaster", attr: "DARK", level: 8, atk: 3000} // can't be targeted or destroyed by card effects
	// HERO (Rhino)
	"Masked HERO Dark Law": {frame: "fusion", kind: "monster", race: "Warrior", attr: "DARK", level: 6, atk: 2400}
	"Contrast HERO Chaos": {frame: "fusion", kind: "monster", race: "Warrior", attr: "DARK", level: 9, atk: 3000} // also LIGHT while face-up
	"Elemental HERO Shining Neos Wingman": {frame: "fusion", kind: "monster", race: "Warrior", attr: "LIGHT", level: 8, atk: 3100}
	"Masked HERO Vapor": {frame: "fusion", kind: "monster", race: "Warrior", attr: "WATER", level: 6, atk: 2400}
	"Elemental HERO Sunrise": {frame: "fusion", kind: "monster", race: "Warrior", attr: "LIGHT", level: 7, atk: 2500}
	// Elfnote / Power Patron (trampaslocas)
	"Elfnote Fortuna": {kind: "monster", race: "Spellcaster", attr: "LIGHT", level: 6, atk: 2200}
	"Elfnote Lucina": {kind: "monster", race: "Spellcaster", attr: "FIRE", level: 6, atk: 2500}
	"Elfnote Tinia": {kind: "monster", race: "Spellcaster", attr: "WATER", level: 6, atk: 2400}
	"Elfnote Regina": {kind: "monster", race: "Spellcaster", attr: "WIND", level: 6, atk: 2000}
	"Elfnote Power Patron": {kind: "monster", race: "Fiend", attr: "FIRE", level: 1, atk: 300}
	"Elfnote Seraphim Strelitzia": {frame: "synchro", kind: "monster", race: "Plant", attr: "FIRE", level: 7}
	"Baronne de Fleur": {frame: "synchro", kind: "monster", race: "Warrior", attr: "WIND", level: 10, atk: 3000}
	"S:P Little Knight": {frame: "link", kind: "monster", race: "Warrior", attr: "DARK", level: 2, atk: 1600}
}
