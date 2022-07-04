print("Let's start!")
WhatFocused=0
wantToStart=input("do you want to start y/n: ")
flower1Grow=1
flower2Grow=1
Coins=0
power=100
Seeds=0
Flower3grow=0
SeedPower=0

print("'Help' for help")



if wantToStart == "y":

    while True:
        for i in range(10):
            print("")
        Operation=input("your operation: ")

# 0 = flower1
# 1 = flower2
# 2 = Fancy flower3
# 3 = shop
# 4 = sleep 




#Help
        if Operation == "Help":
            print(" 'a' to move to the left")
            print(" 'd' to move to the right ")
            print(" 'c' to collect plants")
            print(" 'z' to check Coins ")
            print(" 's' to save")
            print(" 'o' to open")
            print(" 'n' to take a nap")
            print(" 'is' to interact with shop")
            print(" 'p' to plant seed to Fancy flower")
            print(" 'cs' to check seeds amount")
            print(" 'exit' to exit")
        if Operation == "help":
            print(" 'a' to move to the left")
            print(" 'd' to move to the right ")
            print(" 'c' to collect plants")
            print(" 'z' to check Coins ")
            print(" 's' to save")
            print(" 'o' to open")
            print(" 'n' to take a nap")
            print(" 'is' to interact with shop")
            print(" 'p' to plant seed to Fancy flower")
            print(" 'cs' to check seeds amount")
            print(" 'exit' to exit")
#movement       
        if Operation == "d":
            if WhatFocused < 4:
                WhatFocused=WhatFocused+1
                power=int(power)
                power=power-1
            Operation = ""
        
        if Operation == "a":
            if WhatFocused > 0:
                WhatFocused=WhatFocused-1
                power=int(power)
                power=power-1
            Operation = ""
#operations
    #flower collecting
        if Operation == "c":
            if WhatFocused == 0:
                if int(flower1Grow) >= 50:
                    flower1Grow=int(flower1Grow)
                    flower1Grow=int(flower1Grow)-50
                    Coins=int(Coins)
                    Coins=int(Coins)+1
                    power=int(power)
                    power=int(power)-10
            elif WhatFocused ==1:
                if int(flower2Grow) >= 50:
                    flower2Grow=int(flower2Grow)
                    flower2Grow=int(flower2Grow)-50
                    Coins=int(Coins)
                    Coins=int(Coins)+1
                    power=int(power)
                    power=int(power)-10
            elif WhatFocused == 2:
                if Flower3grow >= 50:
                    Flower3grow=Flower3grow-50
                    Coins=int(Coins)
                    Coins=Coins+25
            else:
                print("YOU ARE NOT FOCUSING FLOWER")
    #coins count
        if Operation == "z":
            print("")
            print("Coins Count:",Coins)
    #seeds count
        if Operation == "cs":
            print("")
            print("Seeds Count:", Seeds)
    #exit
        if Operation == "exit":
            exit()
    #nap
        if Operation == "n":
            if WhatFocused == 4:
                print("you went to sleep")
                power=int(power)
                power=int(power)+100
                print("you woke up and you have ", power, " power")
                flower1Grow=int(flower1Grow)
                flower2Grow=int(flower2Grow)
                flower1Grow=flower1Grow+50
                flower2Grow=flower2Grow+50
    #shopInteraction
        if Operation == "is":
            Coins=int(Coins)
            if WhatFocused == 3:
                Operation = ""
                print("Shop: Hello! What do you want to buy?")
                print("to say goodbye: Goodbye")
                print("to buy seed (for fancy flower) type: I want to buy seeds")
                ShopDecision=input("Your decision: ")
                if ShopDecision=="I want to buy seeds":
                    print("Shop: That's 5 Coins.")
                    YesOrNo=input("Y/N: ")
                    if YesOrNo=="Y":
                        if Coins >= 5:
                            Coins=Coins-5
                            print("Here you go. *hands the seeds")
                            Seeds=Seeds+1
                    elif YesOrNo=="N":
                        print("Ok I understand ill try to lower the prices later =).")
                    else:
                        print("Shop: What?")
                elif ShopDecision=="Goodbye":
                    print("Shop: Goodbye! Have a nice day!")
            else:
                print("Why are you trying to talk to plants / bed?")
    #Flower3
        if Operation == "p":
            if Seeds >= 1:            
                isThirdFlower=True
                Seeds=Seeds-1
                SeedPower=50
            

#world management        
        
        if Operation == "s":
            FileName=input("how you want you save to be called?: ")
            f = open(FileName, "w")
            f.write(str(Coins))
            f.write("\n")
            f.write(str(flower1Grow))
            f.write("\n")
            f.write(str(flower2Grow))
            f.write("\n")
            f.write(str(power))
            f.write("\n")
            f.write(str(Seeds))
            f.write("\n")
            f.write(str(Flower3grow))
            f.write("\n")
            f.write(str(SeedPower))
            f.write("\n")
            f.close()         
        if Operation == "o":
            FileNameOpen=input("name of the save: ")
            f = open(FileNameOpen)
            Coins=f.readline()
            flower1Grow=f.readline()
            flower2Grow=f.readline()
            power=f.readline()
            Seeds=f.readline()
            Seeds=int(Seeds)
            Flower3grow=f.readline()
            Flower3grow=int(Flower3grow)
            SeedPower=f.readline()
            SeedPower=int(SeedPower)
#focus
        if WhatFocused == 0:
            print("")
            print("First flower")
            print("flower grow:",flower1Grow)
        
        if WhatFocused == 1:
            print("")
            print("Second flower")
            print("flower grow:",flower2Grow)
        if WhatFocused == 2:
            print("")
            print("Fancy third flower")
            print("Seed Power: ",SeedPower) 
            print("flower grow:", Flower3grow)
        
        if WhatFocused == 3:
            print("")
            print("SHOP")
        
        if WhatFocused == 4:
            print("")            
            print("Sleep place")
#grow           
        if int(flower1Grow)<50:
            flower1Grow=int(flower1Grow)
            flower1Grow=flower1Grow+1
        if int(flower2Grow)<50:
            flower2Grow=int(flower2Grow)
            flower2Grow=flower2Grow+1
        if SeedPower>=1:
            Flower3grow=Flower3grow+1
            SeedPower=SeedPower-1
#how much power
        print("")
        print("power:", power)
        print("")


#what Focused
        print("")
        print("Focused", WhatFocused)
        
#power
        
        power=int(power)
        power=int(power)-1
        if power <= 0:
            print("You died")
            exit()

#game management
elif wantToStart == "n":
    print("...")
    exit()
else:
    print("WRONG OPERATION!!!")