--[[message
Natasha practice: her Horus Dragoon end board vs your Invoked deck, going 2nd. Random hand 3/10.
Your hand: Virakam, the Divine Spirit of Artifice, Super Polymerization, Ash Blossom & Joyous Spring, Ghost Ogre & Snow Rabbit, Aleister the Invoker, Sacred Spirit Sword Aiwass.
Win = deal 8000 this turn.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)

--Your hand
Debug.AddCard(10673071,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Virakam, the Divine Spirit of Artifice
Debug.AddCard(48130397,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(14558127,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(59438930,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Ghost Ogre & Snow Rabbit
Debug.AddCard(86120751,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(63926180,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
--Your Main Deck
Debug.AddCard(74063034,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation
Debug.AddCard(37432075,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation "Sword"
Debug.AddCard(23434538,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
Debug.AddCard(74063034,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation
Debug.AddCard(86120751,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(10045474,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(25311006,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(84288367,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(59438930,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ghost Ogre & Snow Rabbit
Debug.AddCard(86120751,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Invoker
Debug.AddCard(10045474,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(37432075,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Invocation "Sword"
Debug.AddCard(63926180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(63926180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Sacred Spirit Sword Aiwass
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(47679935,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magical Meltdown
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(84192580,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Purulia
Debug.AddCard(65681983,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Crossout Designator
Debug.AddCard(10045474,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(84288367,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(48130397,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Super Polymerization
Debug.AddCard(84288367,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aiwass, Divine Spirit of the Law
Debug.AddCard(57294268,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Aleister the Reminiscent
Debug.AddCard(84192580,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Purulia
--Your Extra Deck
Debug.AddCard(27548199,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Borreload Savage Dragon
Debug.AddCard(66532962,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Magistus Chorozo
Debug.AddCard(49513164,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Raidjin
Debug.AddCard(43989315,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Sorath
Debug.AddCard(70383419,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Baybarron
Debug.AddCard(97973962,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Aleister the Invoker of Madness
Debug.AddCard(80635735,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked De Anima
Debug.AddCard(75286621,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Mechaba
Debug.AddCard(6772168,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Oceanus
Debug.AddCard(11270236,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Invoked Elysium
Debug.AddCard(33166263,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Hyperinvoked Aeon
Debug.AddCard(33166263,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Hyperinvoked Aeon
Debug.AddCard(84815190,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Baronne de Fleur
Debug.AddCard(34755994,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Artemis, the Magistus Moon Maiden
Debug.AddCard(29301450,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --S:P Little Knight
--Her monsters
Debug.AddCard(37818794,1,1,LOCATION_MZONE,5,POS_FACEUP_ATTACK,true) --Red-Eyes Dark Dragoon
Debug.AddCard(84941194,1,1,LOCATION_MZONE,1,POS_FACEUP_ATTACK,true) --Imsety, Glory of Horus
Debug.AddCard(99307040,1,1,LOCATION_MZONE,2,POS_FACEUP_ATTACK,true) --Horus the Black Flame Deity
Debug.AddCard(74725513,1,1,LOCATION_MZONE,3,POS_FACEUP_DEFENSE,true) --Qebehsenuef, Protection of Horus
Debug.AddCard(11335209,1,1,LOCATION_MZONE,4,POS_FACEUP_ATTACK,true) --Duamutef, Blessing of Horus
--Her Spells/Traps
Debug.AddCard(16528181,1,1,LOCATION_SZONE,0,POS_FACEUP) --King's Sarcophagus
Debug.AddCard(79791878,1,1,LOCATION_SZONE,1,POS_FACEUP) --Shining Sarcophagus
Debug.AddCard(78679226,1,1,LOCATION_SZONE,2,POS_FACEDOWN) --Future Silence
Debug.AddCard(26984177,1,1,LOCATION_FZONE,0,POS_FACEUP) --Walls of the Imperial Tomb
--Her hand
Debug.AddCard(14558127,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(94145021,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(46986414,1,1,LOCATION_HAND,0,POS_FACEDOWN) --Dark Magician
--Her GY
Debug.AddCard(47330808,1,1,LOCATION_GRAVE,0,POS_FACEUP) --Hapi, Guidance of Horus
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
Debug.ShowHint("Break Natasha's board and deal 8000 this turn.")
aux.BeginPuzzle()
