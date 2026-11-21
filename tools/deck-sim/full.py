"""Resource-exchange model, going second into Rhino's HERO board and Natasha's Horus board.
Not a game engine: each card is given a role from its card text; the opponent assigns its
interruptions greedily to do the most damage, and we pick the best use of our hand traps."""
import random, collections, itertools, json, sys

DECKS = {
 "Witchcrafter": {"Effect Veiler":2,"Witchcrafter Genni":1,"Genni Maid":1,"Maxx C":1,"Potterie":1,"Terracottan":1,"Ash":3,"Pittore":1,"Schmietta":1,"Fuwalos":1,"Crowley":1,"Verre Maid":1,"Marka":3,"Haine":1,"Madame Verre":1,"Creation":3,"Spell Power Mastery":1,"Walpurgis":3,"Bystreet":1,"Super Polymerization":2,"Unveiling":3,"Lacrima":3,"Gaze":1,"Celebration":2,"Distortion":1},
 "Rikka": {"Rikka Petal":3,"Maxx C":1,"Ash":3,"Primula":1,"Rikka Princess":2,"Fuwalos":3,"Mudan":2,"Black Princess":3,"Hellebore":1,"Primrose":2,"Rikka Glamour":3,"Triple Tactics Talent":2,"Foolish Burial":1,"Moonlit Waters":2,"Rikka Konkon":2,"Fallen & Virtuous":2,"Infinite Impermanence":3,"Rikka Sheet":1,"Dominus Impulse":3},
 "Invoked": {"Droll":2,"Maxx C":1,"Ghost Ogre":2,"Ash":3,"Virakam":1,"Aleister":3,"Fuwalos":3,"Purulia":2,"Reminiscent":3,"Aiwass":3,"Invocation":2,"Triple Tactics Talent":1,"Sacred Sword Aiwass":3,"Magical Meltdown":3,"Super Polymerization":2,"Crossout":1,"Invocation Sword":2,"Infinite Impermanence":3},
 "Orcust": {"Magicians' Souls":1,"Maxx C":1,"Elzette":1,"Ash":3,"Cymbal Skeleton":1,"Harp Horror":3,"Girsu":3,"Fuwalos":3,"Purulia":1,"Orcust Knightmare":1,"Diabellstar":3,"World Wand":1,"NT8000":1,"Diabellstar Vengeance":1,"Hallowed Azamina":1,"Foolish Burial":1,"Babel":1,"Deception":1,"WANTED":1,"Crossout":1,"Gaze":1,"Infinite Impermanence":3,"Dominus Impulse":3,"Dominus Spark":3,"Crescendo":1},
}
# hand traps used on THEIR turn 1 (you go second): expected board pieces removed
HT = {"Ash":1,"Droll":1,"Infinite Impermanence":1,"Effect Veiler":1,"Ghost Ogre":1,"Dominus Impulse":1,"Dominus Spark":1,"Maxx C":.5,"Fuwalos":.5,"Purulia":.5}
# one-card starters: kind of action an interruption must hit to stop that line
STARTERS = {
 "Witchcrafter": {"Walpurgis":"search_face","Marka":"search","Creation":"search","Spell Power Mastery":"search"},
 "Rikka": {"Rikka Petal":"search","Black Princess":"deck_ss","Rikka Glamour":"search","Moonlit Waters":"search","Foolish Burial":"deck_send"},
 "Invoked": {"Aleister":"search","Reminiscent":"search","Aiwass":"search","Magical Meltdown":"search_face","Sacred Sword Aiwass":"deck_ss"},
 "Orcust": {"Girsu":"deck_send","Diabellstar":"face","WANTED":"search","Foolish Burial":"deck_send"},
}
WC_BODIES={"Witchcrafter Genni","Schmietta","Pittore","Potterie"}
WC_SPELLS={"Spell Power Mastery","Walpurgis","Bystreet","Lacrima","Super Polymerization","Gaze","Unveiling","Celebration","Creation"}
# engine removals if the combo resolves; Dark Law (Rhino) and Shining Sarcophagus / Droll (Natasha) penalties
ENGINE = {"Witchcrafter":dict(base=3,dl=1,gysarc=1,droll=1,mass=2),
          "Rikka":dict(base=3,dl=2,gysarc=1,droll=1,mass=2),
          "Invoked":dict(base=3,dl=2,gysarc=1,droll=2,mass=2),
          "Orcust":dict(base=3,dl=0,gysarc=2,droll=1,mass=2)}
HITS = {"ash":{"search","search_face","deck_ss","deck_send"}, "chaos":{"search_face","face"}, "dragoon":{"search","search_face","deck_ss","deck_send","face"}}

def starters(deck,c):
    s=[t for n,t in STARTERS[deck].items() if c[n]]
    if deck=="Witchcrafter" and any(c[b] for b in WC_BODIES) and sum(c[x] for x in WC_SPELLS)>0: s.append("deck_ss")
    return s

def outcome(deck, opp, c, ints, reserve):
    """ints: list of (interruption, target). Returns (full, partial, removals)."""
    e=ENGINE[deck]; st=starters(deck,c)
    live=list(range(len(st))); mid=0; dead_breakers=set()
    for kind,tgt in ints:
        if tgt[0]=="line" and tgt[1] in live: live.remove(tgt[1])
        elif tgt[0]=="mid": mid+= e["droll"] if kind=="droll" else (e["gysarc"] if kind=="gysarc" else 1)
        elif tgt[0]=="brk": dead_breakers.add(tgt[1])
    engine = len(live)>0
    if opp=="rhino":
        dl = reserve.get("dl_present",True)
        chaos = reserve["chaos"]; sunrise = reserve["sunrise"]
        handled_dl = not dl; perm=0
        sp=c["Super Polymerization"]
        if sp:                      # Dark Law + a Chaos into Garura/Starving Venom; can't be responded to
            if dl: dl=False; handled_dl=True
            if chaos: chaos-=1
            if sp>1:
                if chaos: chaos-=1
                elif sunrise: sunrise-=1
        if "veiler_dl" in reserve and "veiler_dl" not in dead_breakers and dl: handled_dl=True
        if "imperm_dl" in reserve and "imperm_dl" not in dead_breakers and dl: handled_dl=True
        mass = "mv" in reserve and "mv" not in dead_breakers
        if mass: handled_dl=True; chaos=0
        out = (e["base"] if (handled_dl or not dl) else e["dl"]) - mid if engine else 0
        out=max(0,out)
        if "ttt" in reserve and "ttt" not in dead_breakers: out+=1
        for _ in range(out):
            if dl: dl=False; handled_dl=True
            elif chaos: chaos-=1
            elif sunrise: sunrise-=1
        full = engine and handled_dl and chaos==0 and sunrise==0
        return (full, engine and handled_dl, out)
    else:
        mass_unhittable = c["Super Polymerization"]>0
        out = max(0, e["base"]-mid) if engine else 0
        if "ttt" in reserve and "ttt" not in dead_breakers: out+=1
        thr = 1 if (deck=="Rikka" and c["Rikka Konkon"]) else e["mass"]
        mass = mass_unhittable or (engine and out>=thr)
        return (engine and mass, engine and (mass or reserve["dragoon"]==0), out)

def opp_ints(opp, reserve):
    if opp=="rhino": return ["chaos"]*reserve["chaos"]
    L=[]
    if reserve["dragoon"]: L.append("dragoon")
    L += [i for i in ("ash","droll") if i not in reserve.get("cancelled",())]
    if reserve["sarc"]: L.append("gysarc")
    return L

def targets(deck,kind,c,reserve):
    st=starters(deck,c); T=[("none",)]
    if kind=="droll" or kind=="gysarc": return [("mid",)]
    T.append(("mid",))
    for i,t in enumerate(st):
        if t in HITS[kind]: T.append(("line",i))
    for b in ("mv","imperm_dl","ttt","dominus_dl"):
        if b in reserve and kind in ("chaos","dragoon"): T.append(("brk",b))
    return T

def worst_case(deck,opp,c,reserve):
    ints=opp_ints(opp,reserve)
    if deck=="Rikka" and c["Rikka Princess"] and starters(deck,c):
        for k in ("dragoon","chaos"):
            if k in ints: ints.remove(k); break
    chosen=[]
    for kind in ints:    # greedy: each interruption picks the target that hurts most given earlier picks
        best=None
        for t in targets(deck,kind,c,reserve):
            r=outcome(deck,opp,c,chosen+[(kind,t)],reserve)
            if best is None or r<best[0]: best=(r,t)
        chosen.append((kind,best[1]))
    return outcome(deck,opp,c,chosen,reserve)

def evaluate(deck,opp,hand):
    c=collections.Counter(hand)
    best=None
    # our choices: which hand traps to keep for our turn instead of using them on theirs
    keepables=[k for k in ("Effect Veiler","Infinite Impermanence","Dominus Impulse","Crossout","Triple Tactics Talent") if c[k]]
    for r in range(0,min(2,len(keepables))+1):
        for keep in itertools.combinations(keepables,r):
            cc=c.copy()
            for k in keep: cc[k]-=1
            phaseA=sum(HT.get(n,0)*v for n,v in cc.items())
            if deck!="Invoked": phaseA-=0  # Ghost Ogre/Droll only in Invoked
            phaseA=min(phaseA,3)
            res={}
            if opp=="rhino":
                pieces=["chaos","chaos","sunrise"]; removed=int(phaseA+random.random()*0) if False else phaseA
                n=int(removed)+ (1 if random.random()<removed-int(removed) else 0)
                pieces=pieces[n:]
                res.update(chaos=pieces.count("chaos"),sunrise=pieces.count("sunrise"),dl_present=True)
                if "Dominus Impulse" in keep: res["dl_present"]=False; res["dominus_dl"]=True
                if "Effect Veiler" in keep: res["veiler_dl"]=True
                if "Infinite Impermanence" in keep: res["imperm_dl"]=True
                if "Triple Tactics Talent" in keep: res["ttt"]=True
                if deck=="Witchcrafter" and c["Unveiling"] and (c["Madame Verre"] or c["Walpurgis"] or c["Marka"]): res["mv"]=True
            else:
                pieces=["dragoon","sarc","hapi","duamutef","qeb"]
                n=int(phaseA)+(1 if random.random()<phaseA-int(phaseA) else 0)
                left=pieces[n:]
                res.update(dragoon=int("dragoon" in left),sarc=int("sarc" in left))
                if "Crossout" in keep: res["cancelled"]=("droll",)
                if "Triple Tactics Talent" in keep: res["ttt"]=True
                if deck=="Witchcrafter" and c["Unveiling"] and (c["Madame Verre"] or c["Walpurgis"] or c["Marka"]) and res["dragoon"]:
                    res["dragoon"]=0   # Unveiling -> Madame Verre negates all her monsters incl. Dragoon
            r=worst_case(deck,opp,cc,res)
            if best is None or r>best: best=r
    return best

def run(n=40000,seed=11):
    random.seed(seed); out={}
    for deck,d in DECKS.items():
        dk=[k for k,v in d.items() for _ in range(v)]
        for opp in ("rhino","natasha"):
            R=collections.Counter()
            for _ in range(n):
                f,p,_r=evaluate(deck,opp,random.sample(dk,6))
                R["full"]+=f; R["partial"]+=p and not f; R["brick"]+= not starters(deck,collections.Counter())
            out[(deck,opp)]={k:round(100*v/n,1) for k,v in R.items() if k!="brick"}
    return out
if __name__=="__main__":
    for k,v in run().items(): print(k,v)
