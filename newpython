import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
layout = 0
flashlight = 0

required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

print("""As the bus comes to a halt, you step off to enter a new life. There's only a few states left without a warrent out for you, and . Has prison reformed you from your old ways?\n\n""")


#The story is broken into sections, starting with "intro"
#When you see def name() it means you are defining a function which you will later call
def intro():
    choice = input("Convicts have it hard after time. Life doesn't provide free rent, and you still haven't paid back some dangerous people. Will you resort back to crime to pay off old debts?\n >>> ")
    time.sleep(1) #this just means you are including a pause
    print("\n")
    if choice in yes: #see arrays above
        print("I heard the old man who lives near the old drop off site doesn't have protection, and at night, people don't pass by.\n")
    elif choice in no:
        print ("\n Then continue struggling with rent"
        "\n\nKeep in mind, however, crime is always there.")
        raise SystemExit #This will exit the program and bring you back to command line

def learn_more():
  print ("""Your brother, still into crime, tells you more about the old man. The old man is closing in on 70 and that he is holding near 200 grand in jewelry, but the word is that he works for your old employer.  Do you: """)
  time.sleep(1)
  choice2 = input("""
    A. Begin planning with your brother
    B. Screw your brother over and do it without him
    C. Have faith in prison and don't turn bad\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("He will scout the place and begin writing up a schedule. You will go find the equipment required.")
  elif choice2 in answer_B:
        print("Your b...\n")
        raise SystemExit
  elif choice2 in answer_C:
        print ("\n Then continue struggling with rent"
        "\n\nKeep in mind, however, crime is always there.")
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        learn_more()
    #option_rock()

def appointment():
    print("""  \When are we hitting the place?""")
    time.sleep(1)
    choice3 = input("""
    A. Next Friday
    B. Next Week
    C. I'm not sure, What would be a good time?\n
    >>> """)
    print("\n")
    if choice3 in answer_A:
          print("Your brother says: I'm not sure next friday's a good time\n")
          time.sleep(0.5)
          print("""Yeah Friday may be a bad time, it may be really busy.\n""")
          layout()
    elif choice3 in answer_B:
          print("""What if we get caught \n""")
          raise SystemExit
    elif choice3 in answer_C:
          print("You're delusional and wasting our time.\n")
          time.sleep(1)
          terrestrial()
          raise SystemExit
    else:
          print(required)
          time.sleep(1)
          appointment()

def layout():
    print("Pssssst...\n")
    time.sleep(0.75)
    print("Huh?\n")
    time.sleep(0.75)
    print("""You turn around and find a mousy looking woman with oversized spectacles
staring back at you.\n""")
    time.sleep(0.75)
    print("What do you want?\n")
    time.sleep(0.75)
    print("""The woman tells you that you're not delusional and quickly presses
a layout of the house into your hand, before scurrying away
at the sound of approaching footsteps.\n""")
    choice4 = input("""Do you leave the layout at your house, or do you put it in your pocket?\n
    A. Leave the layout because you dumb
    B. Quickly put the layout in your pocket, and prepare to face
    the approaching footsteps\n
    >>> """)
    print("\n")
    if choice4 in answer_A:
        print("You're pretty lazy. Do you have the nerve to rob the man?\n")
        raise SystemExit
    elif choice4 in answer_B:
        print("Smart move, that layout is going to become very important.\n")
    else:
          print(required2)
          layout()

def coffeeshop():
    print("""The lady seemed familiar, but you cannot seem to remember from where. Anyway, do you tell your brother about the layout? .\n""")
    time.sleep(0.75)
    choice5 = input("""Do you tell your brother about the layout?
    A. No, because you want all of the money to yourself
    B. Yes, because you are not heartless, but you won't be able to keep all of the money to yourself
    >>> """)
    print("\n")
    if choice5 in answer_A:
        print("Your brother sees the transaction and questions you about if\n")
        raise SystemExit
    elif choice5 in answer_B:
        print("Your brother says that in the layout, the best spot to break in is near the basement antrance\n")
    else:
          print(required2)
          layout()


