# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:25:55 2023

@author: Abdullah
"""

person = {
    "fornavn" : "Ammar",
    "etternavn" : "Anoun",
    "alder" : 22,
    "fag" : ["R2", "IT2", "Norsk", "Historie", "Gym"]
    }

# Ordbok for engelsk til norsk
engelsk_norsk = {
    "dictionary" : "ordbok",
    "loop" : "løkke",
    "key" : "nøkkel",
    "value" : "verdi"
    }

"""
ordbok.items() gir key og value (som en tuple)
ordbok.keys() gir keys (nøkkel)
ordbok.values() gir values (verdiene)
"""

for e in engelsk_norsk:
    print(e)
    
for r in engelsk_norsk.items():
    print(r)
    
for c in engelsk_norsk.items():
    print(f"{c[0]} = {c[1]}")
    
#.items, .keys, .values

# Ønsker å finne ut hva "løkker" er på engelsk
for k in engelsk_norsk.keys():
    #print(engelsk_norsk[k])
    if engelsk_norsk[k] == "løkke":
        print("løkke på engelsk er", k)