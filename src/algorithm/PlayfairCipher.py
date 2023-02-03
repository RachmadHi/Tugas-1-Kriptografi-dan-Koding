import string
import math
from numpy import *

def key_setting(key) :
    alphabet = list(string.ascii_uppercase)
    key = key.upper()
    new_key = ""
    for i in range (len(key)) :
        if (key[i] != "J") and (key[i] not in new_key) :
            new_key = new_key + key[i]

    new_key = new_key.replace(" ","")

    for i in range (len(alphabet)) :
        if (alphabet[i] != "J") and (alphabet[i] not in new_key) :
            new_key = new_key + alphabet[i]
    
    key_matrix = reshape(list(new_key),(5,5))
    return key_matrix

def plaintext_setting(plaintext) :
    plaintext = plaintext.upper()
    new_plaintext = ""
    final_plaintext = ""

    if "J" in plaintext :
        for i in range (len(plaintext)) :
            if (plaintext[i] == "J"):
                new_plaintext = new_plaintext + "I"
            else :
                new_plaintext = new_plaintext + plaintext[i]
    else :
        new_plaintext = plaintext

    new_plaintext = new_plaintext.replace(" ","")

    for i in range (len(new_plaintext)) :
        if i+1 < len(new_plaintext) :
            if (new_plaintext[i] == new_plaintext[i+1]):
                final_plaintext = final_plaintext + new_plaintext[i] + "X"
            else :
                final_plaintext = final_plaintext + new_plaintext[i]
        else :
            final_plaintext = final_plaintext + new_plaintext[i]

    if len(final_plaintext) % 2 == 1 :
        final_plaintext = final_plaintext + "X"

    return final_plaintext

def ciphertext_setting(ciphertext):
    ciphertext= ciphertext.upper()
    final_ciphertext = ""
    new_ciphertext = ciphertext.replace(" ","")

    for i in range (len(new_ciphertext)) :
        if new_ciphertext[i] != "X" :
            final_ciphertext = final_ciphertext + new_ciphertext[i]

    return final_ciphertext

def EnkripsiPlayfair(plaintext, key):
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
        
    if plaintext.isupper() :
        ciphertext = ciphertext.upper()
    else :
        ciphertext = ciphertext.lower()

    return ciphertext

def DekripsiPlayfair(ciphertext, key): 
    plaintext = ""
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
            plaintext += key[row1][(col1 - 1)%5] + key[row1][(col2 - 1)%5]
        elif col1 == col2 :
            plaintext += key[(row1 - 1)%5][col1] + key[(row2 - 1)%5][col2]
        else :
            plaintext += key[row2][col1] + key[row1][col2]
        
        i = i+2

    if ciphertext.isupper() :
        plaintext = plaintext.upper()
    else :
        plaintext = plaintext.lower()

    return plaintext