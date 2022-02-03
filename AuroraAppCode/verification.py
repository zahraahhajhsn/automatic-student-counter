
import sys
import platform
from typing import List
from threading import Timer
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import  Timer

class Ui_VerifyMainWindow(object):
    def setupUi(self, VerifyMainWindow):
        VerifyMainWindow.setObjectName("VerifyMainWindow")
        VerifyMainWindow.resize(1000, 1000)
        VerifyMainWindow.showMaximized()
        VerifyMainWindow.setStyleSheet("QMainWindow{\n"
"\n"
"\n"
"background-image: url(images/new.png);\n"
"}")
        self.centralwidget = QWidget(VerifyMainWindow)
        self.centralwidget.setStyleSheet("QMainWindow{\n"
"background-image: url(images/new.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setStyleSheet("")
        self.pages.setObjectName("pages")
        self.changepassword = QWidget()
        self.changepassword.setObjectName("changepassword")
        self.verticalLayout_3 = QVBoxLayout(self.changepassword)
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, 20)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QLabel(self.changepassword)
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(225, 37, 52);\n"
"font: 87 30pt \"Arial Black\";")
        self.label_15.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.verticalFrame_4 = QFrame(self.changepassword)
        self.verticalFrame_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 11pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_4.setContentsMargins(50, 40, 50, 40)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_21 = QLabel(self.verticalFrame_4)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21, 0,Qt.AlignHCenter)
        self.newpassword = QLineEdit(self.verticalFrame_4)
        self.newpassword.setInputMask("")
        self.newpassword.setEchoMode(QLineEdit.Password)
        self.newpassword.setObjectName("newpassword")
        self.verticalLayout_4.addWidget(self.newpassword)
        self.label_22 = QLabel(self.verticalFrame_4)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.confirmpass = QLineEdit(self.verticalFrame_4)
        self.confirmpass.setEchoMode(QLineEdit.Password)
        self.confirmpass.setObjectName("confirmpass")
        self.verticalLayout_4.addWidget(self.confirmpass)
        self.incorrectv =QLabel(self.verticalFrame_4)
        self.incorrectv.setStyleSheet("color: rgb(225, 37, 52);")
        self.incorrectv.setText("")
        self.incorrectv.setObjectName("incorrectv")
        self.verticalLayout_4.addWidget(self.incorrectv)
        self.submitchange = QPushButton(self.verticalFrame_4)
        self.submitchange.setObjectName("submitchange")
        self.verticalLayout_4.addWidget(self.submitchange)
        self.verticalLayout_3.addWidget(self.verticalFrame_4, 0,Qt.AlignHCenter)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 5)
        self.pages.addWidget(self.changepassword)
        self.verifycode = QWidget()
        self.verifycode.setObjectName("verifycode")
        self.verticalLayout_6 = QVBoxLayout(self.verifycode)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QLabel(self.verifycode)
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(225, 37, 52);\n"
"font: 87 30pt \"Arial Black\";")
        self.label_16.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.verticalWidget = QWidget(self.verifycode)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 350)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QLineEdit(self.horizontalWidget)
        self.lineEdit.setMinimumSize(QSize(400, 0))
        self.lineEdit.setMaximumSize(QSize(400, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit, 0, Qt.AlignVCenter)
        self.state = QLabel(self.horizontalWidget)
        self.state.setMaximumSize(QSize(40, 40))
        self.state.setText("")
        self.state.setScaledContents(True)
        self.state.setObjectName("state")
        self.horizontalLayout.addWidget(self.state, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.horizontalWidget, 0,Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.incorrect = QLabel(self.verticalWidget)
        self.incorrect.setObjectName("incorrect")
        self.incorrect.setStyleSheet("color: rgb(225, 37, 52);\n"
                                     "font: 87 10pt \"Arial Black\";")
        self.incorrect.setText("")
        self.verticalLayout_5.addWidget(self.incorrect,0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.submit = QPushButton(self.verticalWidget)
        self.submit.setMaximumSize(QSize(70, 16777215))
        self.submit.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.submit.setObjectName("submit")
        self.verticalLayout_5.addWidget(self.submit, 0, Qt.AlignHCenter|Qt.AlignVCenter)
        self.verticalLayout_5.setStretch(0, 10)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 10)
        self.verticalLayout_6.addWidget(self.verticalWidget)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)
        self.pages.addWidget(self.verifycode)
        self.verticalLayout.addWidget(self.pages)
        self.pages.setCurrentIndex(1)
        VerifyMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerifyMainWindow)
        QMetaObject.connectSlotsByName(VerifyMainWindow)


    def retranslateUi(self, VerifyMainWindow):
        VerifyMainWindow.setWindowTitle(QCoreApplication.translate("VerifyMainWindow", "verify","None"))
        self.label_15.setText(QCoreApplication.translate("VerifyMainWindow", "<html><head/><body><p align=\"center\">CHANGE PASSWORD</p></body></html>","None"))
        self.label_21.setText(QCoreApplication.translate("VerifyMainWindow", "enter new password:","None"))
        self.label_22.setText(QCoreApplication.translate("VerifyMainWindow", "confirm new  password:","None"))
        self.submitchange.setText(QCoreApplication.translate("VerifyMainWindow", "submit"))
        self.label_16.setText(QCoreApplication.translate("VerifyMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">PLEASE ENTER VERIFICATION CODE</span></p></body></html>","None"))
        #self.incorrect_2.setText(_translate("VerifyMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e12534;\">hello</span></p></body></html>","None"))
        self.submit.setText(QCoreApplication.translate("VerifyMainWindow", "submit","None"))



