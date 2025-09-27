import random
import time

number=random.randint(1,100)
def intro():
    print("May I ask what is your name?")

    global name
    name=input()

    print("Hello " + name + "! Welcome to the Guess the Random Number Game!I amthinking of a number between 1-100")

    if (number%2==0):
        print("This is an even number")
    else:
        print("This is an odd number")

    time.sleep(0.5)
    print("Guess!")

def pick():
    guessestaken=0
    while guessestaken<6:
        time.sleep(0.25)

        enter=input("Guess")

        try:
            
            guess=int(enter)
            if guessestaken<=100 or guessestaken>=1:
                guessestaken=guessestaken+1
                if guessestaken<6:
                    if guess<number:
                        print("Your guess is too low")
                    if guess>number:
                        print("Your guess is too high")
                    if guess!=number:
                        time.sleep(0.5)
                        print("try again")
                    if guess==number:
                        print("Good guess.It was correct")
                        break
                if guess>100 or guess<1:
                    print("Silly goose! This number is not valid")
                    time.sleep(0.25)
                    print("PLease enter a number between 1-100")
        except:
            print("I don't think"+enter+"is a number.Sorry")


        if guessestaken==6:
            print("Sorry you have used all your guesses.The number was "+str(number))

play_again="yes"    
if play_again=="yes":
    intro()
    pick()
    play=input("Would you like to play again?")
else:
    print("Thank you for playing! Goodbye!")




    