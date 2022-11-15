from guessing_game_logo import logo
import random
import os
import time

print(logo)
print ("Vítejte ve hře Guess the secret number. Porazte počítač!.")
attempts = 0
play_again = "yes"

def guessing(attempts):
    print("Myslím si číslo od 0 do 100.")
    secret_number = random.randint(0, 100)
    print(secret_number)
    # while loop to check valid difficulty input
    while True:
        difficulty = input("Zvolte obtížnost hry: easy/hard: ").lower()
        if difficulty == "easy":
            attempts = 10
            break
        elif difficulty == "hard":
            attempts = 5
            break
        else:
            print("Nerozumím.")
    
    while attempts > 0:
        # while loop and try - except to check whether is 'guess' int or not
        while True:
            print (f"Váš počet zbývajících pokusů je {attempts}")
            guess = input("Tipněte si číslo: ")
            if attempts > 0:
                try:
                    # Check if the guess = secret number
                    guess = int(guess)
                    if guess == secret_number:
                        print("Vyhráli jste! Gratuluji!")
                        return False
                    # If the guess is not the secret number, it can be lower or bigger
                    else:
                        attempts -= 1
                        if guess > secret_number: 
                            print("Příliš vysoké!")
                        else: 
                            print("Příliš nízké!")
                except ValueError: 
                    print("To nebylo číslo! Tipni si číslo.")

            else:
                print("Došly Vám pokusy! Prohráli jste.")
                print(f"Hádané číslo bylo {secret_number}")
                break
     
     


while play_again == "yes":
    guessing(attempts)
    play_again = input("Chcete hrát znovu? yes / no  "). lower()
    if play_again == "yes":
        print("Hra začíná znovu!")
        os.system("cls")
    elif play_again != "no":
        print ("Tato odpověď nebyla v nabídce. Program bude ukončen.")
    
    
print ("Díky za hru! Ahoj.") 
time.sleep(5)
os.system("cls")