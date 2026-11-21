--[[message
PredaRikka vs Natasha, GOING SECOND, random hand 7/10.
Opening hand: Predaprimitive, Predaplant Longinephila, Princess Dracaena, the Thirsting Tree, Predaplant Byblisp, Mulcharmy Fuwalos (+1 draw).
Hand traps used on her turn: Mulcharmy Fuwalos -> she lost: Dragoon.
Plan: Droplet first (send a monster), remove with Tributes, answer Horus the Black Flame Deity with Rikka Princess or Dominus, Super Poly Dragoon + your DARK Predaplant, Evenly Matched after battle. Win within 2 of your turns.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)
--Your hand
Debug.AddCard(89176044,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Predaprimitive
Debug.AddCard(44994712,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Predaplant Longinephila
Debug.AddCard(79966218,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Princess Dracaena, the Thirsting Tree
Debug.AddCard(44932065,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Predaplant Byblisp
--Your Main Deck
Debug.AddCard(24299458,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Forbidden Droplet
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(78646298,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Black Princess
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(89176044,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Predaprimitive
Debug.AddCard(81611932,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Moonlit Waters
Debug.AddCard(42651293,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Primrose the Rikka Fairy Duo
Debug.AddCard(78646298,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Black Princess
Debug.AddCard(18595008,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Predaplant Lilizard
Debug.AddCard(31615285,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Cactus Bouncer
Debug.AddCard(79966218,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Princess Dracaena, the Thirsting Tree
Debug.AddCard(69164989,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Glamour
Debug.AddCard(23434538,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
Debug.AddCard(81611932,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Moonlit Waters
Debug.AddCard(15693423,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Evenly Matched
Debug.AddCard(40366667,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Impulse
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(69164989,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Glamour
Debug.AddCard(76869711,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Konkon
Debug.AddCard(71002019,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mudan the Rikka Fairy
Debug.AddCard(69164989,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Glamour
Debug.AddCard(132308,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Princess
Debug.AddCard(25311006,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(60880471,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Hellebore the Rikka Fairy
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(71734607,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Petal
Debug.AddCard(68941332,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Sheet
Debug.AddCard(79966218,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Princess Dracaena, the Thirsting Tree
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(44994712,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Predaplant Longinephila
Debug.AddCard(1845204,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Instant Fusion
Debug.AddCard(78646298,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Black Princess
Debug.AddCard(89176044,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Predaprimitive
Debug.AddCard(71002019,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mudan the Rikka Fairy
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(40366667,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Impulse
Debug.AddCard(40366667,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Impulse
Debug.AddCard(81611932,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Rikka Moonlit Waters
--Your Extra Deck
Debug.AddCard(66309175,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Predaplant Ambulomelides
Debug.AddCard(82370493,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Predaplant Daredevil
Debug.AddCard(11765832,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Garura, Wings of Resonant Life
Debug.AddCard(41209827,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Starving Venom Fusion Dragon
Debug.AddCard(89851827,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Secreterion Dragon
Debug.AddCard(66787942,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Predaplant Bal Teah
Debug.AddCard(3828844,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Rikka Queen Strenna
Debug.AddCard(6284176,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Kanzashi the Rikka Queen
Debug.AddCard(20477370,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Rikka Sacred Queen Strenna
Debug.AddCard(95239444,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Orea, the Sylvan High Arbiter
Debug.AddCard(33779875,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Teardrop the Rikka Queen
Debug.AddCard(33779875,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Teardrop the Rikka Queen
Debug.AddCard(9349094,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Sacred Tree Beast, Hyperyton
Debug.AddCard(94078362,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Teardrop the Rikka Sacred Queen
Debug.AddCard(21200905,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Aromaseraphy Jasmine
--Your hand traps already used on her turn
Debug.AddCard(42141493,0,0,LOCATION_GRAVE,0,POS_FACEUP) --Mulcharmy Fuwalos
--Her board
Debug.AddCard(79791878,1,1,LOCATION_SZONE,1,POS_FACEUP) --Shining Sarcophagus
Debug.AddCard(47330808,1,1,LOCATION_MZONE,3,POS_FACEUP_ATTACK,true) --Hapi, Guidance of Horus
Debug.AddCard(11335209,1,1,LOCATION_MZONE,1,POS_FACEUP_ATTACK,true) --Duamutef, Blessing of Horus
Debug.AddCard(74725513,1,1,LOCATION_MZONE,2,POS_FACEUP_ATTACK,true) --Qebehsenuef, Protection of Horus
Debug.AddCard(84941194,1,1,LOCATION_MZONE,0,POS_FACEUP_ATTACK,true) --Imsety, Glory of Horus
Debug.AddCard(16528181,1,1,LOCATION_SZONE,0,POS_FACEUP) --King's Sarcophagus
Debug.AddCard(78679226,1,1,LOCATION_SZONE,2,POS_FACEDOWN) --Future Silence
Debug.AddCard(26984177,1,1,LOCATION_FZONE,0,POS_FACEUP) --Walls of the Imperial Tomb
--Her hand
Debug.AddCard(99307040,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Horus the Black Flame Deity
Debug.AddCard(14558127,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(94145021,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(46986414,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Dark Magician
--Her Deck
Debug.AddCard(2501624,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magician Girl the Magician's Apprentice
Debug.AddCard(97526666,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Planet Pathfinder
Debug.AddCard(79791878,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Shining Sarcophagus
Debug.AddCard(92110878,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Gadget Trio
Debug.AddCard(65726770,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Silent Magician Zero
Debug.AddCard(22283204,1,1,LOCATION_DECK,0,POS_FACEDOWN) --The Gaze of Timaeus
Debug.AddCard(53129443,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Hole
Debug.AddCard(26984177,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Walls of the Imperial Tomb
Debug.AddCard(22283204,1,1,LOCATION_DECK,0,POS_FACEDOWN) --The Gaze of Timaeus
Debug.AddCard(78679226,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Future Silence
Debug.AddCard(84941194,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Imsety, Glory of Horus
Debug.AddCard(78679226,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Future Silence
Debug.AddCard(41350417,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magical Curtain
Debug.AddCard(16528181,1,1,LOCATION_DECK,0,POS_FACEDOWN) --King's Sarcophagus
Debug.AddCard(94145021,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(97526666,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Planet Pathfinder
Debug.AddCard(25311006,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(24299458,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Forbidden Droplet
Debug.AddCard(26984177,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Walls of the Imperial Tomb
Debug.AddCard(342673,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magician the Magician of Black Magic
Debug.AddCard(52038441,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Ghost Mourner & Moonlit Chill
Debug.AddCard(35269904,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Thrust
Debug.AddCard(14558127,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(23434538,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
Debug.AddCard(16528181,1,1,LOCATION_DECK,0,POS_FACEDOWN) --King's Sarcophagus
Debug.AddCard(84941194,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Imsety, Glory of Horus
Debug.AddCard(97526666,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Planet Pathfinder
Debug.AddCard(2501624,1,1,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magician Girl the Magician's Apprentice
--Her Extra Deck
Debug.AddCard(37818794,1,1,LOCATION_EXTRA,0,POS_FACEDOWN) --Red-Eyes Dark Dragoon
Debug.AddCard(37818794,1,1,LOCATION_EXTRA,0,POS_FACEDOWN) --Red-Eyes Dark Dragoon
Debug.AddCard(37818794,1,1,LOCATION_EXTRA,0,POS_FACEDOWN) --Red-Eyes Dark Dragoon
Debug.AddCard(59400890,1,1,LOCATION_EXTRA,0,POS_FACEDOWN) --Dark Magician of Destruction
Debug.AddCard(59400890,1,1,LOCATION_EXTRA,0,POS_FACEDOWN) --Dark Magician of Destruction

Debug.ReloadFieldEnd()
Debug.ShowHint("Win within 2 of your turns.")
