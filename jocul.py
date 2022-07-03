from data_files import data
import random
from art import logo, vs
import os
import time

def random_():
    alegere = random.randint(0, len(data) - 1)
    return data[alegere]



def jocul():
    scor = 0
    game0 = True
    game0_1 = False
    alegere_1 = random_()
    alegere_2 = random_()
    scor_provizoriu = 0
    while game0:
        print(logo)
        if game0_1 == True:
            print("Nu am inteles!....Te rog repeta")
        if scor > 0:
            if game0_1 == True:
                print(f"Your current score: {scor}")
            else:
                print(f"You're right! Current score: {scor}.")
        print("Compare A: " + alegere_1["name"] + ", " + alegere_1["description"] + ", " + alegere_1["country"])
        print(vs)
        print("Compare B: " + alegere_2["name"] + ", " + alegere_2["description"] + ", " + alegere_2["country"])
        alegere = input("Who has more followers? Type 'A' or 'B':").lower()
        if alegere == "a":
            if alegere_1["follower_count"] >= alegere_2["follower_count"]:
                alegere_1 = alegere_2
                scor = scor + 1
                alegere_2 = random_()
            else:
                game0 = False
        elif alegere == "b":
            if alegere_2["follower_count"] >= alegere_1["follower_count"]:
                alegere_1 = alegere_2
                scor = scor + 1
                alegere_2 = random_()
            else:
                game0 = False
        elif alegere != "a" or alegere != "b":
            game0_1 = True
            continue
        if game0 == False:
            if scor > 0:
                return print(f"Sorry, that's wrong. Final score: {scor}")
            else:
                return print("Sorry, that's wrong")
        os.system('cls')
            
jocul()
game1 = True
input("Apasa \"ENTER\" pentru a continua")
while game1:
    os.system('cls')
    alegere = input("Doresti sa mai joci?...Scrie \"da\" sau \"nu\": ").lower()
    if alegere == "da":
        jocul()
        input("Apasa \"ENTER\" pentru a continua")
    elif alegere == "nu":
        os.system('cls')
        print("Bine.....La revedere...")
        time.sleep(2)
        game1 = False
    else:
        print("Nu am inteleses....")
        continue

