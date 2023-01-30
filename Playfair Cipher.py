import string
import math
from numpy import *

alphabet = list(string.ascii_uppercase)
key = ""
plaintext = ""

def key_setting(key) :
    new_key = ""
    for i in range (len(key)) :
        if (key[i] != "J") and (key[i] not in new_key) :
            new_key = new_key + key[i]

    new_key = new_key.replace(" ","")

    for i in range (len(alphabet)) :
        if (alphabet[i] != "J") and (alphabet[i] not in new_key) :
            new_key = new_key + alphabet[i]

    return new_key

def newkey_matrix(key):
    key_matrix = reshape(list(key),(5,5))
    return key_matrix

def plaintext_setting(plaintext) :
    new_plaintext = ""
    final_plaintext = ""

    if "j" in plaintext :
        for i in range (len(plaintext)) :
            if (plaintext[i] == "J"):
                new_plaintext = new_plaintext + "i"
            else :
                new_plaintext = new_plaintext + plaintext[i]
    else :
        new_plaintext = plaintext

    new_plaintext = new_plaintext.replace(" ","")

    for i in range (len(new_plaintext)) :
        if i+1 < len(new_plaintext) :
            if (new_plaintext[i] == new_plaintext[i+1]):
                final_plaintext = final_plaintext + new_plaintext[i] + "x"
            else :
                final_plaintext = final_plaintext + new_plaintext[i]
        else :
            final_plaintext = final_plaintext + new_plaintext[i]

    if len(final_plaintext) % 2 == 1 :
        final_plaintext = final_plaintext + "x"

    return final_plaintext

def playfair_enkripsi(key, plaintext):
    ciphertext = ""
    i = 0
    
    while i <= (len(plaintext)-2) :
        bigram = plaintext[i] + plaintext[i+1]
        row1 = None
        row2 = None
        col1 = None
        col2 = None

        for j in range (5) :
            for k in range (5) :
                if key[j][k] == bigram[0].upper() :
                    row1 = j
                    col1 = k
                elif key[j][k] == bigram[1].upper() :
                    row2 = j
                    col2 = k

        if row1 == row2 :
            ciphertext = ciphertext + key[row1][(col1 + 1)%5] + key[row1][(col2 + 1)%5]
        elif col1 == col2 :
            ciphertext = ciphertext + key[(row1+1)%5][col1] + key[(row2+1)%5][col2]
        else :
            ciphertext = ciphertext + key[row1][col2] + key[row2][col1]
        
        i = i+2
  
    return ciphertext

def playfair_dekripsi(key, ciphertext): 
    decyrpt_result = ""
    i = 0
    
    while i <= (len(ciphertext)-2) :
        bigram = ciphertext[i] + ciphertext[i+1]
        row1 = None
        row2 = None
        col1 = None
        col2 = None

        for j in range (5) :
            for k in range (5) :
                if key[j][k] == bigram[0].upper() :
                    row1 = j
                    col1 = k
                elif key[j][k] == bigram[1].upper() :
                    row2 = j
                    col2 = k

        if row1 == row2 :
            decyrpt_result += key[row1][(col1 - 1)%5] + key[row1][(col2 - 1)%5]
        elif col1 == col2 :
            decyrpt_result += key[(row1 - 1)%5][col1] + key[(row2 - 1)%5][col2]
        else :
            decyrpt_result += key[row1][col2] + key[row2][col1]
        
        i = i+2
  
    return decyrpt_result

def menu_playchiper():
    plaintext = str(input("Masukkan plaintext : "))
    key = str(input("Masukkan key : "))

    new_key = key_setting(key)
    new_plaintext = plaintext_setting(plaintext)

    new_key_matrix = newkey_matrix(new_key)
    print(new_key_matrix)
    print(new_plaintext)

    play = playfair_enkripsi(new_key_matrix, new_plaintext)
    print(play)

    dec = playfair_dekripsi(new_key_matrix, play)
    print(dec)

menu_playchiper()