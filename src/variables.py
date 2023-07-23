#coding:utf-8

"""
Nommer une variable : doit commencer par une lettre ou un underscore
                      ne pas contenir de caractères spéciaux
                      ne pas contenir d'espace
                      utiliser des underscores (_)

Types standards     : entier numérique (int)
                      nombre flottant (float)
                      chaîne de caractères (str)
                      booléen (bool)
                      autres(listes, dictionnaires, tuples, etc..)

Fonctions vues      : print()      -> afficher à l'écran
                      input()      -> lire au clavier
                      type()       -> retourne le type d'une donnée, variable, etc.  
                      int(), float(), bool() -> "caster" une donnée, la convertir
                      str.format() -> formater une chaîne                    
"""

agePersonne = 14 # agePersonne -> int

"""
Autres moyens de nommer une variable:

    age_personne
    agepersonne
    AgePersonne
    Age_Personne
    _age_personne
"""

nomJoueur = "MrBeast" # nomJoueur -> str
continuer_partie = True # continuer_partie -> bool


print(type(agePersonne)) # afficher le type de agePersonne (int)
print(type(nomJoueur)) # afficher le type de nomJoueur (str)


texte = "L'âge de la personne est {} et son nom est {}." # utiliser {} pour pouvoir passer des arguments avec str.format()
print(texte.format(agePersonne, nomJoueur)) # dans le premier {}, il y aura la valeur de agePersonne et dans le deuxième, la valeur de nomJoueur
# /!\ ceci est également possible -> texte = f"L'âge de la personne est {agePersonne} et son nom est {nomJoueur}."


pseudo = input("Choisir un pseudo : ") # input() va lire la donnée écrite au clavier par l'utilisateur
print("Salut", pseudo) # et ensuite afficher la donnée


prixHT = input("Entrez un prix HT : ") # lire la donnée renseignée
prixHT = int(prixHT) # convertir la donnée str en int
prixTTC = prixHT + (prixHT * 20 / 100) # pouvoir faire les calculs
print(f"Prix TTC = {prixTTC}") # puis afficher

valeur_booleen = True # déclarer un booléen
valeur_booleen = int(valeur_booleen) # le convertir en int
print(valeur_booleen) # afficher sa valeur -> True = 1 | False = 0