def openFile():
    return None

def saveFile(algorithm, text) :
    return None
ciphertext = "AAAAAAAAAAAAAA"
new_ciphertext = ""
for i in range (len(ciphertext)) :
    if i % 5 == 0 and i != 0 :
        new_ciphertext += ciphertext[i] + " "
    else :
        new_ciphertext += ciphertext[i]

print(new_ciphertext)