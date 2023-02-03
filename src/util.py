def openFile():
    return None

def saveFile(algorithm, text) :
    file_name =  algorithm + "_file"
    file = open(f'savedfile\\{file_name}.txt', 'w')
    file.write(text)
    file.close()