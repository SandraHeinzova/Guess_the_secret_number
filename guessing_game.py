from guessing_game_logo import logo
import random
import os

# print(logo)
print ("Vítejte ve hře Guess secret number. Porazte počítač.")
hraju = "ano"

print("Myslím si číslo od 1 do 100.")
number = random.randint(0, 101)
print (number)
pokusy = 5

while pokusy > 0:
    print (f"Váš počet zbývajících pokusů je {pokusy}")
    tip = int(input("Tipněte si číslo: "))
    if tip > number:
        print("Příliš vysoké. Zkuste to znovu.")
        pokusy -= 1
    elif tip < number:
        print("Příliš nízké! Zkuste to znovu!")
        pokusy -= 1
    elif tip == number:
        print("Vyhráli jste! Gratuluji!")  
