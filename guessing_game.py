from guessing_game_logo import logo
import random
import os

print(logo)
print ("Vítejte ve hře Guess the secret number. Porazte počítač!.")
attempts = 0
play_again = "yes"

def guessing(attempts):
    print("Myslím si číslo od 0 do 100.")
    secret_number = random.randint(0, 101)
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
        print (f"Váš počet zbývajících pokusů je {attempts}")
        guess = int(input("Tipněte si číslo: "))
        # Check if the guess = secret number
        if guess == secret_number:
            print("Vyhráli jste! Gratuluji!")
            break
        # If the guess is not the secret number, it can be lower or bigger
        else:
            attempts -= 1
            if guess > secret_number: 
                print("Příliš vysoké!")
            else: 
                print("Příliš nízké!")

    if attempts == 0:
        print("Došly Vám pokusy! Prohráli jste.")
        print(f"Hádané číslo bylo {secret_number}")
     
     


while play_again == "yes":
    guessing(attempts)
    play_again = input("Chcete hrát znovu? yes / no  "). lower()
    os.system("cls")
    
print ("Díky za hru! Ahoj.")    