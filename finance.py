
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 558)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 579))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(999, 600))
        self.frame_2.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 780, 120))
        self.frame_3.setMaximumSize(QtCore.QSize(900, 200))
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setStyleSheet("background-color: rgb(131, 197, 197);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(240, 20, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(300, 80, 171, 111))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(55, 65, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(181, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(500, 80, 171, 111))
        self.frame_6.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 25px;\n"
"\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(55, 65, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(100, 80, 171, 111))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(50, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(55, 65, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 191, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(60, 220, 651, 141))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(70, 69, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(47, 47, 47);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:focus {\n"
"\n"
"border:  2px solid rgb(204, 204, 204);\n"
"\n"
"}")
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 70, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"\n"
"border: 2px solid rgb(47, 47, 47);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:focus {\n"
"\n"
"border:  2px solid rgb(204, 204, 204);\n"
"\n"
"}\n"
"\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(110, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setGeometry(QtCore.QRect(430, 70, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(50, 50, 50);\n"
"border: 2px solid rgb(60, 60, 60);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(60, 60, 60);\n"
"border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"color: rgb(216, 216, 216);\n"
"border: 2px solid rgb(255, 165, 24);\n"
"color: rgb(239, 239, 239);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton.setGeometry(QtCore.QRect(430, 30, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 30, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(69, 370, 691, 155))
        self.tableWidget.setMaximumSize(QtCore.QSize(750, 200))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget { \n"
"border-radius: 25px;\n"
"border:10px ;\n"
"}")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(204, 204, 204))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(213)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finance"))
        self.label_6.setText(_translate("MainWindow", "CONTROLE "))
        self.label_2.setText(_translate("MainWindow", "Saída"))
        self.label_8.setText(_translate("MainWindow", "R$ 00,00"))
        self.label_3.setText(_translate("MainWindow", "Total"))
        self.label_9.setText(_translate("MainWindow", "R$ 00,00"))
        self.label.setText(_translate("MainWindow", "Entrada"))
        self.label_7.setText(_translate("MainWindow", "R$ 00,00"))
        self.label_4.setText(_translate("MainWindow", "Descrição"))
        self.label_5.setText(_translate("MainWindow", "Valor"))
        self.pushButton.setText(_translate("MainWindow", "Adicionar"))
        self.radioButton.setText(_translate("MainWindow", "Entrada"))
        self.radioButton_2.setText(_translate("MainWindow", "Saida"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descrição"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
