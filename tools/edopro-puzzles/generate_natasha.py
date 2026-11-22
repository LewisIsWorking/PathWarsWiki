import json,random,zipfile,glob,os
D='natasha_practice'; os.makedirs(D,exist_ok=True)
ID={k:v[0] for k,v in json.load(open('ids.json')).items()}
DECKS={
"Yummy":({"Droll & Lock Bird":2,"Magicians' Souls":1,"Cooky☆Yummy":3,"Cupsy☆Yummy":1,"Lollipo☆Yummy":3,"Marshmao☆Yummy":2,'Maxx "C"':1,"Ash Blossom & Joyous Spring":3,"Witch of the Black Forest":1,"Mulcharmy Fuwalos":2,"Mind on Air":1,"Dark Magician, the Pharaoh's Servant":1,"Illusion of Chaos":1,"Triple Tactics Talent":2,"Piri Reis Map":3,"Yummyusment★Acroquey":1,"Yummyusment☆Mignon":1,"Crossout Designator":1,"The Gaze of Timaeus":1,"Yummy☆Surprise":1,"Dark Magical Curtain":3,"Infinite Impermanence":3,"Dominus Spark":3},
 ["Red-Eyes Dark Dragoon","Dark Magician of Destruction","Cooky★Yummy Way","Cupsy★Yummy Way","Lollipo★Yummy Way","Shamisen Samsara Sorrowcat","Herald of the Arc Light","Borreload Savage Dragon","Baronne de Fleur","Yummy★Snatchy","Yummy★Snatchy","Linkuriboh","Artemis, the Magistus Moon Maiden","Spright Elf","S:P Little Knight"]),
"Invoked":({"Droll & Lock Bird":2,'Maxx "C"':1,"Ghost Ogre & Snow Rabbit":2,"Ash Blossom & Joyous Spring":3,"Virakam, the Divine Spirit of Artifice":1,"Aleister the Invoker":3,"Mulcharmy Fuwalos":3,"Mulcharmy Purulia":2,"Aleister the Reminiscent":3,"Aiwass, Divine Spirit of the Law":3,"Invocation":2,"Triple Tactics Talent":1,"Sacred Spirit Sword Aiwass":3,"Magical Meltdown":3,"Super Polymerization":2,"Crossout Designator":1,'Invocation "Sword"':2,"Infinite Impermanence":3},
 ["Borreload Savage Dragon","Magistus Chorozo","Invoked Raidjin","Invoked Sorath","Invoked Baybarron","Aleister the Invoker of Madness","Invoked De Anima","Invoked Mechaba","Invoked Oceanus","Invoked Elysium","Hyperinvoked Aeon","Hyperinvoked Aeon","Baronne de Fleur","Artemis, the Magistus Moon Maiden","S:P Little Knight"]),
}
def add(name,owner,loc,seq=0,pos="POS_FACEDOWN",proc=False):
    return f'Debug.AddCard({ID[name]},{owner},{owner},{loc},{seq},{pos}{",true" if proc else ""}) --{name}'
board=["--Her monsters: Dragoon + all 4 Sons of Horus",
 add("Red-Eyes Dark Dragoon",1,"LOCATION_MZONE",5,"POS_FACEUP_ATTACK",True),
 add("Imsety, Glory of Horus",1,"LOCATION_MZONE",0,"POS_FACEUP_ATTACK",True),
 add("Duamutef, Blessing of Horus",1,"LOCATION_MZONE",1,"POS_FACEUP_ATTACK",True),
 add("Qebehsenuef, Protection of Horus",1,"LOCATION_MZONE",2,"POS_FACEUP_ATTACK",True),
 add("Hapi, Guidance of Horus",1,"LOCATION_MZONE",3,"POS_FACEUP_ATTACK",True),
 "--Her Spells/Traps",
 add("King's Sarcophagus",1,"LOCATION_SZONE",0,"POS_FACEUP"),
 add("Shining Sarcophagus",1,"LOCATION_SZONE",1,"POS_FACEUP"),
 add("Future Silence",1,"LOCATION_SZONE",2,"POS_FACEDOWN"),
 add("Walls of the Imperial Tomb",1,"LOCATION_FZONE",0,"POS_FACEUP"),
 "--Her hand: Horus the Black Flame Deity waits for a Son to leave the field",
 add("Horus the Black Flame Deity",1,"LOCATION_HAND"),
 add("Ash Blossom & Joyous Spring",1,"LOCATION_HAND"),
 add("Droll & Lock Bird",1,"LOCATION_HAND"),
 add("Dark Magician",1,"LOCATION_HAND"),
 "--Her GY"]+[add(n,1,"LOCATION_GRAVE",0,"POS_FACEUP") for n in ["Dark Magician Girl the Magician's Apprentice","Dark Magical Curtain","The Gaze of Timaeus","Planet Pathfinder"]]+["--Her Deck"]+[add(n,1,"LOCATION_DECK") for n in ["Dark Magician","Planet Pathfinder","Planet Pathfinder","Imsety, Glory of Horus","Imsety, Glory of Horus","Shining Sarcophagus","King's Sarcophagus","King's Sarcophagus","Future Silence","Future Silence"]]
for deck,(main,extra) in DECKS.items():
    pool=[n for n,c in main.items() for _ in range(c)]
    rng=random.Random(2026112000+len(deck))
    for i in range(1,11):
        p=pool[:]; rng.shuffle(p); hand,rest=p[:6],p[6:]
        L=[f'''--[[message
Natasha practice: her Horus Dragoon end board (Dragoon + all 4 Sons, Black Flame Deity in hand) vs your {deck} deck, going 2nd. Random hand {i}/10.
Your hand: {", ".join(hand)}.
Win = deal 8000 this turn.
]]
Debug.SetAIName("Natasha (Horus Dragoon)")
Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)
Debug.SetPlayerInfo(0,8000,0,0)
Debug.SetPlayerInfo(1,8000,0,0)
''',"--Your hand"]+[add(h,0,"LOCATION_HAND") for h in hand]+["--Your Main Deck"]+[add(n,0,"LOCATION_DECK") for n in rest]+["--Your Extra Deck"]+[add(n,0,"LOCATION_EXTRA") for n in extra]+board+["","Debug.ReloadFieldEnd()",'Debug.ShowHint("Break Natasha\'s board and deal 8000 this turn.")',"aux.BeginPuzzle()"]
        open(f"{D}/Natasha_{deck}_hand{i:02d}.lua","w").write("\n".join(L)+"\n")
z=zipfile.ZipFile('Natasha_practice_puzzles_v2.zip','w')
for f in sorted(glob.glob(D+'/*.lua')): z.write(f,os.path.basename(f))
print(len(z.namelist()))
