# Import the random module for the lucky number game
import random

max_lives=3

# Display the welcome message

def intro():
    print("Welcome to Escape Room")
    print("Solve the puzzle to escape")

# Door 1: Math puzzle

def d1():
    answer1=int(input("Solve: 7*6+8="))
    if answer1==50:
        return True
    else:
        return False

# Door 2: Mystery word guessing game

def d2(attempts=2):
    tries=0
    code="mystery"
    while tries < attempts:
        answer2=input("guess the mystery word(hint:the question contains the answer):").lower()
        if answer2=="":
            continue
        if answer2==code:
            return True
        print("wrong answer Try again")
        tries+=1
    return False

# Door 3: Lucky number game

def d3():
    guess=random.randint(1,5)
    for i in range(2):
        answer3=int(input("guess the lucky number between 1 and 5:"))
        if answer3==guess:
            return True
    return False

# Main game loop

def escaperoom():
    lives=max_lives
    badges=set()

    while True:
        choice = int(input("Choose your Door number (1-3 and choose 4 to exit the game:)"))
        if choice==1:
            if d1():
                print("You win")
                badges.add("math mastery")
            else:
                lives-=1
        elif choice==2:
            if d2():
                print("You win")
                badges.add("pro guesser")
            else:
                lives-=1
        elif choice==3:
            if d3():
                print("You win")
                badges.add("Luck maxxing")
            else:
                lives-=1
        elif choice==4:
            break
        else:
            print("wrong choice")
        print("lives left:",lives)
        if lives<=0:
            print("You lose")
            break
        print("badges:",badges)

        print("Escape Room Finished Thank you for playing")
# Program starts here

def main():
    intro()

#Calling functions
main()
escaperoom()
