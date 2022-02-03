

import sys
import platform
from typing import List
from threading import  Timer
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
# GUI FILE
from headSettings import Ui_headSettingsMainWindow
#from login import Ui_LoginWindow
import login
import cameras
#from cameras import Ui_CameraMainWindow
import pyodbc
import pickle

class headSettingsMainWindow(QMainWindow):
    current = "none"
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_headSettingsMainWindow()
        self.ui.setupUi(self)
        self.ui.changepassword.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.changepasswordPage))
        self.ui.logout.clicked.connect(lambda: self.messagelogout())
        self.ui.back.clicked.connect(lambda: self.back())
        self.ui.confirmchange.clicked.connect(lambda: self.fchangePassword())
        self.show()
    def logout(self):
        self.window = QMainWindow()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
        self.window.show()
        self.close()
    def back(self):
       self.window = QtWidgets.QMainWindow()
       self.ui = cameras.Ui_CameraMainWindow()
       self.ui.setupUi(self.window)
       self.window.show()
       self.close()
    def fchangePassword(self):
        server = 'Nurkanaan\sqlexpress'
        database='senior'
        conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                         SERVER='+server+'; \
                                          DATABASE='+database+'; \
                                          Trusted_Connection=yes;')
        cursor = conn.cursor()
        email=pickle.load("email.dat","rb")
        insert_query = "Select * from headsInfo where email=?"
        cursor.execute(insert_query,email)
        result = cursor.fetchall()
        prevouisdb = result
        if len(self.ui.previouspass.text()) == 0 or len(self.ui.newpass.text())==0 or len(self.ui.confirmnewpass.text()) ==0 :
            self.ui.incorrectp.setText("input text must not be empty! retry")
        elif len(self.ui.previouspass.text()) < 8 or len(self.ui.newpass.text())<8 or len(self.ui.confirmnewpass.text()) <8 :
            self.ui.incorrectp.setText("password must be at least 8 characters! retry")
        elif self.ui.newpass.text() != self.ui.confirmnewpass.text():
            self.ui.incorrectp.setText("new password does not match confirmation")
        elif any(map(str.isdigit ,self.ui.newpass.text()))==False or any(map(str.isupper,self.ui.newpass.text()))==False or any(map(str.isupper,self.ui.newpass.text()))==False:
            self.ui.incorrectp.setText("password must at least include 1 number,1 lowercase character and an uppercase character")
        elif self.ui.previouspass.text() != prevouisdb:
            self.ui.incorrectp.setText("incorrect password")

        else:

             new=self.ui.newpass.text()
             server = 'Nurkanaan\sqlexpress'
             database = 'senior'
             conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                      SERVER=' + server + '; \
                                                       DATABASE=' + database + '; \
                                                       Trusted_Connection=yes;')
             cursor = conn.cursor()
             email = pickle.load("email.dat", "rb")
             insert_query = "UPDATE headsInfo SET pass = ? WHERE email= ?"
             cursor.execute(insert_query,new,email )

             self.ui.incorrectp.setText("<strong>Loading...</strong>")
             self.timer = QtCore.QTimer()
             self.timer.start(35)
             QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectp.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.previouspass.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.newpass.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.confirmnewpass.setText(""))
             QtCore.QTimer.singleShot(3300, lambda: self.messagechange())

    def messagechange(self):
            m= QMessageBox()
            m.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Password changed successfully!"
                          "</span></p><p>Do you want to logout from this device?</p></body></html>")
            m.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            m.setWindowTitle("AURORA")

            m.setIcon(QMessageBox.NoIcon)
            reply=m.exec()
            if reply == QMessageBox.Yes :
                self.logout()
            if reply == QMessageBox.No:
                self.ui.pages.setCurrentWidget(self.ui.home)

    def messagelogout(self):
            m= QMessageBox()
            m.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Are you sure you want to logout?</p>"
                      "</span><p> </p></body></html>")
            m.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            m.setWindowTitle("AURORA")
            m.setIcon(QMessageBox.NoIcon)
            reply=m.exec()
            if reply == QMessageBox.Yes :
                self.logout()

            if reply == QMessageBox.No:
                self.ui.pages.setCurrentWidget(self.ui.home)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = headSettingsMainWindow()
    sys.exit(app.exec_())
