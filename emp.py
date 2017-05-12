# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kush/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog, QPixmap, QTableWidgetItem
import base64, os
import csv
fname = '/'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1130, 642)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1131, 601))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(110, 10, 131, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8("set_user"))
        self.comboBox.addItem(_fromUtf8("get_user"))
        self.comboBox.addItem(_fromUtf8("user_activity"))
        self.comboBox_2 = QtGui.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 56, 131, 31))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8("known"))
        self.comboBox_2.addItem(_fromUtf8("unknown"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.enabledChange(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 100, 131, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.enabledChange(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 150, 131, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame)
        self.lineEdit_5.enabledChange(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 200, 131, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.comboBox_3 = QtGui.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 240, 131, 31))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8("in"))
        self.comboBox_3.addItem(_fromUtf8("out"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 91, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 91, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.save = QtGui.QPushButton(self.frame)
        self.save.setGeometry(QtCore.QRect(10, 380, 99, 27))
        self.save.setObjectName(_fromUtf8("save"))
        self.Quit = QtGui.QPushButton(self.frame)
        self.Quit.setGeometry(QtCore.QRect(150, 380, 99, 27))
        self.Quit.setObjectName(_fromUtf8("Quit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 340, 99, 27))
        self.pushButton.setText(_fromUtf8("Save"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 111, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(260, 0, 571, 411))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label0 = QtGui.QLabel(self.frame_2)
        self.label0.setGeometry(QtCore.QRect(100, 30, 371, 351))
        self.label0.setText(_fromUtf8(""))
        self.label0.setObjectName(_fromUtf8("label0"))
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(280, 0, 141, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tableWidget = QtGui.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 420, 831, 161))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(20)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1130, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getparams)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getpar)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getfile)
        QtCore.QObject.connect(self.Quit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getparams(self):
        global fname
        with open(fname, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read())
        shost = {"mode" : self.comboBox.currentText(), "user_type" : self.comboBox_2.currentText(), "name" : self.lineEdit_3.text(),
                 "department" : self.lineEdit_4.text(), 'employee_id': self.lineEdit_5.text(),
                 "entry_type" : self.comboBox_3.currentText(), "image" : encoded_image}
        return shost

    def getpar(self):
        with open('/home/kush/Desktop/FaceTrack/data/names.csv', mode='rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')  # use csv module to parse in the header
            rfd_header = reader.next()
            print "header:\n"
            print rfd_header
            for row, col in enumerate(reader):
                for i in range(len(col)):
                    self.tableWidget.setItem(row, i, QTableWidgetItem(col[i]))
                    # self.tableWidget.setItem(0, 1, QTableWidgetItem(str(row[col])))
                    # self.tableWidget.setItem(0, 2, QTableWidgetItem(str(row[2])))
                    # self.tableWidget.setItem(0, 3, QTableWidgetItem(str(row[3])))
                    # self.tableWidget.setItem(0, 4, QTableWidgetItem(str(row[4])))
                    # self.tableWidget.setItem(0, 5, QTableWidgetItem(str(row[5])))


    def getfile(self):
        global fname
        fname = QFileDialog.getOpenFileName(None, 'Open file',
                                            '/home/kush/Desktop/FaceTrack/Face',
                                            "Image files (*.jpg *.gif *.jpeg *.png)")
        self.label0.setPixmap(QPixmap(fname))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Mode", None))
        self.label_2.setText(_translate("MainWindow", "User Type", None))
        self.label_3.setText(_translate("MainWindow", "Name", None))
        self.label_4.setText(_translate("MainWindow", "Department", None))
        self.label_5.setText(_translate("MainWindow", "Employee ID", None))
        self.label_6.setText(_translate("MainWindow", "Entry Type", None))
        self.save.setText(_translate("MainWindow", "Save ", None))
        self.Quit.setText(_translate("MainWindow", "Quit", None))
        self.pushButton.setText(_translate("MainWindow", "Browser", None))
        self.label_8.setText(_translate("MainWindow", "Image Browser..", None))
        self.label_10.setText(_translate("MainWindow", "Employee Image", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "set_user", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "get_user", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "user_activity", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "known", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "unknown", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "in", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "out", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Empolyee Id", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Department", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Image", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time_in", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time_out", None))