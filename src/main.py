import subprocess
import os
import sys
from PyQt5 import QtWidgets
from interface.hompageInterface import Ui_Homepage


## Install package/library yang dibutuhkan
print("Preparing Classical Cryptography...")
print("Installing libraries...")
#curpath = str(os.path.realpath(__file__) + "\\..")
# reqpath = str(curpath + "\\requirements.txt")
# subprocess.call(f'pip install -r \"{reqpath}\"', shell=True)
# subprocess.call('cls', shell=True)

print("Opening Classical Cryptography...")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Homepage()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Classical Cryptography")
    MainWindow.show()

    MainWindow.setFixedHeight(650)
    MainWindow.setFixedWidth(1000)

    sys.exit(app.exec_())

def openFile():
    return None

def saveFile() :
    return None

def Vigenere(plaintext, key):
    return None

def ExtendedVigenere(plaintext, key):
    return None

def Playfair(plaintext, key):
    return None

def OTP(plaintext, key):
    return None


