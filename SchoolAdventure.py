print("----------------School Adventure---------------")
print("---------------Blue Group--------------")
print("\n")

print("You are sitting in the classroom.Your teacher annoys you.  Do you:")
print("a) Sit quietly.")
print("b) Punch them in the face")
x = input("Enter a or b: ")
if x == "a":
    print("You are a good boy, well done.  GAME OVER")

elif x == "b":
    print("  ")
    print("The teacher still annoys you. He is shouting at you")
    
else:
    print("That was not an option.  Game Over")
   
print("You are so furious! Do you:")
print("a) jump out the window.")
print("b) walk out the door")
x = input("Enter a or b: ")
if x == "a":
    print("you are dead. End of the game")

elif x == "b":
    print(".")
    print("What do you do now?:")
    print("a) Hide in the nearest toilet.")
    print("b) punch someone else in the face")
    x = input("Enter a or b: ")    
else:
    print("That was not an option.  Game Over")
