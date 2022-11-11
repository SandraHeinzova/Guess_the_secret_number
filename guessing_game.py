from guessing_game_logo import logo
import random
import os

print(logo)
print ("Vítejte ve hře Guess secret number. Porazte počítač.")
hraju = "ano"

def tezka_uroven():
    pokusy = 5
    while pokusy > 0:
        print (f"Váš počet zbývajících pokusů je {pokusy}")
        tip = int(input("Tipněte si číslo: "))
        if tip > number:
            print("Příliš vysoké!")
            pokusy -= 1
            if pokusy == 0:
                print("Došly Vám pokusy! Prohráli jste. Mmožná příště.")
                print(f"Hádané číslo bylo {number}")
                break
        elif tip < number:
            print("Příliš nízké!")
            pokusy -= 1
            if pokusy == 0:
                print("Došly Vám pokusy! Prohráli jste. Mmožná příště.")
                print(f"Hádané číslo bylo {number}")
                break
        elif tip == number:
            print("Vyhráli jste! Gratuluji!")
            break
            
def lehka_uroven():
    pokusy = 10
    while pokusy > 0:
        print (f"Váš počet zbývajících pokusů je {pokusy}")
        tip = int(input("Tipněte si číslo: "))
        if tip > number:
            print("Příliš vysoké!")
            pokusy -= 1
            if pokusy == 0:
                print("Došly Vám pokusy! Prohráli jste. Mmožná příště.")
                print(f"Hádané číslo bylo {number}")
                break
        elif tip < number:
            print("Příliš nízké!")
            pokusy -= 1
            if pokusy == 0:
                print("Došly Vám pokusy! Prohráli jste. Mmožná příště.")
                print(f"Hádané číslo bylo {number}")
                break
        elif tip == number:
            print("Vyhráli jste! Gratuluji!")
            break


while hraju == "ano":
    print("Myslím si číslo od 1 do 100.")
    number = random.randint(0, 101)
    obtiznost = input("Vyberte obtížnost hry. Napište 'easy' nebo 'hard' ").lower()
    if obtiznost == "easy":
        lehka_uroven()
        hraju = input("Napište 'ano', pokud chcete hrát znovu. Napište 'ne', pokud chcete hru ukončit. ")
        os.system("cls")
    elif obtiznost == "hard":
        tezka_uroven()
        hraju = input("Napište 'ano', pokud chcete hrát znovu. Napište 'ne', pokud chcete hru ukončit. ")
        os.system("cls")

