print("Let's start!")
WhatFocused=0
wantToStart=input("do you want to start y/n: ")
flower1Grow=1
flower2Grow=1
Coins=0



print("'Help' for help")

if wantToStart == "y":

    while True:
        for i in range(10):
            print("")
        Operation=input("your opreation: ")

# 0 = flower1
# 1 = flower2
# not added:
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
            print(" 'exit' to exit")
        if Operation == "help":
            print(" 'a' to move to the left")
            print(" 'd' to move to the right ")
            print(" 'c' to collect plants")
            print(" 'z' to check Coins ")
            print(" 's' to save")
            print(" 'o' to open")
            print(" 'exit' to exit")
#movement       
        if Operation == "d":
            if WhatFocused < 4:
                WhatFocused=WhatFocused+1
            Operation = ""
        
        if Operation == "a":
            if WhatFocused > 0:
                WhatFocused=WhatFocused-1
            Operation = ""
#operations
        if Operation == "c":
            if WhatFocused == 0:
                if int(flower1Grow) >= 50:
                    flower1Grow=int(flower1Grow)
                    flower1Grow=int(flower1Grow)-50
                    Coins=int(Coins)
                    Coins=int(Coins)+1
            elif WhatFocused ==1:
                if int(flower2Grow) >= 50:
                    flower2Grow=int(flower2Grow)
                    flower2Grow=int(flower2Grow)-50
                    Coins=int(Coins)
                    Coins=int(Coins)+1
            else:
                print("YOU ARE NOT FOCUSING FLOWER")
        if Operation == "z":
            print("")
            print("Coins Count:",Coins)
        if Operation == "exit":
            exit()
#world management        
        
        if Operation == "s":
            FileName=input("how you want you save to be called?: ")
            f = open(FileName, "a")
            f.write(str(Coins))
            f.write("\n")
            f.write(str(flower1Grow))
            f.write("\n")
            f.write(str(flower2Grow))
            f.write("\n")
            f.close()         
        if Operation == "o":
            FileNameOpen=input("name of the save: ")
            f = open(FileNameOpen)
            Coins=f.readline()
            flower1Grow=f.readline()
            flower2Grow=f.readline()         
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
            print("Fancy third flower/not added yet") 
        
        if WhatFocused == 3:
            print("")
            print("this feature is not added")
        
        if WhatFocused == 4:
            print("")            
            print("this feature is not added")
#grow           
        if int(flower1Grow)<50:
            flower1Grow=flower1Grow+1
        if int(flower2Grow)<50:
            flower2Grow=flower2Grow+1
#what Focused
        print("")
        print("Focuse", WhatFocused)

#game management
elif wantToStart == "n":
    print("...")
    exit()
else:
    print("WRONG OPERATION!!!")