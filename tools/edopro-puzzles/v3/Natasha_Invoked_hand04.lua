--[[message
Natasha practice: her Horus Dragoon end board (Dragoon + all 4 Sons, Black Flame Deity in hand) vs your Invoked deck, going 2nd. Random hand 4/10 (v3: full duel, no turn limit).
Opening hand: Ash Blossom & Joyous Spring, Crossout Designator, Invocation "Sword", Aiwass, Divine Spirit of the Law, Droll & Lock Bird, Pot of Desires.
Hand traps used on her turn: Ash Blossom & Joyous Spring, Droll & Lock Bird -> she lost: Dragoon, Shining Sarcophagus.
Win = win the duel. Her AI is much weaker than Natasha: count it as a win only if you win within 2 of your turns.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)

--Your hand
Debug.AddCard(65681983,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Crossout Designator
Debug.AddCard(37432075,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Invocation "Sword"
Debug.AddCard(84288367,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(35261759,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Pot of Desires
--Your Main Deck
Debug.AddCard(63926180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
Debug.AddCard(74063034,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(86120751,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(84288367,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(35261759,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Pot of Desires
Debug.AddCard(86319972,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Gamma Summon
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(63926180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(74063034,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation
Debug.AddCard(35269904,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Thrust
Debug.AddCard(84288367,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(63926180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
Debug.AddCard(37432075,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation "Sword"
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(86120751,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(37432075,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation "Sword"
Debug.AddCard(25311006,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(25311006,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(74063034,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation
Debug.AddCard(10673071,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Virakam, the Divine Spirit of Artifice
Debug.AddCard(86120751,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(23434538,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
--Your Extra Deck
Debug.AddCard(66532962,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Magistus Chorozo
Debug.AddCard(49513164,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Raidjin
Debug.AddCard(43989315,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Sorath
Debug.AddCard(70383419,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Baybarron
Debug.AddCard(48791583,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Magellanica
Debug.AddCard(80635735,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked De Anima
Debug.AddCard(75286621,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Mechaba
Debug.AddCard(6772168,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Oceanus
Debug.AddCard(11270236,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Elysium
Debug.AddCard(33166263,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Hyperinvoked Aeon
Debug.AddCard(33166263,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Hyperinvoked Aeon
Debug.AddCard(84815190,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Baronne de Fleur
Debug.AddCard(2220237,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Secure Gardna
Debug.AddCard(60303245,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Salamangreat Almiraj
Debug.AddCard(29301450,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --S:P Little Knight
--Your hand traps already used on her turn
Debug.AddCard(14558127,0,0,LOCATION_GRAVE,0,POS_FACEUP) --Ash Blossom & Joyous Spring
Debug.AddCard(94145021,0,0,LOCATION_GRAVE,0,POS_FACEUP) --Droll & Lock Bird
--Her board pieces your hand traps didn't stop
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
