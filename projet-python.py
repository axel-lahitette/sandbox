#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:55:25 2021

@author: axel
"""

MENU = int(input("Saisir 1 pour entrer un nouveau contact, 2 pour effectuer une recherche et 0 pour quitter"))
MENU = 1
while MENU != 0:
    if MENU == 1:
        numero = input("Entrez un numéro ")
        monFichier = open('fichier.txt', 'a')
        monFichier.write("Le numéro : ")
        monFichier.write(numero)
        monFichier.write("\t")
        monFichier.close()
        print('Numéro Enregistré')
 
        nom = input("Entrer le nom correspondant : ")
        monFichier = open('fichier.txt', 'a')
        monFichier.write("Nom : ")
        monFichier.write(nom)
        monFichier.write("\t")
        monFichier.close()
        print('Le nom a bien été enregistré')
        MENU=int(input("Saisir 1 pour entrer un nouveau contact, 2 pour effectuer une recherche et 0 pour quitter"))
 
    if MENU == 2:
        monFichier = open('fichier.txt', 'r')
        recherche = input("Entrer le nom du contact")
        for ligne in monFichier:
            if recherche in ligne:
                print(ligne)
                break
        monFichier.close()
        print(numero)
        MENU = int(input("Saisir 1 pour entrer un nouveau contact, 2 pour effectuer une recherche et 0 pour quitter"))
