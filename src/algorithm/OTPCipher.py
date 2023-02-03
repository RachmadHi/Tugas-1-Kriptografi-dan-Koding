import re
#bikin guard input selain alphabet di GUI

def wordCounter(plaintext):
    counter = 0
    for i in plaintext:
        counter+=1
    return counter

def vigenere_cipher(text, key, operation):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    text = re.sub('[!@#$]%^&*()_-+=|";\':?/.,></', '', text) #omit special characters
    text = text.replace(' ','') #omit whitespaces
    text = text.upper()
    key = key.upper()
    key_index = 0
    key = key * (len(text)//len(key)) + key[:len(text) % len(key)]
    for char in text:
        char_index = ALPHABET.find(char)
        #if char_index == -1:
        #    result += char
        #   continue
        if operation == 'encrypt':
            result += ALPHABET[(char_index + ALPHABET.find(key[key_index])) % 26]
        elif operation == 'decrypt':
            result += ALPHABET[(char_index - ALPHABET.find(key[key_index])) % 26]
        key_index += 1
    return result


def menu():
    print('\n')
    print("--------  One Time Pad Cipher  ---------")
    print("Pilihan menu :")
    print("1. Enkripsi")
    print("2. Dekripsi")
    operator = int(input("Masukkan Nomor: "))
    if operator == 1:
        plaintext = input("input plaintext: ")
        operation='encrypt'
        counter = wordCounter(plaintext)
        otpkey= read_otpkey(counter)
        print(otpkey)
        encrypt = vigenere_cipher(plaintext,otpkey,operation)
        print("Cipher Text adalah: " + encrypt)
        print("Berikut adalah One Time Key Anda, gunakan ini untuk melakukan dekripsi: "+ otpkey )
    else:
        ciphertext = input("Masukkan ciphertext: ")
        otpkey = input("Masukkan OTP Key: ")
        operation = 'decrypt'
        decrypt = vigenere_cipher(ciphertext,otpkey,operation)
        print("Hasil dekripsi adalah: " + decrypt)
        
    
def read_otpkey(counter):
    otpkey=''
    with open('otpkey.txt') as f:
        
        for i in range (0,counter):
            lines = f.read(1)
            otpkey = otpkey+lines
    deleteUsedKey(counter)
    return otpkey
    f.close()

def deleteUsedKey(counter):
    with open("otpkey.txt", "r") as file:
        content = file.read()

    # Remove the first counter characters from the string
    content = content[counter:]

    with open("otpkey.txt", "w") as file:
        file.write(content)


menu()
