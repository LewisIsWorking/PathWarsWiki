--[[message
Natasha practice: her Horus Dragoon end board (Dragoon + all 4 Sons, Black Flame Deity in hand) vs your Yummy deck, going 2nd. Random hand 4/10.
Your hand: The Gaze of Timaeus, Infinite Impermanence, Witch of the Black Forest, Triple Tactics Talent, Marshmao☆Yummy, Ash Blossom & Joyous Spring.
Win = deal 8000 this turn.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)

--Your hand
Debug.AddCard(22283204,0,0,LOCATION_HAND,0,POS_FACEDOWN) --The Gaze of Timaeus
Debug.AddCard(10045474,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(78010363,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Witch of the Black Forest
Debug.AddCard(25311006,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(10966439,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Marshmao☆Yummy
Debug.AddCard(14558127,0,0,LOCATION_HAND,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
--Your Main Deck
Debug.AddCard(10966439,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Marshmao☆Yummy
Debug.AddCard(6325660,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Spark
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(94145021,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Droll & Lock Bird
Debug.AddCard(33907039,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Piri Reis Map
Debug.AddCard(93360904,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Yummyusment★Acroquey
Debug.AddCard(6325660,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Spark
Debug.AddCard(4215180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Lollipo☆Yummy
Debug.AddCard(23434538,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Maxx "C"
Debug.AddCard(68810435,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Cooky☆Yummy
Debug.AddCard(6325660,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dominus Spark
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(66975205,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Yummyusment☆Mignon
Debug.AddCard(10045474,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(29369059,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Yummy☆Surprise
Debug.AddCard(10045474,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Infinite Impermanence
Debug.AddCard(33907039,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Piri Reis Map
Debug.AddCard(68810435,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Cooky☆Yummy
Debug.AddCard(33907039,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Piri Reis Map
Debug.AddCard(4215180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Lollipo☆Yummy
Debug.AddCard(14558127,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Ash Blossom & Joyous Spring
Debug.AddCard(31425736,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Cupsy☆Yummy
Debug.AddCard(66690411,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mind on Air
Debug.AddCard(97631303,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Magicians' Souls
Debug.AddCard(88570003,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magician, the Pharaoh's Servant
Debug.AddCard(42141493,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Mulcharmy Fuwalos
Debug.AddCard(41350417,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magical Curtain
Debug.AddCard(12266229,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Illusion of Chaos
Debug.AddCard(68810435,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Cooky☆Yummy
Debug.AddCard(41350417,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magical Curtain
Debug.AddCard(4215180,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Lollipo☆Yummy
Debug.AddCard(65681983,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Crossout Designator
Debug.AddCard(25311006,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Triple Tactics Talent
Debug.AddCard(41350417,0,0,LOCATION_DECK,0,POS_FACEDOWN) --Dark Magical Curtain
--Your Extra Deck
Debug.AddCard(37818794,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Red-Eyes Dark Dragoon
Debug.AddCard(59400890,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Dark Magician of Destruction
Debug.AddCard(67098897,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Cooky★Yummy Way
Debug.AddCard(31603289,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Cupsy★Yummy Way
Debug.AddCard(93192592,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Lollipo★Yummy Way
Debug.AddCard(46057733,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Shamisen Samsara Sorrowcat
Debug.AddCard(79606837,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Herald of the Arc Light
Debug.AddCard(27548199,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Borreload Savage Dragon
Debug.AddCard(84815190,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Baronne de Fleur
Debug.AddCard(30581601,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Yummy★Snatchy
Debug.AddCard(30581601,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Yummy★Snatchy
Debug.AddCard(41999284,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Linkuriboh
Debug.AddCard(34755994,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Artemis, the Magistus Moon Maiden
Debug.AddCard(27381364,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --Spright Elf
Debug.AddCard(29301450,0,0,LOCATION_EXTRA,0,POS_FACEDOWN) --S:P Little Knight
--Her monsters: Dragoon + all 4 Sons of Horus
Debug.AddCard(37818794,1,1,LOCATION_MZONE,5,POS_FACEUP_ATTACK,true) --Red-Eyes Dark Dragoon
Debug.AddCard(84941194,1,1,LOCATION_MZONE,0,POS_FACEUP_ATTACK,true) --Imsety, Glory of Horus
Debug.AddCard(11335209,1,1,LOCATION_MZONE,1,POS_FACEUP_ATTACK,true) --Duamutef, Blessing of Horus
Debug.AddCard(74725513,1,1,LOCATION_MZONE,2,POS_FACEUP_ATTACK,true) --Qebehsenuef, Protection of Horus
Debug.AddCard(47330808,1,1,LOCATION_MZONE,3,POS_FACEUP_ATTACK,true) --Hapi, Guidance of Horus
--Her Spells/Traps
Debug.AddCard(16528181,1,1,LOCATION_SZONE,0,POS_FACEUP) --King's Sarcophagus
Debug.AddCard(79791878,1,1,LOCATION_SZONE,1,POS_FACEUP) --Shining Sarcophagus
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
Debug.ShowHint("Break Natasha's board and deal 8000 this turn.")
aux.BeginPuzzle()
