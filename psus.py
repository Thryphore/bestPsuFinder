#Tiers (A), high priority tiers (Ahp), low priority tiers (Alp), and small form factor tiers (Asff)
tierList = {"A":[], "Ahp":[], "Alp":[], "Asff": [],
"B":[], "Bhp":[], "Blp":[],  "Bsff": [],
"C": [], "Chp":[], "Clp": [], "Csff": [],
"IGPU": [], "IGPUlp": [], "IGPUsff": []}

def psuWattage(psu): #works great for EVGA
    wattage = ''

    for character in psu:
        if character.isnumeric():
            if len(wattage) == 1 and wattage == "0":
                wattage = ""
            wattage += character
            if len(wattage) == 4:
                if int(wattage)>2000:
                    wattage = ""
                    continue
                return wattage
        if character.isnumeric() == False:
            if len(wattage) <= 2:
                wattage = ""
                continue
            if len(wattage) == 3:
                if int(wattage)<450:
                    wattage = ""
                    continue
                return wattage

def EVGA(psu):
    wattage = int(psuWattage(psu))
    if any(x in psu for x in ["n1", "n2", "w1", "w2", "w3", "bv"]) : return

    if "bt" in psu:
        tierList["IGPUlp"].append(psu)
        return

    if any(x in psu for x in ["ba", "br", "m1"]):
        tierList["Clp"].append(psu)
        return

    if any(x in psu for x in ["b5", "bq"]):
        tierList["C"].append(psu)
        return
    
    if "b2" in psu:
        tierList["Chp"].append(psu)
        return

    if "gq" in psu:
        if wattage >= 750:
            tierList["C"].append(psu)
            return

        if wattage >= 850:
            tierList["B"].append(psu)
            return

    if any(x in psu for x in ["p3", "p5", "pq"]):
        tierList["Clp"].append(psu)
        return

    if "gd" in psu:
        tierList["Blp"].append(psu)
        return

    if "gt" in psu:
        if wattage == 1300:
            tierList["Blp"].append(psu)
            return

        if wattage <= 1000:
            tierList["Bhp"].append(psu)
            return
    
    if "g5" in psu:
        tierList["Bhp"].append(psu)
        return

    if any(x in psu for x in ["b3", "g+", "ga"]):
        tierList["B"].append(psu)
        return

    if "gm" in psu:
        tierList["Bsff"].append(psu)
        return

    if "g3" in psu:
        tierList["Alp"].append(psu)
        return

    if any(x in psu for x in ["g7", "t2", "g6", "p6"]):
        tierList["Ahp"].append(psu)
        return

    if any(x in psu for x in ["g2", "p2"]):
        tierList["A"].append(psu)
        return

    else:
        print(psu, " hasn't been recorded yet")
    


corsairCX = 0
corsairHX = 0
def corsair(psu):
    global corsairCX
    global corsairHX
    wattage = int(psuWattage(psu))

    if "cv" in psu and wattage <= 550:
        tierList["IGPU"].append(psu)
        return
    
    if "cv" in psu:
        tierList["Chp"].append(psu)  #check

    if "vs" in psu:
        tierList["IGPU"]
        return
    
    if "cx" in psu:
        if corsairCX == 0:
            print("Corsair CX power supply detected. Note: Good as long as it doesn't have a green label (on the power supply itself where it says the wattage (e.g. 750) shouldn't be green)")
            corsairCX += 1
        if "modular" in psu:
            tierList["Chp"]
        else:
            tierList["Bhp"].append(psu)
        return
    
    if "rm" in psu:
        tierList["Ahp"].append(psu)
        return
    
    if "sf" in psu:
        tierList["Asff"].append(psu)
        return

    if "tx" in psu:
        tierList["A"].append(psu)
        return

    if "hx" in psu:
        if corsairHX == 0:
            print("Corsair HX(i) detected. Note: If the PSU has a blue label (meaning the place that has the wattage labeled (e.g. 750)) don't buy. These are about 10 years old, too old to safely put into a machine.")
            corsairHX += 1
        tierList["Ahp"].append(psu)
        return

    if "ax" in psu:
        if wattage == 1600:
            tierList["Ahp"].append(psu)
        else:
            tierList["Alp"].append(psu)

def printTierList():
    print("")
    print("Tier list, from best to worst (Small form factor by users discression)")
    print("")

    if tierList["Asff"]:
        print("A Tier Small Form Factor:")
        for val in tierList["Asff"]:
            print(val)
    if tierList["Ahp"]:
        print("A Tier High Priority")
        for val in tierList["Ahp"]:
            print(val)
    if tierList["A"]:
        print("A Tier")
        for val in tierList["A"]:
            print(val)
    if tierList ["Alp"]:
        print("A Tier Low Priority")
        for val in tierList["Alp"]:
            print(val)

    print("")

    if tierList["Bsff"]:
        print("B Tier Small Form Factor")
        for val in tierList["Bsff"]:
            print(val)
    if tierList["Bhp"]:
        print("B Tier High Priority")
        for val in tierList["Bhp"]:
            print(val)
    if tierList["B"]:
        print("B Tier")
        for val in tierList["B"]:
            print(val)
    if tierList ["Blp"]:
        print("B Tier Low Priority")
        for val in tierList["Blp"]:
            print(val)

    print("")

    if tierList["Csff"]:
        print("C Tier Small Form Factor")
        for val in tierList["Csff"]:
            print(val)
    if tierList["Chp"]:
        print("C Tier High Priority")
        for val in tierList["Chp"]:
            print(val)
    if tierList["C"]:
        print("C Tier")
        for val in tierList["C"]:
            print(val)
    if tierList ["Clp"]:
        print("C Tier Low Priority")
        for val in tierList["Clp"]:
            print(val)