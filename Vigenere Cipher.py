## Note
# Nambahi pengahpus spasi
# 
import string
import math

alphabet = list(string.ascii_uppercase)
enkripsi_result = ""
dekripsi_result = ""
alphabet_type = ""

def enkripsi(plaintext, key, alphabet_type):
    hasil_enkripsi = ""
    i = 0
    j = 0
    for i in range (len(plaintext)):
        for j in range (len(alphabet)) :
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

def dekripsi(chipertext, key,alphabet_type):
    hasil_dekripsi = ""
    i = 0
    j = 0
    for i in range (len(chipertext)):
        for j in range (len(alphabet)) :
            if key[i] == alphabet[j] :
                idx_key = j
        for j in range (len(alphabet)) :
            if chipertext[i] == alphabet[j] :
                idx_text = j
        
        hasil_dekripsi = hasil_dekripsi + alphabet[(idx_text-idx_key)%26]
    
    if alphabet_type == "uppercase" :
        hasil_dekripsi = hasil_dekripsi.upper()
    else :
        hasil_dekripsi = hasil_dekripsi.lower()

    return(hasil_dekripsi)


def menu():
    menu_bool = False
    while menu_bool == False:
        print('\n')
        print("--------  Vigenere Cipher  ---------")
        print("Pilihan menu :")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Exit")
        pilihan_menu = int(input("Masukkan nomor : "))

        if pilihan_menu == 1 or pilihan_menu == 2 or pilihan_menu == 3 :
            if pilihan_menu == 1 :
                inputCheck = True
                while inputCheck:
                    plaintext = str(input("Masukan plaintext : "))
                    key = str(input("Masukan key :"))

                    if plaintext.isupper() :
                        alphabet_type = "uppercase"
                    else :
                        alphabet_type = "lowercase"

                    plaintext = plaintext.upper().replace(" ","")
                    key = key.upper().replace(" ","")


                    if len(plaintext) == len(key) :
                        enkripsi_result = enkripsi(plaintext, key, alphabet_type)
                        print(enkripsi_result)
                        inputCheck = False
                    elif len(key) < len(plaintext) :
                        key = key*(math.floor(len(plaintext)/len(key))) + key[0:(len(plaintext)%len(key))]
                        enkripsi_result = enkripsi(plaintext, key, alphabet_type)
                        print(enkripsi_result)
                        inputCheck = False
                    else :
                        print("Masukan salah, ulangi!")
                menu()
            elif pilihan_menu == 2 :
                inputCheck = True
                while inputCheck:
                    chipertext = str(input("Masukan chipertext : "))
                    key = str(input("Masukan key :"))

                    if chipertext.isupper() :
                        alphabet_type = "uppercase"
                    else :
                        alphabet_type = "lowercase"

                    chipertext = chipertext.upper().replace(" ","")
                    key = key.upper().replace(" ","")

                    if len(chipertext) == len(key) :
                        dekripsi_result = dekripsi(chipertext, key, alphabet_type)
                        print(dekripsi_result)
                        inputCheck = False
                    elif len(key) < len(chipertext) :
                        key = key*(math.floor(len(chipertext)/len(key))) + key[0:(len(chipertext)%len(key))]
                        dekripsi_result = dekripsi(chipertext, key, alphabet_type)
                        print(dekripsi_result)
                        inputCheck = False
                    else :
                        print("Masukan salah, ulangi!")
                menu()
            else :
                print("Pilihan salah, ulangi!")
            menu_bool = True


menu()
