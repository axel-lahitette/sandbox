#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:55:25 2021

@author: axel
"""

"""
Return the number of the person using the name provided as argument
"""
def get(name):
    monFichier = open('fichier.txt','r')
    for ligne in monFichier:
        if name in ligne:
            number = ligne
            print(ligne)
            break
    monFichier.close()
    return number

"""
Insert the contact of the person using the name and number provided as arguments
"""
def put(name, number):
    monFichier = open('fichier.txt','a')
    monFichier.write("Le numéro : ")
    monFichier.write(number)
    monFichier.write("\t")
    monFichier.write("Nom : ")
    monFichier.write(name)
    monFichier.write("\n")
    monFichier.close()

"""
Delete the contact of the person with the name provided as argument
"""
def delete(name):
    return

def main():
    exemple_nom = "Guillaume"
    exemple_num = "0644093517"
    print(put(exemple_nom, exemple_num))
    print(get(exemple_nom))
    print(delete(exemple_nom))

if __name__ == "__main__":
    main()
