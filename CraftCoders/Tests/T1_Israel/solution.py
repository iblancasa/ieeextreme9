#!/bin/python
# -*- coding: utf-8 -*-

def main():
    letras = {}

    entrada = input()

    for letra in entrada:
        if not letra in letras.keys():
            letras[letra] = 0
        letras[letra] += 1

    impar = False;

    for letra in letras:
        if ( letras[letra] % 2 != 0 ) and impar:
            print ("NO",end ="")
            return 
        elif letras[letra] % 2 != 0:
            impar = True

    print("YES", end="")


if __name__ == '__main__':
    main()
