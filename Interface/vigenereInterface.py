# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setStyleSheet("background: #E2CD93;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DecryptPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DecryptPushButton.setGeometry(QtCore.QRect(310, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.DecryptPushButton.setFont(font)
        self.DecryptPushButton.setStyleSheet("background: #D19B47;\n"
"border-radius: 15px;\n"
"\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 49px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.DecryptPushButton.setObjectName("DecryptPushButton")
        self.Judul = QtWidgets.QLabel(self.centralwidget)
        self.Judul.setGeometry(QtCore.QRect(260, 30, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(36)
        self.Judul.setFont(font)
        self.Judul.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.Judul.setObjectName("Judul")
        self.encryptPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptPushButton.setGeometry(QtCore.QRect(100, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.encryptPushButton.setFont(font)
        self.encryptPushButton.setStyleSheet("background: #D19B47;\n"
"border-radius: 15px;\n"
"\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 49px;\n"
"text-align: center;\n"
"letter-spacing: 0.2em;\n"
"color: #FFFFFF;")
        self.encryptPushButton.setObjectName("encryptPushButton")
        self.TextInput = QtWidgets.QTextEdit(self.centralwidget)
        self.TextInput.setGeometry(QtCore.QRect(100, 160, 561, 41))
        self.TextInput.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.TextInput.setObjectName("TextInput")
        self.textInput_label = QtWidgets.QLabel(self.centralwidget)
        self.textInput_label.setGeometry(QtCore.QRect(100, 100, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.textInput_label.setFont(font)
        self.textInput_label.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.textInput_label.setObjectName("textInput_label")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(100, 190, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.keyLabel.setFont(font)
        self.keyLabel.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.keyLabel.setObjectName("keyLabel")
        self.KeyInput = QtWidgets.QTextEdit(self.centralwidget)
        self.KeyInput.setGeometry(QtCore.QRect(100, 250, 791, 41))
        self.KeyInput.setStyleSheet("background-color : white;\n"
"border-radius : 15px;")
        self.KeyInput.setObjectName("KeyInput")
        self.ResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.ResultLabel.setGeometry(QtCore.QRect(100, 420, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.ResultLabel.setObjectName("ResultLabel")
        self.textInput_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.textInput_label_4.setGeometry(QtCore.QRect(700, 90, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.textInput_label_4.setFont(font)
        self.textInput_label_4.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.textInput_label_4.setObjectName("textInput_label_4")
        self.SpacingLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpacingLabel.setGeometry(QtCore.QRect(100, 280, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(14)
        self.SpacingLabel.setFont(font)
        self.SpacingLabel.setStyleSheet("text-align : center;\n"
"color: #B67F57;")
        self.SpacingLabel.setObjectName("SpacingLabel")
        self.NoSpacingRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.NoSpacingRadioButton.setGeometry(QtCore.QRect(100, 340, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.NoSpacingRadioButton.setFont(font)
        self.NoSpacingRadioButton.setStyleSheet("font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 32px;\n"
"\n"
"color: #B67F57;\n"
"")
        self.NoSpacingRadioButton.setObjectName("NoSpacingRadioButton")
        self.GroupBy5radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.GroupBy5radioButton.setGeometry(QtCore.QRect(260, 340, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.GroupBy5radioButton.setFont(font)
        self.GroupBy5radioButton.setStyleSheet("font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 32px;\n"
"\n"
"color: #B67F57;\n"
"")
        self.GroupBy5radioButton.setObjectName("GroupBy5radioButton")
        self.encryptPushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.encryptPushButton_2.setGeometry(QtCore.QRect(100, 570, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.encryptPushButton_2.setFont(font)
        self.encryptPushButton_2.setStyleSheet("background: #D19B47;\n"
"border-radius: 15px;\n"
"\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 49px;\n"
"text-align: center;\n"
"letter-spacing: 0.2em;\n"
"color: #FFFFFF;")
        self.encryptPushButton_2.setObjectName("encryptPushButton_2")
        self.DecryptPushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.DecryptPushButton_2.setGeometry(QtCore.QRect(700, 580, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.DecryptPushButton_2.setFont(font)
        self.DecryptPushButton_2.setStyleSheet("background: #E24848;\n"
"border-radius: 15px;\n"
"\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"line-height: 49px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.DecryptPushButton_2.setObjectName("DecryptPushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 480, 791, 71))
        self.textBrowser_2.setStyleSheet("background : white;\n"
"border-radius : 15px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.SpacingLabel.raise_()
        self.ResultLabel.raise_()
        self.keyLabel.raise_()
        self.DecryptPushButton.raise_()
        self.Judul.raise_()
        self.encryptPushButton.raise_()
        self.textInput_label.raise_()
        self.TextInput.raise_()
        self.KeyInput.raise_()
        self.textInput_label_4.raise_()
        self.NoSpacingRadioButton.raise_()
        self.GroupBy5radioButton.raise_()
        self.encryptPushButton_2.raise_()
        self.DecryptPushButton_2.raise_()
        self.textBrowser_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DecryptPushButton.setText(_translate("MainWindow", "Decrypt"))
        self.Judul.setText(_translate("MainWindow", "Vigenere Cipher"))
        self.encryptPushButton.setText(_translate("MainWindow", "Encrypt"))
        self.TextInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.textInput_label.setText(_translate("MainWindow", "Text input"))
        self.keyLabel.setText(_translate("MainWindow", "Key"))
        self.KeyInput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.ResultLabel.setText(_translate("MainWindow", "Result"))
        self.textInput_label_4.setText(_translate("MainWindow", "Input File"))
        self.SpacingLabel.setText(_translate("MainWindow", "Spacing"))
        self.NoSpacingRadioButton.setText(_translate("MainWindow", "No Spacing"))
        self.GroupBy5radioButton.setText(_translate("MainWindow", "Group by 5"))
        self.encryptPushButton_2.setText(_translate("MainWindow", "Save File"))
        self.DecryptPushButton_2.setText(_translate("MainWindow", "Back to Main Menu"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
