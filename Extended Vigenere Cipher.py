## Note

import math

enkripsi_result = ""
dekripsi_result = ""

def enkripsi(plaintext, key):
    hasil_enkripsi = ""
    for i in range (len(plaintext)):
        idx_key = ord(key[i])
        idx_text = ord(plaintext[i])
        
        hasil_enkripsi = hasil_enkripsi + (chr((idx_key+idx_text)%256))

    return(hasil_enkripsi)

def dekripsi(chipertext, key):
    hasil_dekripsi = ""
    for i in range (len(chipertext)):
        idx_key = ord(key[i])
        idx_text = ord(chipertext[i])
        
        hasil_dekripsi = hasil_dekripsi + (chr((idx_text-idx_key)%256))

    return(hasil_dekripsi)


def menu():
    menu_bool = False
    while menu_bool == False:
        print('\n')
        print("-------- Extended Vigenere Cipher  ---------")
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

                    plaintext = plaintext.replace(" ","")
                    key = key.replace(" ","")


                    if len(plaintext) == len(key) :
                        enkripsi_result = enkripsi(plaintext, key)
                        print(enkripsi_result)
                        inputCheck = False
                    elif len(key) < len(plaintext) :
                        key = key*(math.floor(len(plaintext)/len(key))) + key[0:(len(plaintext)%len(key))]
                        enkripsi_result = enkripsi(plaintext, key)
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

                    chipertext = chipertext.replace(" ","")
                    key = key.replace(" ","")

                    if len(chipertext) == len(key) :
                        dekripsi_result = dekripsi(chipertext, key)
                        print(dekripsi_result)
                        inputCheck = False
                    elif len(key) < len(chipertext) :
                        key = key*(math.floor(len(chipertext)/len(key))) + key[0:(len(chipertext)%len(key))]
                        dekripsi_result = dekripsi(chipertext, key)
                        print(dekripsi_result)
                        inputCheck = False
                    else :
                        print("Masukan salah, ulangi!")
                menu()
            else :
                print("Pilihan salah, ulangi!")
            menu_bool = True


menu()