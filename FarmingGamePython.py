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
# 2 = paid flower
# not added:
# 3 = shop
# 4 = sleep 





        if Operation == "Help":
            print("a(left)d(right) for movement ")
            print("'c' to collect plants")
            print("'z' to check coins ")
            print(" s to save")
            print(" o to open")
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
                if flower1Grow == 50:
                    flower1Grow=1
                    Coins=Coins+1
            elif WhatFocused ==1:
                if flower2Grow == 50:
                    flower2Grow=1
                    Coins=Coins+1
            else:
                print("YOU ARE NOT FOCUSING FLOWER")
        if Operation == "z":
                print("Coins Count:",Coins)
                
        if Operation == "s":
            FileName=input("how you want you save to be called?: ")
            f = open(FileName, "a")
            f.write(str(Coins))
            f.close()         
        if Operation == "o":
            FileNameOpen=input("name of the save: ")
            f = open(FileNameOpen)
            Coins=f.readline()
            print(Coins)          
#focus
        if WhatFocused == 0:
            print("")
            print("you are focusing flower")
            print("flower grow:",flower1Grow)
        
        if WhatFocused == 1:
            print("")
            print("you are focusing flower")
            print("flower grow:",flower2Grow)
        if WhatFocused == 2:
            print("")
            print("you are focusing flower that is blocked rn") 
        
        if WhatFocused == 3:
            print("")
            print("this feature is not added YET")
        
        if WhatFocused == 4:
            print("")            
            print("this feature is not added YET")
#grow           
        if flower1Grow<50:
            flower1Grow=flower1Grow+1
        if flower2Grow<50:
            flower2Grow=flower2Grow+1
#what Focused
        print("")
        print("Focuse", WhatFocused)


elif wantToStart == "n":
    print("...")
else:
    print("WRONG OPERATION!!!")