import random

vastaus = random.randint(1, 10)
arvaus = int(input("Arvaa 1-10 väliltä: "))

while vastaus != arvaus:
    if arvaus < vastaus:
        print("Liian pieni arvaus.")
    elif arvaus > vastaus:
        print("Liian suuri arvaus.")

    arvaus = int(input("Arvaa 1-10 väliltä: "))

print("Arvasit oikein.")
