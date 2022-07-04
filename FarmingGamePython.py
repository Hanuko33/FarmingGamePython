#libs
import pyglet
#from pyglet.window import key
#from pyglet.window import mouse
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


cls()



#music
music = pyglet.resource.media('music1.wav')
music.play()

#setting variables
WhatFocused=0
flower1Grow=1
flower2Grow=1
Coins=0
power=100
Seeds=0
Flower3grow=0
SeedPower=0

wantToStart=input("do you want to start y/n: ")

if wantToStart == "y":
    print("'Help' for help")
    while True:

        Operation=input("your operation: ")
        cls()

#Help
        if Operation == "Help":
            print(" If your power runs out you will die so remember to sleep!")
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
            print(" If your power runs out you will die so remember to sleep!")
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
            else:
                print("You can't go that way!")
            #Operation = ""
        
        if Operation == "a":
            if WhatFocused > 0:
                WhatFocused=WhatFocused-1
                power=int(power)
                power=power-1
            else:
                print("You can't go that way!")
            #Operation = ""
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
    #coins amount
        if Operation == "z":
            print("")
            print("Coins amount:",Coins)
    #seeds amount
        if Operation == "cs":
            print("")
            print("Seeds amount:", Seeds)
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
                print("when you sleept flowers grew. You can now harvest them!")
                flower1Grow=int(flower1Grow)
                flower2Grow=int(flower2Grow)
                flower1Grow=50
                flower2Grow=50
                if SeedPower >= 1:
                    Flower3grow=Flower3grow+SeedPower
                    SeedPower=0
    #shopInteraction
        if Operation == "is":
            Coins=int(Coins)
            if WhatFocused == 3:
                Operation = ""
                print("Shop: Hello! What do you want to buy?")
                print("to say goodbye: Goodbye")
                print("to buy seed (for fancy flower) type: I want to buy seed")
                ShopDecision=input("Your decision: ")
                if ShopDecision=="I want to buy seed":
                    print("Shop: That's 5 Coins.")
                    YesOrNo=input("Y/N: ")
                    if YesOrNo=="Y":
                        if Coins >= 5:
                            Coins=Coins-5
                            print("Here you go. *hands the seed *you are not interacting with shop anymore")
                            Seeds=Seeds+1
                            print("You now have", Seeds, "Seed")
                        else:
                            print("Shop: It's not enough coins to buy seed! *you are not interacting with shop anymore")
                    elif YesOrNo=="N":
                        print("Shop: OK.")
                    else:
                        print("Shop: What? *you are not interacting with shop anymore")
                elif ShopDecision=="Goodbye":
                    print("Shop: Goodbye! Have a nice day!")
                else:
                    print("Shop: What do you mean? *you are not interacting with shop anymore")
            else:
                print("Your focus is not on shop!")
    #Flower3
        if Operation == "p":
            if Seeds >= 1:            
                Seeds=Seeds-1
                SeedPower=SeedPower+50
                print("Your flower should grow")
            else:
                print("You don't have any seeds!")
            

#world management        
        
        if Operation == "s":
            FileName=input("how you want you save to be called? Don't overwrite files beacuse this can break your save: ")
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
            flower1Grow=int(flower1Grow)
            flower2Grow=int(flower2Grow)
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
            print("Your focus is on: First flower")
            print("flower grow:",flower1Grow, "/ 50")
            if flower1Grow == 50:
                print("You can harvest this flower by typing 'c' ")
        
        if WhatFocused == 1:
            print("")
            print("Your focus is on: Second flower")
            print("flower grow:",flower2Grow, "/ 50")
            if flower2Grow == 50:
                print("You can harvest this flower by typing 'c' ")
                            
        if WhatFocused == 2:
            print("")
            print("Your focus is on: Fancy third flower")
            print("Seed Power: ",SeedPower) 
            print("flower grow:", Flower3grow)
            
            if Flower3grow >= 150:
                print("You can harvest this flower THREE TIMES (using 'c')")
            elif Flower3grow >= 100:
                print("You can harvest this flower TWICE (using 'c')")
            elif Flower3grow >= 51:
                print("This flower is overgrown you may need to collect it few times")
            elif Flower3grow >= 50:
                print("You can harvest this flower by typing 'c' ")
            
            
            if SeedPower == 0:
                print("Third flower isn't growing beacuse it need seed that you can get from shop")
        
        if WhatFocused == 3:
            print("")
            print("Your focus is on: Shop | 'is' to interact with shop")
        
        if WhatFocused == 4:
            print("")            
            print("Your focus is on: Sleep place | 'n' to take a nap")
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
        
#what happen
        print("")
        print("What happened:")
       
        if Operation=="a":
            print("You tried to go left")
        
        if Operation=="d":
            print("You tried to go right")
        
        if Operation=="z":
            print("You checked your coins amount")
        
        if Operation=="help":
            print("You checked help")
        
        if Operation=="Help":
            print("You checked help")
        
        if flower1Grow <= 49:
            print("First flower grew")
        
        if flower2Grow <= 49:
            print("First flower grew")
        
        if SeedPower >= 1:
            print("Third flower grew")
        print("You got tired")
        
        if Operation=="":
            print("You did nothing (you waited)")
        if Operation==" ":
            print("You did nothing (you waited)")    
        if Operation=="c":
            print("You tried to collect flower")
        if Operation=="p":
            print("You tried to plant flower")
            
            
        print("")       
#power
        
        power=int(power)
        power=int(power)-1
        if power <= 0:
            print("You died")
            exit()

#game management
elif wantToStart == "n":
    exit()
else:
    print("Wrong operation!")
