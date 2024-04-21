#AveryAllen, CIS261, GuessingGame
import random

def play():
    x = random.randint(1, 100)

    guess = int(input("Guess a number between 1 and 100: "))
    while True:
        if guess > x:
            print ("Sorry, unfortunately your guess was too high. Try again!")
            guess = int(input("Guess a number between 1 and 100: "))
        elif guess < x:
            print("Sorry, unfornately your guess was too low. Try again!")
            guess = int(input("Guess a number between 1 and 100: "))
        else:
            print("WooHoo!! You got it correct!")
            break
while True:
    play()
    answer = input("Do you want to play again? (yes/no): ")
    if answer.lower() != 'yes':
        break
    print("Let's play again!\n")
        
            
                        
                        
                
                
