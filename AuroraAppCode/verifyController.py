
import sys
from threading import Timer
from PySide2 import QtCore
from PySide2.QtCore import (Qt)
from PySide2.QtGui import (QPixmap)
from PySide2.QtWidgets import *
from PyQt5 import QtCore
from verification import Ui_VerifyMainWindow
import login
import pyodbc
import pickle

class Verfifycontroller(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_VerifyMainWindow()
        self.ui.setupUi(self)
        self.t = Timer(1, self.timer)
        self.timer()
        self.ui.submit.clicked.connect(lambda: self.change())
        self.ui.submitchange.clicked.connect(lambda: self.fchangePassword())
        self.show()

    def fchangePassword(self):
        if len(self.ui.newpassword.text())==0 or len(self.ui.confirmpass.text()) ==0 :
            self.ui.incorrectv.setText("input text must not be empty! retry")
        elif len(self.ui.newpassword.text())<8 or len(self.ui.confirmpass.text()) <8 :
            self.ui.incorrectv.setText("password must be at least 8 characters! retry")
        elif self.ui.newpassword.text() != self.ui.confirmpass.text():
            self.ui.incorrectv.setText("new password does not match confirmation")
        elif any(map(str.isdigit ,self.ui.newpassword.text()))==False or any(map(str.isupper,self.ui.newpassword.text()))==False or any(map(str.isupper,self.ui.newpassword.text()))==False:
             self.ui.incorrectv.setText("password must at least include 1 number,1 lowercase character and an uppercase character")
        else:
             new=str(self.ui.newpassword.text())
             server = 'Nurkanaan\sqlexpress'
             database = 'senior'
             conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; \
                                                      SERVER=' + server + '; \
                                                      DATABASE=' + database + '; \
                                                      Trusted_Connection=yes;')
             cursor = conn.cursor()
             insert_query = "UPDATE headsInfo SET pass = ? WHERE email= ?"
             email=pickle.load(open("email.dat","rb"))
             cursor.execute(insert_query,new,email)
             conn.commit()
             self.ui.incorrectv.setText("<strong>Loading...</strong>")
             self.timer = QtCore.QTimer()
             self.timer.start(35)
             QtCore.QTimer.singleShot(3300, lambda: self.messagechange())
             QtCore.QTimer.singleShot(3400, lambda: self.ui.incorrectv.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.newpassword.setText(""))
             QtCore.QTimer.singleShot(3400, lambda: self.ui.confirmpass.setText(""))

    def logout(self):
        self.window = QMainWindow()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.showMaximized()
        self.window.show()
        self.close()
    def messagechange(self):
            m= QMessageBox()
            m.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Password changed successfully!"
                          "</span></p><p>You will logout from this device</p></body></html>")
            m.setStandardButtons(QMessageBox.Ok)
            m.setWindowTitle("AURORA")
            m.setIcon(QMessageBox.NoIcon)
            m.setWindowFlag(Qt.FramelessWindowHint)
            reply=m.exec()
            if reply == QMessageBox.Ok :
                self.logout()
    def timer(self):
        code = pickle.load(open("rand.dat","rb"))
        self.t = Timer(1, self.timer)
        self.t.start()
        if  len(self.ui.lineEdit.text()) >= 6:
            if self.ui.lineEdit.text() == str(code):

                self.ui.incorrect.setText("please press on submit to continue")
                self.ui.state.setPixmap(QPixmap("images/tick.jpg"))
            else:
                self.ui.state.setPixmap(QPixmap("images/cross.jpg"))
                self.ui.incorrect.setText("incorrect code! retry")
        else:
            self.ui.incorrect.setText("")
            self.ui.state.setPixmap(QPixmap(""))


    def change(self):
       code = pickle.load(open("rand.dat", "rb"))
       if self.ui.lineEdit.text() != str(code) and len(self.ui.lineEdit.text()) >=6:
         self.ui.state.setPixmap(QPixmap("images/cross.jpg"))
         self.ui.incorrect.setText("incorrect code! retry")
       elif len(self.ui.lineEdit.text()) < 6:
           self.ui.incorrect.setText("")
           self.ui.state.setPixmap(QPixmap(""))
       else:
        self.t.cancel()
        self.ui.incorrect.setText("please press on submit to continue")
        self.ui.state.setPixmap(QPixmap("images/tick.jpg"))
        self.timer = QtCore.QTimer()
        self.timer.start(35)
        QtCore.QTimer.singleShot(100, lambda: self.ui.incorrect.setText("Loading..."))
        QtCore.QTimer.singleShot(3400, lambda: self.ui.lineEdit.setText(""))
        QtCore.QTimer.singleShot(3500, lambda: self.ui.pages.setCurrentWidget(self.ui.changepassword))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Verfifycontroller()
        sys.exit(app.exec_())
