"""
DAY - 3  GAME  Treasure Island
Auth : o.satish kumar
"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island....")
print("Your mission is to find the treasure.")

step_1 = input("Enter which direction would you travel (left Or right) :").lower()

if step_1 == "left":
    print("You are fell in Dung !")
    print("You Game Over !")
    print("Better luck next time..")
elif step_1 == "right":
    print("You are reached to river.")
    step_2 = input("you can Swim or Wait for a Boat (Swim or Boat):").lower()
    if step_2 == "Swim":
        print("crocodiles are in River ! ")
        print("You Game Over !")
        print("Better luck next time..")
    elif step_2 == "Boat":
        print("you get in to the Boat")
        print("-------------------------")
        print("Your are react to the Dark forest")
        step_3 = input("Enter which direction would you travel (left Or right) :").lower()
        if step_3 == "right":
            print("You are eat by lion !")
            print("Your Game Over !")
            print("Better luck next time..")
        elif step_3 == "left":
            print("Your reached to the final stage... ")
            print("**************************\n"
                  "****************************\n"
                  "********************************")
            print("Your reached to Cave")
            step_4 = input("Enter which Door will open (red, blue, yellow):").lower()
            if step_4 == "red":
                print("You got a Snake bite.!..")
                print("Your Game Over !")
                print("Better luck next time..")
            elif step_4 == "yellow":
                print("You cursed by a ghost !.....")
                print("Your Game Over !")
                print("Better luck next time..")
            elif step_4 == "blue":
                print("You Win!.....")
                print("You Got the this : ")
                print('''
                *******************************************************************************
                          |                   |                  |                     |
                 _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                          |                `"=._o`"=._      _`"=._                     |
                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/_____ /
                *******************************************************************************
                ''')


