# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created: Mon Jan 19 21:34:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_form(object):
    def setupUi(self, main_form):
        main_form.setObjectName(_fromUtf8("main_form"))
        main_form.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_form.sizePolicy().hasHeightForWidth())
        main_form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        main_form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/configuration21.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_form.setWindowIcon(icon)
        self.listView = QtGui.QListView(main_form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 250, 401))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView_2 = QtGui.QListView(main_form)
        self.listView_2.setGeometry(QtCore.QRect(260, 0, 250, 401))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.pushButton = QtGui.QPushButton(main_form)
        self.pushButton.setGeometry(QtCore.QRect(525, 10, 64, 64))
        self.pushButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/zoom77.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(main_form)
        self.pushButton_2.setGeometry(QtCore.QRect(525, 90, 64, 64))
        self.pushButton_2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/settings22.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(main_form)
        self.pushButton_3.setGeometry(QtCore.QRect(525, 170, 64, 64))
        self.pushButton_3.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/check61.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(main_form)
        self.pushButton_4.setGeometry(QtCore.QRect(525, 250, 64, 64))
        self.pushButton_4.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/uparrow15.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(main_form)
        self.pushButton_5.setGeometry(QtCore.QRect(525, 330, 64, 64))
        self.pushButton_5.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/cross106.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(main_form)
        QtCore.QMetaObject.connectSlotsByName(main_form)

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(_translate("main_form", "Herramienta de Configuracion WIZnet WIZ110SR", None))