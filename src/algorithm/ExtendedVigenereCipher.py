## Note

import math

enkripsi_result = ""
dekripsi_result = ""

def EnkripsiExtendedVigenere(plaintext, key):
    plaintext = plaintext.upper().replace(" ","")
    key = key.upper().replace(" ","")

    if len(plaintext) > len(key) :
        key = key*(math.floor(len(plaintext)/len(key))) + key[0:(len(plaintext)%len(key))]
    elif len(plaintext) < len (key) :
        key = key[0:len(plaintext)]
    else :
        key = key
    
    ciphertext = ""
    for i in range (len(plaintext)):
        idx_key = ord(key[i])
        idx_text = ord(plaintext[i])
        
        ciphertext = ciphertext + (chr((idx_key+idx_text)%256))

    if plaintext.isupper() :
        ciphertext = ciphertext.upper()
    else :
        ciphertext = ciphertext.lower()
    return(ciphertext)

def DekripsiExtendedVigenere(ciphertext, key):
    plaintext = ciphertext.upper().replace(" ","")
    key = key.upper().replace(" ","")

    if len(plaintext) > len(key) :
        key = key*(math.floor(len(plaintext)/len(key))) + key[0:(len(plaintext)%len(key))]
    elif len(plaintext) < len (key) :
        key = key[0:len(plaintext)]
    else :
        key = key
        
    plaintext = ""
    for i in range (len(ciphertext)):
        idx_key = ord(key[i])
        idx_text = ord(ciphertext[i])
        
        plaintext = plaintext + (chr((idx_text-idx_key)%256))
    
    if ciphertext.isupper() :
        plaintext = plaintext.upper()
    else :
        plaintext = plaintext.lower()

    return(plaintext)