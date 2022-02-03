
from PyQt5.QtCore import QBasicTimer, QTimer, QCoreApplication
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtCore import Qt

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from login import Ui_LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(700, 300)
        SplashScreen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self.verticalWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_title = QLabel(self.widget)
        font = QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(225, 37, 52);\n"
"font: 75 50pt \"MS Shell Dlg 2\";")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_3.addWidget(self.label_title)
        self.label_description = QLabel(self.widget)
        font =QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout_3.addWidget(self.label_description)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QWidget(self.verticalWidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setContentsMargins(40, 90, 40, 60)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n""}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(225, 37, 52), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        #self.progressBar.setMaximum(100)
        self.verticalLayout_4.addWidget(self.progressBar)
        self.label_loading = QLabel(self.widget_2)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.verticalLayout_4.addWidget(self.label_loading)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.verticalWidget, 0,Qt.AlignVCenter)
        SplashScreen.setCentralWidget(self.centralwidget)
        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)




    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", "<html><head/><body><p>AURORA</p></body></html>", None))
        self.label_description.setText(
        QCoreApplication.translate("SplashScreen","<html><head/><body><p>an eye on every detail</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))






