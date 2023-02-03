## Note
# Nambahi pengahpus spasi
# 
import string
import math

alphabet = list(string.ascii_uppercase)

def EnkripsiVigenere(plaintext, key):
    alphabet = list(string.ascii_uppercase)
    if plaintext.isupper() :
        alphabet_type = "uppercase"
    else :
        alphabet_type = "lowercase"

    plaintext = plaintext.upper().replace(" ","")
    key = key.upper().replace(" ","")

    if len(plaintext) > len(key) :
        key = key*(math.floor(len(plaintext)/len(key))) + key[0:(len(plaintext)%len(key))]
    elif len(plaintext) < len (key) :
        key = key[0:len(plaintext)]
    else :
        key = key

    hasil_enkripsi = ""

    i = 0
    j = 0
    for i in range (len(plaintext)):
        for j in range (len(alphabet)):
            if key[i] == alphabet[j] :
                idx_key = j
        for j in range (len(alphabet)) :
            if plaintext[i] == alphabet[j] :
                idx_text = j
        
        hasil_enkripsi = hasil_enkripsi + alphabet[(idx_key+idx_text)%26]
        
    if alphabet_type == "uppercase" :
        hasil_enkripsi = hasil_enkripsi.upper()
    else :
        hasil_enkripsi = hasil_enkripsi.lower()

    return(hasil_enkripsi)

def DekripsiVigenere(ciphertext, key):
    alphabet = list(string.ascii_uppercase)
    if ciphertext.isupper() :
        alphabet_type = "uppercase"
    else :
        alphabet_type = "lowercase"

    ciphertext = ciphertext.upper().replace(" ","")
    key = key.upper().replace(" ","")

    if len(ciphertext) > len(key) :
        key = key*(math.floor(len(ciphertext)/len(key))) + key[0:(len(ciphertext)%len(key))]
    elif len(ciphertext) < len (key) :
        key = key[0:len(ciphertext)]
    else :
        key = key

    hasil_dekripsi = ""
    i = 0
    j = 0
    for i in range (len(ciphertext)):
        for j in range (len(alphabet)) :
            if key[i] == alphabet[j] :
                idx_key = j
        for j in range (len(alphabet)) :
            if ciphertext[i] == alphabet[j] :
                idx_text = j
        
        hasil_dekripsi = hasil_dekripsi + alphabet[(idx_text-idx_key)%26]
    
    if alphabet_type == "uppercase" :
        hasil_dekripsi = hasil_dekripsi.upper()
    else :
        hasil_dekripsi = hasil_dekripsi.lower()

    return(hasil_dekripsi)