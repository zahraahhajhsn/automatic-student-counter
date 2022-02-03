

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
import pickle
from settings import Ui_SettingsMainWindow
import login
import cameras
import pyodbc
import re

class SettingsMainWindow(QMainWindow):
    current = "none"

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SettingsMainWindow()
        self.ui.setupUi(self)

        self.ui.cameradep.addItem("none")
        self.ui.cameradep.addItem("Mathematics")
        self.ui.cameradep.addItem("Physics")
        self.ui.cameradep.addItem("Biology")
        self.ui.cameradep.addItem("Biochemistry")
        self.ui.cameradep.addItem("Electronics")
        self.ui.cameradep.addItem("Applied Mathematics")
        self.ui.cameradep.addItem("Chemistry")
        self.ui.cameradep.addItem("Physical Biochemistry")

        self.ui.roomdep.addItem("none")
        self.ui.roomdep.addItem("Mathematics")
        self.ui.roomdep.addItem("Physics")
        self.ui.roomdep.addItem("Biology")
        self.ui.roomdep.addItem("Biochemistry")
        self.ui.roomdep.addItem("Electronics")
        self.ui.roomdep.addItem("Applied Mathematics")
        self.ui.roomdep.addItem("Chemistry")
        self.ui.roomdep.addItem("Physical Biochemistry")

        self.t = Timer(20, self.updateCombo)
        self.ui.deleteheadb.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.deletehead))
        self.ui.addHead.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.addhead))
        self.ui.addHead.clicked.connect(lambda: self.headCombo())
        self.ui.addroom.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.addroomt))
        self.ui.addCamera.clicked.connect(lambda: self.updateCombo())
        self.ui.addCamera.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.addcamera))
        self.ui.changepassword.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.changepasswordPage))
        self.ui.logout.clicked.connect(lambda: self.messagelogout())
        self.ui.back.clicked.connect(lambda: self.back())
        self.ui.headconfirm.clicked.connect(lambda: self.faddHead())
        self.ui.deletesubmit.clicked.connect(lambda: self.fdeleteHead())
        self.ui.confirmchange.clicked.connect(lambda: self.fchangePassword())
        self.ui.camerasubmit.clicked.connect(lambda: self.faddCamera())
        self.ui.roomsubmit.clicked.connect(lambda: self.faddroom())
        self.show()
    def logout(self):
        self.window = QMainWindow()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
        self.t.cancel()
        #self.window.show()
        self.close()

    def back(self):
       self.window = QtWidgets.QMainWindow()
       self.ui = cameras.Ui_CameraMainWindow()
       self.ui.setupUi(self.window)
       self.window.show()
       self.t.cancel()
       self.close()

    def headCombo(self):
        while self.ui.headdep.count() > 0:
            self.ui.headdep.removeItem(0)
        L=["none","Mathematics","Physics","Biology","Biochemistry","Electronics","Applied Mathematics","Chemistry","Physical Biochemistry"]
        server = 'Nurkanaan\sqlexpress'
        database = 'senior'
        conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                 SERVER=' + server + '; \
                                                  DATABASE=' + database + '; \
                                                  Trusted_Connection=yes;')
        cursor = conn.cursor()
        insert_query = "Select department from headsInfo"
        cursor.execute(insert_query)
        result = cursor.fetchall()
        for row in result:
            for a in L :
                if row[0]==a:
                    L.remove(row[0])
                    break
        self.ui.headdep.addItems(L)

    def fchangePassword(self):
        server = 'Nurkanaan\sqlexpress'
        database='senior'
        conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                         SERVER='+server+'; \
                                          DATABASE='+database+'; \
                                          Trusted_Connection=yes;')
        cursor = conn.cursor()
        email=pickle.load(open("email.dat","rb"))
        insert_query = "Select pass from headsInfo where email=?"
        cursor.execute(insert_query,email)
        result = cursor.fetchone()
        prevouisdb = result[0]
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
             email = pickle.load(open("email.dat","rb"))
             insert_query = "UPDATE headsInfo SET pass = ? WHERE email= ?"
             cursor.execute(insert_query,new,email )
             conn.commit()

             self.ui.incorrectp.setText("<strong>Loading...</strong>")
             self.timer = QtCore.QTimer()
             self.timer.start(35)
             QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectp.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.previouspass.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.newpass.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.confirmnewpass.setText(""))
             QtCore.QTimer.singleShot(3300, lambda: self.messagechange())
    def faddroom(self):
        if len(self.ui.roomnumber1.text()) == 0:
            self.ui.incorrectr.setText("feild can't be empty! retry")
        elif self.ui.roomdep.currentText()=="none":
            self.ui.incorrectr.setText("please choose a valid department!")
        else:
            room=str(self.ui.roomnumber1.text())
            rdepartment=str(self.ui.roomdep.currentText())
            server = 'Nurkanaan\sqlexpress'
            database = 'senior'
            conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                   SERVER=' + server + '; \
                                   DATABASE=' + database + '; \
                                   Trusted_Connection=yes;')
            cursor = conn.cursor()
            insert_query = '''INSERT INTO room(roomNumber,department) VALUES(?,?);'''
            cursor.execute(insert_query, room,rdepartment)
            conn.commit()

            self.t.cancel()
            self.ui.incorrectc.setText("<strong>Loading...</strong>")
            self.timer = QtCore.QTimer()
            self.timer.start(35)
            QtCore.QTimer.singleShot(3300, lambda: self.messageAddRoom())
            QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectr.setText(""))
            QtCore.QTimer.singleShot(3400, lambda: self.ui.roomdep.setCurrentText("none"))
            QtCore.QTimer.singleShot(3400, lambda: self.ui.roomnumber1.setText(""))
    def faddHead(self):
        print(self.ui.heademail.text())
        print(str(self.ui.headdep.currentText()))
        if len(self.ui.headpassword.text()) == 0 or len(self.ui.headconfirmpass.text()) == 0 or len(self.ui.headname.text()) == 0 or len(self.ui.heademail.text()) == 0 :
            self.ui.incorrecth.setText("input text must not be empty! retry")
        elif str(self.ui.headdep.currentText()) == "none":
            self.ui.incorrecth.setText("please choose a valid department!")
        elif len(self.ui.headpassword.text()) < 8 or len(self.ui.headconfirmpass.text()) < 8:
            self.ui.incorrecth.setText("password must be at least 8 characters! retry")
        elif self.ui.headpassword.text() != self.ui.headconfirmpass.text():
            self.ui.incorrecth.setText("new password does not match confirmation")
        elif any(map(str.isdigit, self.ui.headpassword.text())) == False or any(
                map(str.isupper, self.ui.headpassword.text())) == False or any(
                map(str.isupper, self.ui.headpassword.text())) == False:
            self.ui.incorrecth.setText("password must at least include 1 number,1 lowercase character and an uppercase character")
        elif ("@hotmail.com" in self.ui.heademail.text()) == False and ("@gmail.com" in self.ui.heademail.text()) == False and ("@outlook.com" in self.ui.heademail.text()) == False :
            self.ui.incorrecth.setText("invalid email address!retry")

        else :
                server = 'Nurkanaan\sqlexpress'
                database='senior'
                conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                SERVER='+server+'; \
                DATABASE='+database+'; \
                Trusted_Connection=yes;')
                cursor = conn.cursor()
                insert_query = "Select * from headsInfo where email=?"
                cursor.execute(insert_query,self.ui.heademail.text())
                result = cursor.fetchall()
                if len(result) != 0:
                     self.ui.incorrecth.setText("email address exists already! retry")
                else:
                    hname=str(self.ui.headname.text())
                    heademail=str(self.ui.heademail.text())
                    headpass = str(self.ui.headpassword.text())
                    headdep=str(self.ui.headdep.currentText())
                    server = 'Nurkanaan\sqlexpress'
                    database = 'senior'
                    conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                    SERVER=' + server + '; \
                    DATABASE=' + database + '; \
                    Trusted_Connection=yes;')
                    cursor = conn.cursor()
                    insert_query = '''INSERT INTO headsInfo(name,email,pass,department) VALUES(?,?,?,?);'''
                    cursor.execute(insert_query, hname, heademail, headpass, headdep)
                    conn.commit()
                    self.ui.incorrecth.setText("<strong>Loading...</strong>")
                    self.timer = QtCore.QTimer()
                    self.timer.start(35)
                    QtCore.QTimer.singleShot(3300, lambda: self.messageAddHead())
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrecth.setText(""))
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.headpassword.setText(""))
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.headconfirmpass.setText(""))
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.heademail.setText(""))
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.headname.setText(""))
                    QtCore.QTimer.singleShot(3400, lambda: self.ui.headdep.setCurrentText("none"))

    def fdeleteHead(self):
        if len(self.ui.deleteemail.text()) == 0:
            self.ui.incorrectd.setText("input text must not be empty! retry")
        elif ("@hotmail.com" in self.ui.deleteemail.text()) == False and ("@gmail.com" in self.ui.deleteemail.text()) == False and ("@outlook.com" in self.ui.deleteemail.text()) == False :
            self.ui.incorrectd.setText("invalid email address! retry")
        else:
            server = 'Nurkanaan\sqlexpress'
            database='senior'
            print(self.ui.deleteemail.text())
            conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
            SERVER='+server+'; \
            DATABASE='+database+'; \
            Trusted_Connection=yes;')
            cursor = conn.cursor()
            insert_query = "Select * from headsInfo where email=?"
            cursor.execute(insert_query,str(self.ui.deleteemail.text()))
            result = cursor.fetchall()
            if not len(result) == 0:
                demail=self.ui.deleteemail.text()
                print(demail)
                server = 'Nurkanaan\sqlexpress'
                database = 'senior'
                conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                       SERVER=' + server + '; \
                       DATABASE=' + database + '; \
                       Trusted_Connection=yes;')
                cursor = conn.cursor()
                insert_query = "delete from headsInfo where email=?"
                cursor.execute(insert_query,demail)
                conn.commit()
                self.ui.incorrectd.setText("<strong>Loading...</strong>")
                self.timer = QtCore.QTimer()
                self.timer.start(35)
                QtCore.QTimer.singleShot(3300, lambda: self.messageDeleteHead())
                QtCore.QTimer.singleShot(3300, lambda: self.ui.deleteemail.setText(""))
                QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectd.setText(""))
            else:
                demail = self.ui.deleteemail.text()
                query="select * from administratorr where email=?"
                cursor.execute(query,demail)
                result=cursor.fetchall()
                print(result)
                if len(result)==0:
                   self.ui.incorrectd.setText("email address not found! retry")
                else:
                   self.ui.incorrectd.setText("This account cannot be deleted")

    def faddCamera(self):
        regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
        if len(self.ui.ip.text()) == 0:
            self.ui.incorrectc.setText("input text must not be empty! retry")
        elif (re.search(regex, self.ui.ip.text())) == None:
            self.ui.incorrectc.setText("Invalid Ip address! retry")
        if self.ui.cameradep.currentText() == "none":
            self.ui.incorrectc.setText("please choose a valid department!")

        elif self.ui.roomnumber.currentText()=="none" or self.ui.roomnumber.currentText()=="please choose a room":
            self.ui.incorrectc.setText("please choose a valid room!")

        else:
            croom=str(self.ui.roomnumber.currentText())
            cdepartment=str(self.ui.cameradep.currentText())
            ip=str(self.ui.ip.text())
            server = 'Nurkanaan\sqlexpress'
            database = 'senior'
            conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                   SERVER=' + server + '; \
                                   DATABASE=' + database + '; \
                                   Trusted_Connection=yes;')
            cursor = conn.cursor()
            insert_query = "insert into cameraInfo(roomNumber,department,ip) values (?,?,?)"
            cursor.execute(insert_query, croom,cdepartment,ip)
            conn.commit()
            self.t.cancel()
            self.ui.incorrectc.setText("<strong>Loading...</strong>")
            self.timer = QtCore.QTimer()
            self.timer.start(35)
            QtCore.QTimer.singleShot(3300, lambda: self.messageAddCamera())
            QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectc.setText(""))
            QtCore.QTimer.singleShot(3400, lambda: self.ui.cameradep.setCurrentText("none"))
            QtCore.QTimer.singleShot(3450, lambda: self.ui.roomnumber.setCurrentText("none"))

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
    def messageAddRoom(self):
        m = QMessageBox()
        m.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Room added successfully!</span></p>"
            "<p> </p></body></html>")
        m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        m.setWindowTitle("AURORA")
        m.setIcon(QMessageBox.NoIcon)
        reply = m.exec()
        if reply == QMessageBox.Ok:
            self.ui.pages.setCurrentWidget(self.ui.home)

    def messageAddHead(self):
        m = QMessageBox()
        m.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Head of department added successfully!</p>"
                  "</span><p> </p></body></html>")
        m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        m.setWindowTitle("AURORA")
        m.setIcon(QMessageBox.NoIcon)
        reply = m.exec()
        if reply == QMessageBox.Ok:
            self.ui.pages.setCurrentWidget(self.ui.home)
    def messageDeleteHead(self):
        m = QMessageBox()
        m.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Head of department removed successfully!</p>"
                  "</span><p> </p></body></html>")
        m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        m.setWindowTitle("AURORA")
        m.setIcon(QMessageBox.NoIcon)
        reply = m.exec()
        if reply == QMessageBox.Ok:
            self.ui.pages.setCurrentWidget(self.ui.home)

    def messageAddCamera(self):
        self.t.cancel()
        self.t.cancel()
        m = QMessageBox()
        m.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Camera added successfully!</span></p>"
            "<p> </p></body></html>")
        m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        m.setWindowTitle("AURORA")
        m.setIcon(QMessageBox.NoIcon)
        reply = m.exec()
        if reply == QMessageBox.Ok:
            self.ui.pages.setCurrentWidget(self.ui.home)

    def getRoom(self,department):
        L=[]
        server = 'Nurkanaan\sqlexpress'
        database = 'senior'
        conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                         SERVER=' + server + '; \
                                                          DATABASE=' + database + '; \
                                                          Trusted_Connection=yes;')
        cursor = conn.cursor()
        insert_query = "Select roomNumber from Room where department=?"
        cursor.execute(insert_query,department)
        result = cursor.fetchall()
        for row in result:
           L.append(row[0])
        self.ui.roomnumber.addItems(L)


    def updateCombo(self):
        while self.ui.roomnumber.count() > 0:
            self.ui.roomnumber.removeItem(0)

        text = self.ui.cameradep.currentText()
        if text == "none":
              self.ui.roomnumber.addItem("none")
        else:
              self.t.cancel()
              self.ui.roomnumber.addItem("please choose a room")
              self.getRoom(text)
        if self.ui.roomnumber.currentText() == "please choose a room" or self.ui.roomnumber.currentText() == "none":
              self.t = Timer(20, self.updateCombo)
              self.t.start()
        else:
              self.t = Timer(1, self.updateCombo)
              self.t.start()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsMainWindow()
    sys.exit(app.exec_())
