# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:48:15 2023

@author: Abdullah
"""
import random

person = {
    "fornavn" : "Ammar",
    "etternavn" : "Anoun",
    "alder" : "22"
    }

norsk_arabisk = {
    "spise" : "r",
    "spille" : "d",
    "studere" : "a", 
    #"studere" : "d",
    }
for x in norsk_arabisk.keys():
    print(x, end=" ")
#print(norsk_arabisk)
"""
# "spise" : "يأكل",
# "spille" : "يلعب",
# "studere" : "يدرس "
b = 0

# for i in norsk_arabisk.items():
#    # print(i)
#     print(i[0], "=", i[1])
# print("Du har 10 ganger å prøve deg på det spillet")

norsk = random.choice(list(norsk_arabisk.keys()))
arabisk = input(f"Hva betyr {norsk} i arabisk: ")
while True:
    b += 1
    if arabisk == norsk_arabisk[norsk]:
        print("Det er riktig")
        break
    else:
        print("Det er feil, du har ", b ,"/10, prøv igjen")
    if b == 10:
        print("Du har brukt maksimalt prøve sjanser")
        break
    
    


# for c in engelsk_norsk.items():
#     print(f"{c[0]} = {c[1]}")
"""