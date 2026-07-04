import random

inventory=list()

def room1(health):
    print("\nEntered Room 1\n")
    option1=int(input("You see a locked door\n1.Search the room\n2.kick the door"))
    if option1==1:
        inventory.append("key")

    else:
        health-=15

    print("Door unlocked")
    print("updated inventory:",inventory)
    print("remaining health:",health)
    return health

def room2(health):
    if health<=0:
        print("Game Over")
    else:
        print("\nEntered Room 2\n")
        option2=int(input("You see a locked chest\n1.Search the chest\n2.ignore the chest"))
        if option2==1:
            luck=random.randint(1,2)
            if luck==1:
                inventory.append("SWORD")
                print("Congrats You Found a Sword")
            else:
                print("Its a trap!\nlose 25 health")
                health-=25
        elif option2==2:
            print("Chest ignored")
        print("updated inventory:",inventory)
        print("remaining health:",health)
    return health

def room3(health):
    print("\nEntered Room 3\n")
    if health<=0:
        print("Game Over")
    elif "SWORD" in inventory:
        print("You defeated the monster with a sword")
    else:
        print("You dont have the sword to defeat the monster!\nlose 40 health")
        health-=40
    print("updated inventory:",inventory)
    print("remaining health:",health)
    return health


def room4(health):
    if health<=0:
        print("Game Over")
    else:
        print("\nentered Room 4\n")
        if "key" in inventory:
            print("Final door unlocked")
            print("Congrats You Escaped succesfully")
        else:
            print("key not found in inventory\nUnable to open the door")
            print("Game Over")
    return health



def escape_room():

    print("Welcome to the escape room.")
    print("solve the 4 upcoming doors to escape the room")
    health=100
    health=room1(health)
    health=room2(health)
    health=room3(health)
    health=room4(health)

escape_room()


