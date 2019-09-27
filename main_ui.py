# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Face_Recognition_window(object):
    def setupUi(self, Face_Recognition_window):
        Face_Recognition_window.setObjectName("Face_Recognition_window")
        Face_Recognition_window.resize(966, 790)
        Face_Recognition_window.setMinimumSize(QtCore.QSize(100, 50))
        Face_Recognition_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Face_Recognition_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 823, 637))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lab_frame = QtWidgets.QLabel(self.layoutWidget)
        self.lab_frame.setMinimumSize(QtCore.QSize(641, 481))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lab_frame.setFont(font)
        self.lab_frame.setToolTip("")
        self.lab_frame.setTextFormat(QtCore.Qt.RichText)
        self.lab_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_frame.setObjectName("lab_frame")
        self.verticalLayout_4.addWidget(self.lab_frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_selecFile = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecFile.setFont(font)
        self.lab_selecFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecFile.setObjectName("lab_selecFile")
        self.verticalLayout_2.addWidget(self.lab_selecFile)
        self.lab_faceNum = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_faceNum.setFont(font)
        self.lab_faceNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_faceNum.setObjectName("lab_faceNum")
        self.verticalLayout_2.addWidget(self.lab_faceNum)
        self.lab_faceNum_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_faceNum_2.setFont(font)
        self.lab_faceNum_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_faceNum_2.setObjectName("lab_faceNum_2")
        self.verticalLayout_2.addWidget(self.lab_faceNum_2)
        self.lab_trainBar = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_trainBar.setFont(font)
        self.lab_trainBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_trainBar.setObjectName("lab_trainBar")
        self.verticalLayout_2.addWidget(self.lab_trainBar)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_selectFile = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_selectFile.setObjectName("comboBox_selectFile")
        self.verticalLayout.addWidget(self.comboBox_selectFile)
        self.lab_faceNumShow = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_faceNumShow.setFont(font)
        self.lab_faceNumShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_faceNumShow.setObjectName("lab_faceNumShow")
        self.verticalLayout.addWidget(self.lab_faceNumShow)
        self.lab_faceNumDisplay = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_faceNumDisplay.setFont(font)
        self.lab_faceNumDisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_faceNumDisplay.setObjectName("lab_faceNumDisplay")
        self.verticalLayout.addWidget(self.lab_faceNumDisplay)
        self.progressBar_trainBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar_trainBar.setProperty("value", 24)
        self.progressBar_trainBar.setObjectName("progressBar_trainBar")
        self.verticalLayout.addWidget(self.progressBar_trainBar)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_delFace = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_delFace.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_delFace.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_delFace.setFont(font)
        self.btn_delFace.setObjectName("btn_delFace")
        self.gridLayout.addWidget(self.btn_delFace, 5, 0, 1, 1)
        self.btn_openCamera = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_openCamera.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_openCamera.setFont(font)
        self.btn_openCamera.setObjectName("btn_openCamera")
        self.gridLayout.addWidget(self.btn_openCamera, 0, 0, 1, 1)
        self.btn_train = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_train.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_train.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_train.setFont(font)
        self.btn_train.setObjectName("btn_train")
        self.gridLayout.addWidget(self.btn_train, 3, 0, 1, 1)
        self.btn_recogniton = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_recogniton.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_recogniton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_recogniton.setFont(font)
        self.btn_recogniton.setObjectName("btn_recogniton")
        self.gridLayout.addWidget(self.btn_recogniton, 4, 0, 1, 1)
        self.btn_takePhoto = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_takePhoto.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_takePhoto.setFont(font)
        self.btn_takePhoto.setObjectName("btn_takePhoto")
        self.gridLayout.addWidget(self.btn_takePhoto, 2, 0, 1, 1)
        self.btn_addFace = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_addFace.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_addFace.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_addFace.setFont(font)
        self.btn_addFace.setAutoRepeatInterval(100)
        self.btn_addFace.setObjectName("btn_addFace")
        self.gridLayout.addWidget(self.btn_addFace, 1, 0, 1, 1)
        self.btn_refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_refresh.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_refresh.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setObjectName("btn_refresh")
        self.gridLayout.addWidget(self.btn_refresh, 6, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        Face_Recognition_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Face_Recognition_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Face_Recognition_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Face_Recognition_window)
        self.statusbar.setObjectName("statusbar")
        Face_Recognition_window.setStatusBar(self.statusbar)
        self.actionAdd_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionAdd_Person.setObjectName("actionAdd_Person")
        self.actionDelete_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelete_Person.setObjectName("actionDelete_Person")
        self.actionInstructions = QtWidgets.QAction(Face_Recognition_window)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionExit = QtWidgets.QAction(Face_Recognition_window)
        self.actionExit.setObjectName("actionExit")
        self.actionauthor = QtWidgets.QAction(Face_Recognition_window)
        self.actionauthor.setObjectName("actionauthor")
        self.menuFile.addAction(self.actionAdd_Person)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionauthor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Face_Recognition_window)
        QtCore.QMetaObject.connectSlotsByName(Face_Recognition_window)

    def retranslateUi(self, Face_Recognition_window):
        _translate = QtCore.QCoreApplication.translate
        Face_Recognition_window.setWindowTitle(_translate("Face_Recognition_window", "人脸识别1.0"))
        self.lab_frame.setText(_translate("Face_Recognition_window", "没有图像输入"))
        self.lab_selecFile.setText(_translate("Face_Recognition_window", "选择人脸文件夹："))
        self.lab_faceNum.setText(_translate("Face_Recognition_window", "当前人脸个数:"))
        self.lab_faceNum_2.setText(_translate("Face_Recognition_window", "当前录入照片数："))
        self.lab_trainBar.setText(_translate("Face_Recognition_window", "训练完成度："))
        self.lab_faceNumShow.setText(_translate("Face_Recognition_window", "0"))
        self.lab_faceNumDisplay.setText(_translate("Face_Recognition_window", "0"))
        self.btn_delFace.setText(_translate("Face_Recognition_window", "删除人脸"))
        self.btn_openCamera.setText(_translate("Face_Recognition_window", "打开摄像头"))
        self.btn_train.setText(_translate("Face_Recognition_window", "提取特征"))
        self.btn_recogniton.setText(_translate("Face_Recognition_window", "开始检测"))
        self.btn_takePhoto.setText(_translate("Face_Recognition_window", "录入一张人脸"))
        self.btn_addFace.setText(_translate("Face_Recognition_window", "添加一个用户"))
        self.btn_refresh.setText(_translate("Face_Recognition_window", "刷新"))
        self.menuFile.setTitle(_translate("Face_Recognition_window", "文件"))
        self.menuHelp.setTitle(_translate("Face_Recognition_window", "帮助"))
        self.actionAdd_Person.setText(_translate("Face_Recognition_window", "添加人脸"))
        self.actionDelete_Person.setText(_translate("Face_Recognition_window", "删除人脸"))
        self.actionInstructions.setText(_translate("Face_Recognition_window", "帮助"))
        self.actionExit.setText(_translate("Face_Recognition_window", "退出"))
        self.actionauthor.setText(_translate("Face_Recognition_window", "关于作者"))

