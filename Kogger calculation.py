#MR Equation (100/(100+MR)) or 2 - (100/(100+MR))
#  MR = MR * .65 if void staff is present
#Damage = ((Base dmg + Ratio)[*Missing HP mult]*MR Multiplier
#Current HP = Total HP - Damage
#Liandrys Burn = 2%current hp per second (x2)
#Q - 80/130/180/230/280 (50% AP) [20/22/24/26/28% Shred]
#E - 60/110/160/210/260 (70% AP)
#R - 100/140/180 (25% AP) | 200/280/360 (50% AP) <= Execute (below 40% HP)
#Generate results for 30, 40, 50, 75, 100, 150, 200, MR
#Ashe HP 528-1871 (1221 at 11) 30 MR
#Alistar HP 613-2415 (1544 at 11) +1.25 Mr per level (43 at 11)

def Barrage

print("Scenario 1: Level 11, Optimal Target (1221hp)")
print("Build 1: Tear, Rylais, Sorc Boots, Chalice")
Barrage (1221, 100, 32, 140, 1)

def Barrage (Health, AP, Mpen, Base, MRignore):
    #Health = 1221 #Targets HP
    HP = []
    for i in range(0,7):
        HP.append(Health)
    #AP = 100
    #Mpen = 32 
    #Base = 140 #Ult base damage
    MRmult = 1 #How much damage we are actually doing to target
    Hpcount = 0 #is this 30, 40, 50 etc
    #MRignore = 1 #Multiplier if there is MR to ignore
    MRActual = 0

    for shot in range(1,6):
        Missinghp = Health - HP[Hpcount]
        Missingmult = Missinghp/Health
        Missingmult = .83 * Missingmult
        tmp = "Shot {0}:"
        print(tmp.format(shot))
        #For each stage of MR
        for i in range(30,201,10):
            if (i > 50 and i < 70) or (i > 70 and i < 100) or (i > 100 and i < 150) or (i > 150 and i < 200):
                continue #Only keep the important ones
            #Lets get into the actual calculations!
            ExecuteFlag = 0
            Current = HP[Hpcount]
            MR = i
            MR = MR * MRignore #Change only if voidstaff or Q is present
            MR = MR - Mpen
            MRActual = MR
            if MR >= 0:
                MRmult = 100.0/(100+MR)
            else: #Negative MR
                MRmult = 2-(100.0/(100+MR))

            if (Current/Health > .4):
                Damage = (Base + (AP*.25))*(1+Missingmult)*MRmult
            else: #Execute
                Damage = (Base*2 + (AP*.5))*MRmult
                ExecuteFlag = 1
                
            Damage = round(Damage)

            HP[Hpcount] = HP[Hpcount] - Damage
            tmp = "MR:{0}({3}) | Damage:{1} | Remaining: {2} {4} [Dealt:{5}]"
            if HP[Hpcount] <= 0:
                filler = "dead"
            else:
                filler = HP[Hpcount]
            exfiller = ""
            if ExecuteFlag == 1:
                exfiller = "!"
            else:
                exfiller = ""
            print (tmp.format(i,Damage,filler, MRActual, exfiller, Health-HP[Hpcount]))
            Hpcount = Hpcount + 1
        Hpcount = 0

