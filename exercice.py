#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_majuscule = ""
    for maj in mot:
        maj = ord(maj) - 32
        mot_majuscule += chr(maj)
    return mot_majuscule


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
