
import verifyController
import pyodbc
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject,QSize,Qt)
from PySide2.QtGui import (QCursor, QFont,QIcon)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import cameras
import pickle
import smtplib
from random import randint
import PyQt5

class Ui_LoginWindow(object):

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("MainWindow")
        LoginWindow.resize(1000, 1000)
        LoginWindow.showMaximized()
        sizePolicy = QtWidgets.QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon =QIcon()
        #icon.addPixmap(QPixmap("e9b4c65fb45f70ad1b573f67e486d91c.jpg"), QIcon.Normal , QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("QMainWindow{background-image: url(images/new.png);}")
        LoginWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(LoginWindow)
        self.roomnumber = QComboBox()
        self.roomnumber.setObjectName("roomnumber")
        self.cameradep = QComboBox()
        self.cameradep.setObjectName("cameradep")
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(200, 10, 200, 30)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial Black")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 35pt \"Arial Black\";")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 87 11pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(100, 30, 100, 10)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QLineEdit(self.verticalWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QLineEdit(self.verticalWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.incorrect = QLabel(self.verticalWidget)
        self.incorrect.setText("")
        self.incorrect.setObjectName("incorrect")
        self.incorrect.setStyleSheet("color: rgb(225, 37, 52);\n"
                       "font: 87 10pt \"Arial Black\";")
        self.verticalLayout_2.addWidget(self.incorrect)
        self.verticalWidget_2 = QWidget(self.verticalWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QSize(200, 121))
        self.verticalWidget_2.setBaseSize(QSize(10, 0))
        self.verticalWidget_2.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setContentsMargins(30, 0, 30, 30)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QPushButton(self.verticalWidget_2)
        self.pushButton.setStyleSheet("background-color: rgb(225, 37, 52);\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.verticalWidget_2)
        self.pushButton_2.setStyleSheet("font: italic 11pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 85, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.verticalWidget_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout.addWidget(self.verticalWidget, 0,Qt.AlignHCenter|Qt.AlignVCenter)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)
        QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate =QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("MainWindow", "login","None"))
        self.label.setText(_translate("MainWindow", "LOGIN","None"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Enter Username</p></body></html>","None"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/>Enter Password</p></body></html>","None"))
        self.pushButton.setText(_translate("MainWindow", "Submit","None"))
        self.pushButton_2.setText(_translate("MainWindow", "forgot password?","None"))
        self.pushButton.clicked.connect(lambda:self.open_window(LoginWindow))
        self.pushButton_2.clicked.connect(lambda:self.send_email(LoginWindow))

    def open_window(self,LoginWindow):
        if len(self.lineEdit_2.text()) == 0:
                self.incorrect.setText("empty email field")
        elif len(self.lineEdit.text()) == 0:
                self.incorrect.setText("empty password field")
        else:
                server='Nurkanaan\sqlexpress'
                database='senior'
                conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                      SERVER='+server+'; \
                                      DATABASE='+database+'; \
                                      Trusted_Connection=yes;')
                cursor = conn.cursor()
                insert_query = "Select * from headsInfo where email=? and pass=?"
                cursor.execute(insert_query,self.lineEdit_2.text(), self.lineEdit.text())
                result = cursor.fetchall()
                conn.commit()
                if len(result) == 0:
                    self.incorrect.setText("invalid email/password!")
                    server = 'Nurkanaan\sqlexpress'
                    database = 'senior'
                    conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                         SERVER=' + server + '; \
                                                         DATABASE=' + database + '; \
                                                         Trusted_Connection=yes;')
                    cursor = conn.cursor()
                    insert_query = "Select * from administratorr where email=? and pass=?"
                    cursor.execute(insert_query, self.lineEdit_2.text(), self.lineEdit.text())
                    result = cursor.fetchall()
                    conn.commit()
                    if len(result)==0:
                        self.incorrect.setText("invalid email/password!")
                    else:
                        pickle.dump("no", open("sc.dat", "wb"))
                        pickle.dump(self.lineEdit_2.text(),open("email.dat" , "wb"))
                        self.window = PyQt5.QtWidgets.QMainWindow()
                        self.ui = cameras.Ui_CameraMainWindow()
                        self.ui.setupUi(self.window)
                        self.window.show()
                        LoginWindow.close()
                else:
                    pickle.dump("no", open("sc.dat", "wb"))
                    pickle.dump(self.lineEdit_2.text(), open("email.dat", "wb"))
                    self.window = PyQt5.QtWidgets.QMainWindow()
                    self.ui = cameras.Ui_CameraMainWindow()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    LoginWindow.close()

    def send_email(self,LoginWindow):
        if len(self.lineEdit_2.text()) == 0:
                self.incorrect.setText("empty email field")
        else:
               server = 'Nurkanaan\sqlexpress'
               database = 'senior'
               conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                   SERVER=' + server + '; \
                                                   DATABASE=' + database + '; \
                                                   Trusted_Connection=yes;')
               cursor = conn.cursor()
               insert_query = "Select email from headsInfo where email=?"
               cursor.execute(insert_query, self.lineEdit_2.text())
               result = cursor.fetchall()
               if len(result) == 0:
                        self.incorrect.setText("invalid email/password!")
               else:
                   try:
                        self.incorrect.setText("<strong>Loading...</strong>")
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.ehlo()
                        server.starttls()
                        server.login('AuroraCameraApplication@gmail.com', 'Aurora1234')
                        rand = randint(100000, 999999)
                        pickle.dump(rand, open("rand.dat", "wb"))
                        print(rand)
                        subject = "Recover Password"
                        msg = "your recovery code is: " + str(rand) + " \nplease enter this code in the page that opened in the application"
                        message = 'Subject: {}\n\n{}'.format(subject, msg)
                        #str(self.lineEdit_2.text())
                        server.sendmail('AuroraCameraApplication@gmail.com',str(self.lineEdit_2.text()), message)
                        server.quit()
                        self.timer = QtCore.QTimer()
                        self.timer.start(35)
                        QtCore.QTimer.singleShot(2000,lambda: self.message(LoginWindow))
                        QtCore.QTimer.singleShot(2000,lambda :self.incorrect.setText(""))
                   except:
                        m = QMessageBox()
                        msg1 = "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">No internet connection!</span></p><p>please check internet connection.</p></body></html>"
                        m.setText(msg1)
                        m.setStandardButtons(QMessageBox.Ok)
                        m.setWindowTitle("AURORA")
                        m.setIcon(QMessageBox.Information)
                        reply = m.exec()


    def message(self,LoginWindow):
        m = QMessageBox()
        msg1="<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">recovery code sent to: "+str(self.lineEdit_2.text())+ " </span></p><p>     please follow instructions in sent email</p></body></html>"
        m.setText(msg1)
        m.setStandardButtons(QMessageBox.Ok)
        m.setWindowTitle("AURORA")
        m.setIcon(QMessageBox.NoIcon)
        m.setWindowFlag(Qt.FramelessWindowHint)
        reply = m.exec()
        if reply == QMessageBox.Ok:
            self.open(LoginWindow)

    def open(self,LoginWindow):
        pickle.dump(self.lineEdit_2.text(), open("email.dat", "wb"))
        self.window = QtWidgets.QMainWindow()
        self.ui = verifyController.Verfifycontroller()
        LoginWindow.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
