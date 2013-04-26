# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Apr 26 17:34:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setAcceptDrops(False)
        self.openButton.setObjectName("openButton")
        self.verticalLayout.addWidget(self.openButton)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setMovement(QtGui.QListView.Static)
        self.listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.copyButton = QtGui.QPushButton(self.centralwidget)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout.addWidget(self.copyButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "dat File Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Also accepts drag-and-drop files.", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("MainWindow", "Open a .dat file", None, QtGui.QApplication.UnicodeUTF8))
        self.copyButton.setToolTip(QtGui.QApplication.translate("MainWindow", "copy selected channel numbers into the clipboard.", None, QtGui.QApplication.UnicodeUTF8))
        self.copyButton.setText(QtGui.QApplication.translate("MainWindow", "Copy selected channel numbers", None, QtGui.QApplication.UnicodeUTF8))

