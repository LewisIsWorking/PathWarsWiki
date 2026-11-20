--[[message
Natasha practice: her Horus Dragoon end board (Dragoon + all 4 Sons, Black Flame Deity in hand) vs your Witchcrafter deck, going 2nd. Random hand 2/10 (v3: full duel, no turn limit).
Opening hand: Witchcrafter Walpurgis, The Gaze of Timaeus, Witchcrafter Marka, Super Polymerization, Witchcrafter Creation, Witchcrafter Pittore.
Hand traps used on her turn: none -> she lost: nothing.
Win = win the duel. Her AI is much weaker than Natasha: count it as a win only if you win within 2 of your turns.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)

--Your hand
Debug.AddCard(32353566,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Witchcrafter Walpurgis
Debug.AddCard(22283204,0,0,LOCATION_HAND,0,POS_FACEDOWN) --The Gaze of Timaeus
Debug.AddCard(6071005,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Witchcrafter Marka
Debug.AddCard(48130397,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(57916305,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Witchcrafter Creation
Debug.AddCard(95245544,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Witchcrafter Pittore
--Your Main Deck
Debug.AddCard(22623509,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Verre, the Maid of Endymion
Debug.AddCard(57916305,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Creation
Debug.AddCard(23434538,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
Debug.AddCard(32353566,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Walpurgis
Debug.AddCard(38943357,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Spell Power Mastery
Debug.AddCard(97268402,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Effect Veiler
Debug.AddCard(32353566,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Walpurgis
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(73664385,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Verre Magic - Lacrima of Light
Debug.AddCard(21744288,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Schmietta
Debug.AddCard(70226289,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Unveiling
Debug.AddCard(875572,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Crowley, the Gifted Magistus
Debug.AddCard(83289866,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Bystreet
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(73664385,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Verre Magic - Lacrima of Light
Debug.AddCard(69748261,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Distortion
Debug.AddCard(21522601,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Madame Verre
Debug.AddCard(6071005,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Marka
Debug.AddCard(6958567,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Celebration
Debug.AddCard(59851535,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Potterie
Debug.AddCard(70686400,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Terracottan
Debug.AddCard(64756282,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Genni
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(6071005,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Marka
Debug.AddCard(97268402,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Effect Veiler
Debug.AddCard(73664385,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Verre Magic - Lacrima of Light
Debug.AddCard(57916305,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Creation
Debug.AddCard(7656689,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Genni, the Maid of Endymion
Debug.AddCard(70226289,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Unveiling
Debug.AddCard(84523092,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Haine
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(6958567,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Celebration
Debug.AddCard(70226289,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Witchcrafter Unveiling
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
--Your Extra Deck
Debug.AddCard(54757758,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Mudragon of the Swamp
Debug.AddCard(11765832,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Garura, Wings of Resonant Life
Debug.AddCard(37818794,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Red-Eyes Dark Dragoon
Debug.AddCard(9603252,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Witchcrafter Vice-Madame
Debug.AddCard(37260677,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Zoroa, the Magistus Verethragna
Debug.AddCard(59400890,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Dark Magician of Destruction
Debug.AddCard(27118421,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Starving Venom Fusion Dragon, Four Heavenly Dragons
Debug.AddCard(33475154,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Witchcrafter Madame Rilliona
Debug.AddCard(69964858,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Witchcrafter Pupils
Debug.AddCard(69964858,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Witchcrafter Pupils
Debug.AddCard(33166263,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Hyperinvoked Aeon
Debug.AddCard(34755994,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Artemis, the Magistus Moon Maiden
Debug.AddCard(50277355,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Cross-Sheep
Debug.AddCard(29301450,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --S:P Little Knight
Debug.AddCard(20714553,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Endymion, the Crescent Magistus
--Your hand traps already used on her turn
--Her board pieces your hand traps didn't stop
Debug.AddCard(37818794,1,1,LOCATION_MZONE,5,POS_FACEUP_ATTACK,true) --Red-Eyes Dark Dragoon
Debug.AddCard(79791878,1,1,LOCATION_SZONE,1,POS_FACEUP) --Shining Sarcophagus
Debug.AddCard(47330808,1,1,LOCATION_MZONE,3,POS_FACEUP_ATTACK,true) --Hapi, Guidance of Horus
Debug.AddCard(11335209,1,1,LOCATION_MZONE,1,POS_FACEUP_ATTACK,true) --Duamutef, Blessing of Horus
Debug.AddCard(74725513,1,1,LOCATION_MZONE,2,POS_FACEUP_ATTACK,true) --Qebehsenuef, Protection of Horus
--Her fixed cards
Debug.AddCard(84941194,1,1,LOCATION_MZONE,0,POS_FACEUP_ATTACK,true) --Imsety, Glory of Horus
--Her Spells/Traps
Debug.AddCard(16528181,1,1,LOCATION_SZONE,0,POS_FACEUP) --King's Sarcophagus
Debug.AddCard(78679226,1,1,LOCATION_SZONE,2,POS_FACEDOWN) --Future Silence
Debug.AddCard(26984177,1,1,LOCATION_FZONE,0,POS_FACEUP) --Walls of the Imperial Tomb
--Her hand: Horus the Black Flame Deity waits for a Son to leave the field
Debug.AddCard(99307040,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Horus the Black Flame Deity
Debug.AddCard(14558127,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(94145021,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(46986414,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Dark Magician
--Her GY
Debug.AddCard(2501624,1,1,LOCATION_GRAVE,0,POS_FACEUP) --Dark Magician Girl the Magician's Apprentice
Debug.AddCard(41350417,1,1,LOCATION_GRAVE,0,POS_FACEUP) --Dark Magical Curtain
Debug.AddCard(22283204,1,1,LOCATION_GRAVE,0,POS_FACEUP) --The Gaze of Timaeus
Debug.AddCard(97526666,1,1,LOCATION_GRAVE,0,POS_FACEUP) --Planet Pathfinder
--Her Deck
Debug.AddCard(46986414,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magician
Debug.AddCard(97526666,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Planet Pathfinder
Debug.AddCard(97526666,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Planet Pathfinder
Debug.AddCard(84941194,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Imsety, Glory of Horus
Debug.AddCard(84941194,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Imsety, Glory of Horus
Debug.AddCard(79791878,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Shining Sarcophagus
Debug.AddCard(16528181,1,1,LOCATION_DECK,0,POS_FACEDOWN) --King's Sarcophagus
Debug.AddCard(16528181,1,1,LOCATION_DECK,0,POS_FACEDOWN) --King's Sarcophagus
Debug.AddCard(78679226,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Future Silence
Debug.AddCard(78679226,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Future Silence

Debug.ReloadFieldEnd()
Debug.ShowHint("Win within 2 of your turns.")
