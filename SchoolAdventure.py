import time
import random
time.sleep(1)
print("----------------School Adventure---------------")
time.sleep(2)
print("-------------------Blue Group--------------")
print("\n")
time.sleep(2)
print("You are sitting in the classroom.Your teacher annoys you.  Do you:")
time.sleep(2)
print("a) Sit quietly.")
time.sleep(1)
print("b) Punch them in the face")
time.sleep(2)
x = input("Enter a or b: ")

#Sit quietly
if x == "a":
    print("You are a good boy, well done.  GAME OVER")
    
#punch teacher in the face    
elif x == "b":
    print("  ")
    print("The teacher still annoys you. He is shouting at you")
    time.sleep(2)
    
else:
    print("That was not an option.  Game Over")

   
print("You are so furious! Do you:")

print("a) jump out the window.")
print("b) walk out the door")
time.sleep(2)
x = input("Enter a or b: ")

#jump out the window
if x == "a":
    print("you are dead. End of the game")

#walk out the door
elif x == "b":
    print("you hear voices: your headteacher's voice and your teacher's")
    time.sleep(2)
    
    print("What do you do now?:")
    print("a) Hide in the nearest toilet.")
    time.sleep(1)
    print("b) punch someone else in the face")
    time.sleep(2)
    x = input("Enter a or b: ")    
else:
    print("That was not an option.  Game Over")


