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
        
def encrypt_file(file_path):
    with open(file_path, "r") as file:
        plaintext = file.read()
        counter = wordCounter(plaintext)
    otpkey = read_otpkey(counter)
    print('Berikut adalah OTP Key yang digunakan: ' + otpkey )
    ciphertext = vigenere_cipher(plaintext, otpkey,'encrypt')
    with open(file_path, "w") as file:
        file.write(ciphertext)

def decrypt_file(file_path):
    """Decrypts the contents of the file at file_path using the one-time pad cipher"""
    key = input('Masukkan Key: ')
    with open(file_path, "r") as file:
        ciphertext = file.read()
    plaintext = vigenere_cipher(ciphertext, key,'decrypt')
    with open(file_path, "w") as file:
        file.write(plaintext)

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

def read_from_file(randomfile):
    with open(randomfile, 'rb') as file:
        content = file.read()
        return content

def write_binary(randomfile,content):
    with open(randomfile, 'wb') as file:
        file.write(content)



menu()
