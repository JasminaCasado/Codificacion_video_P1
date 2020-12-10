#!/usr/bin/python3

import numpy as np


def rgb2yuv(rgb_values):

        R = rgb_values[0]
        G = rgb_values[1]
        B = rgb_values[2]

        Y = round(0.299 * R + 0.587 * G + 0.114 * B)
        U = round(-0.168736 * R - 0.331264 * G + 0.5 * B + 128)
        V = round(0.5 * R - 0.418688 * G - 0.081312 * B + 128)
        yuv = [Y, U, V]

        for i in range(0, len(yuv)):
            if yuv[i] > 255:
                yuv[i] = 255
            elif yuv[i] < 0:
                yuv[i] = 0

        return yuv


def yuv2rgb(yuv_values):

        Y = yuv_values[0]
        U = yuv_values[1]
        V = yuv_values[2]

        R = round(Y + 1.4075 * (V - 128))
        G = round(Y - 0.3455 * (U - 128) - (0.7169 * (V - 128)))
        B = round(Y + 1.7790 * (U - 128))
        rgb = [R, G, B]

        for i in range(0, len(rgb)):
            if rgb[i] > 255:
                rgb[i] = 255
            elif rgb[i] < 0:
                rgb[i] = 0
        return rgb


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0
n = 3  # length data input

while not salir:

    print ("1. Opcion 1 : Conversor RGB a YUV")
    print ("2. Opcion 2 : Conversor YUV a RGB")
    # print ("3. Opcion 3")
    print ("4. Salir")

    # print ("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print ("Opcion 1")

        # Below line read inputs from user using map() function
        RGB_values = list(map(int, input("\nIntroduce los valores RGB : ").strip().split()))[:n]

        yuv = rgb2yuv(RGB_values)
        print("\nLa conversion de", RGB_values, "a YUV es", yuv)
        print("\n")

    elif opcion == 2:
        print ("Opcion 2")
        print ("Introduce los valores YUB")
        # Below line read inputs from user using map() function
        YUB_values = list(map(int, input("\nIntroduce los valores YUB : ").strip().split()))[:n]

        rgb = yuv2rgb(YUB_values)
        print("La conversion de", YUB_values, "a RGB es", rgb,"\n")

    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 2")

print ("Fin")
