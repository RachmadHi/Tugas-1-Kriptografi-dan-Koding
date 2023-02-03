def openFile():
    return None

def saveFile(algorithm, text) :
    file_name =  algorithm + "_file"
    file = open(f'savedfile\\{file_name}.txt', 'w')
    file.write(text)
    file.close()

def read_from_file(randomfile):
    with open(randomfile, 'rb') as file:
        content = file.read()
        return content

def write_binary(randomfile,content):
    with open(randomfile, 'wb') as file:
        file.write(content)

def read_from_file(randomfile):
    with open(randomfile, 'rb') as file:
        content = file.read()
        return content

def write_binary(randomfile,content):
    with open(randomfile, 'wb') as file:
        file.write(content)