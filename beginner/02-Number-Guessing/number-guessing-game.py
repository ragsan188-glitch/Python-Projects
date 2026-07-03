import random
max_attempts=5

def game():
    print("Welcome to the Number Guessing Game!")
    answer=random.randint(1,20)

    attempts=0
    while attempts<max_attempts:
        guess = int(input("Enter your guess(1-20): "))
        if guess>20 or guess<1:
            print("guess is not in the desired range\nTry again!")
            continue
        elif guess==answer:
            print("Congratulations")
            attempts+=1
            break
        elif guess>answer:
            print("Too high!")
            attempts+=1
        else :
            print("Too low!")
            attempts+=1

    if attempts==5:
        print("Game Over! \nThe number was " + str(answer))
    else:
        print("You Guessed it in",attempts,"attempts")

game()


