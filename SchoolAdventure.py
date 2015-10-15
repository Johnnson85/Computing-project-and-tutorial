
import time
def vinput():
    while True:
        try:
            inp=input("Please enter a or b: ").lower()
            if inp in ["a","b"]:
                break
            else:
                print("That's not a valid number")
        except:
            print("That's not even an input!")
    
    return inp
time.sleep(1)
print("----------------School Adventure---------------")
time.sleep(1)
print("-------------------Blue Group--------------")
print("\n")
time.sleep(1)
print("You are sitting in the classroom.Your teacher annoys you.  Do you:")
time.sleep(1)
print("a) Sit quietly.")
time.sleep(1)
print("b) Punch them in the face")
x = vinput()

#Sit quietly
if x == "a":
    print("You are a good boy, well done.  GAME OVER")

#punch teacher in the face    
elif x == "b":
    print("  ")
    print("The teacher still annoys you. He is shouting at you")
    time.sleep(2)
    print("You are so furious! Do you:")

    print("a) jump out the window.")
    print("b) walk out the door")
    x = vinput()

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
        x = vinput()   
    #find window to jump out
        if x == "a":
            print("You find a window and climb out. Game over.")

    #Punch someone else in the face.
        elif x == "b":
            print("You see a possible target in the corridor.")
            time.sleep(1)
            print ("He looks very scared")
            print("What do you do now?:")
            print("a) Think twice about it and return to the classroom")
            time.sleep(1)
            print("b) Go for it!")
            x = vinput()
        #You get suspended 
            if x == "a":
                print("You go back to the classroom and the teacher suspends you.")

        #Go for it 
            elif x == "b":
                print("You went for it and missed")
                time.sleep(1)
                print ("He is very angry!")
                print("What do you do now?:")
                print("a) Throw your book at him")
                time.sleep(1)
                print("b) Run away!")
                time.sleep(1)
                x= vinput()
                if x=="a":
                    # book
                    print(" you've just ruined your class notes, the book knocked him out")
                    
                   #run away 
                elif x == "b":
                    print ("You have made yourself look like an idiot, well done!")
                    
            

        
else:
    print("That was not an option.  Game Over")


