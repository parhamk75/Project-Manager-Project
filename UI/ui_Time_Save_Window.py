# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/parhamk75/GitHub/Self_Fun_Projects/Project-Manager-Project/UI/Time_Save_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 838)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.get_time_but_start = QtWidgets.QPushButton(self.centralwidget)
        self.get_time_but_start.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_time_but_start.sizePolicy().hasHeightForWidth())
        self.get_time_but_start.setSizePolicy(sizePolicy)
        self.get_time_but_start.setMinimumSize(QtCore.QSize(0, 70))
        self.get_time_but_start.setMaximumSize(QtCore.QSize(173, 16777215))
        self.get_time_but_start.setObjectName("get_time_but_start")
        self.horizontalLayout_4.addWidget(self.get_time_but_start)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit_start = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_start.setEnabled(True)
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.verticalLayout.addWidget(self.lineEdit_start)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.set_but_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_but_start.sizePolicy().hasHeightForWidth())
        self.set_but_start.setSizePolicy(sizePolicy)
        self.set_but_start.setMaximumSize(QtCore.QSize(16777215, 30))
        self.set_but_start.setObjectName("set_but_start")
        self.horizontalLayout.addWidget(self.set_but_start)
        self.reset_but_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_but_start.sizePolicy().hasHeightForWidth())
        self.reset_but_start.setSizePolicy(sizePolicy)
        self.reset_but_start.setMaximumSize(QtCore.QSize(16777215, 30))
        self.reset_but_start.setObjectName("reset_but_start")
        self.horizontalLayout.addWidget(self.reset_but_start)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_6.addWidget(self.line_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.get_time_but_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_time_but_stop.sizePolicy().hasHeightForWidth())
        self.get_time_but_stop.setSizePolicy(sizePolicy)
        self.get_time_but_stop.setMinimumSize(QtCore.QSize(0, 70))
        self.get_time_but_stop.setMaximumSize(QtCore.QSize(173, 16777215))
        self.get_time_but_stop.setObjectName("get_time_but_stop")
        self.horizontalLayout_5.addWidget(self.get_time_but_stop)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lineEdit_stop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_stop.setObjectName("lineEdit_stop")
        self.verticalLayout_2.addWidget(self.lineEdit_stop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.set_but_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_but_stop.sizePolicy().hasHeightForWidth())
        self.set_but_stop.setSizePolicy(sizePolicy)
        self.set_but_stop.setMaximumSize(QtCore.QSize(16777215, 30))
        self.set_but_stop.setObjectName("set_but_stop")
        self.horizontalLayout_3.addWidget(self.set_but_stop)
        self.reset_but_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_but_stop.sizePolicy().hasHeightForWidth())
        self.reset_but_stop.setSizePolicy(sizePolicy)
        self.reset_but_stop.setMaximumSize(QtCore.QSize(16777215, 30))
        self.reset_but_stop.setObjectName("reset_but_stop")
        self.horizontalLayout_3.addWidget(self.reset_but_stop)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.textEdit_details = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_details.setObjectName("textEdit_details")
        self.gridLayout_4.addWidget(self.textEdit_details, 2, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_Label = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Label.sizePolicy().hasHeightForWidth())
        self.comboBox_Label.setSizePolicy(sizePolicy)
        self.comboBox_Label.setEditable(False)
        self.comboBox_Label.setPlaceholderText("")
        self.comboBox_Label.setObjectName("comboBox_Label")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/parhamk75/GitHub/Self_Fun_Projects/Project-Manager-Project/UI/../ICONS/Bio-Engine.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_Label.addItem(icon, "")
        self.comboBox_Label.addItem("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/parhamk75/GitHub/Self_Fun_Projects/Project-Manager-Project/UI/../ICONS/INILAB.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_Label.addItem(icon1, "")
        self.gridLayout.addWidget(self.comboBox_Label, 0, 0, 1, 1)
        self.checkBox_SaveToFTP = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SaveToFTP.sizePolicy().hasHeightForWidth())
        self.checkBox_SaveToFTP.setSizePolicy(sizePolicy)
        self.checkBox_SaveToFTP.setChecked(True)
        self.checkBox_SaveToFTP.setTristate(False)
        self.checkBox_SaveToFTP.setObjectName("checkBox_SaveToFTP")
        self.gridLayout.addWidget(self.checkBox_SaveToFTP, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.save_but = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_but.sizePolicy().hasHeightForWidth())
        self.save_but.setSizePolicy(sizePolicy)
        self.save_but.setMinimumSize(QtCore.QSize(100, 0))
        self.save_but.setMaximumSize(QtCore.QSize(16777215, 40))
        self.save_but.setObjectName("save_but")
        self.gridLayout_2.addWidget(self.save_but, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        self.reset_but = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_but.sizePolicy().hasHeightForWidth())
        self.reset_but.setSizePolicy(sizePolicy)
        self.reset_but.setMinimumSize(QtCore.QSize(100, 0))
        self.reset_but.setMaximumSize(QtCore.QSize(16777215, 40))
        self.reset_but.setObjectName("reset_but")
        self.gridLayout_2.addWidget(self.reset_but, 1, 2, 1, 1)
        self.progressBar_Save = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_Save.setEnabled(True)
        self.progressBar_Save.setProperty("value", 0)
        self.progressBar_Save.setObjectName("progressBar_Save")
        self.gridLayout_2.addWidget(self.progressBar_Save, 0, 0, 1, 4)
        self.gridLayout_4.addLayout(self.gridLayout_2, 4, 0, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_Load = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Load.sizePolicy().hasHeightForWidth())
        self.pushButton_Load.setSizePolicy(sizePolicy)
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.gridLayout_3.addWidget(self.pushButton_Load, 0, 1, 2, 1)
        self.checkBox_LoadFromFTP = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_LoadFromFTP.sizePolicy().hasHeightForWidth())
        self.checkBox_LoadFromFTP.setSizePolicy(sizePolicy)
        self.checkBox_LoadFromFTP.setChecked(True)
        self.checkBox_LoadFromFTP.setObjectName("checkBox_LoadFromFTP")
        self.gridLayout_3.addWidget(self.checkBox_LoadFromFTP, 0, 2, 2, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "START"))
        self.get_time_but_start.setText(_translate("MainWindow", "Get time"))
        self.set_but_start.setText(_translate("MainWindow", "Set"))
        self.reset_but_start.setText(_translate("MainWindow", "Reset"))
        self.label_3.setText(_translate("MainWindow", "STOP"))
        self.get_time_but_stop.setText(_translate("MainWindow", "Get time"))
        self.set_but_stop.setText(_translate("MainWindow", "Set"))
        self.reset_but_stop.setText(_translate("MainWindow", "Reset"))
        self.comboBox_Label.setCurrentText(_translate("MainWindow", "Bio-Engine"))
        self.comboBox_Label.setItemText(0, _translate("MainWindow", "Bio-Engine"))
        self.comboBox_Label.setItemText(1, _translate("MainWindow", "Four Clovers Health"))
        self.comboBox_Label.setItemText(2, _translate("MainWindow", "INILAB"))
        self.checkBox_SaveToFTP.setText(_translate("MainWindow", "Save to FTP"))
        self.save_but.setText(_translate("MainWindow", "Save"))
        self.reset_but.setText(_translate("MainWindow", "Reset"))
        self.pushButton_Load.setText(_translate("MainWindow", "Load"))
        self.checkBox_LoadFromFTP.setText(_translate("MainWindow", "from FTP"))
