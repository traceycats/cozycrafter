# Form implementation generated from reading ui file 'd:\tracey\Documents\code\cozycrafter\pyqt6 designer\welcome.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 195)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 361, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.maingrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.maingrid.setContentsMargins(0, 0, 0, 0)
        self.maingrid.setObjectName("maingrid")
        self.resume_project = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.resume_project.setFont(font)
        self.resume_project.setAutoFillBackground(False)
        self.resume_project.setObjectName("resume_project")
        self.maingrid.addWidget(self.resume_project, 4, 0, 1, 1)
        self.create_project = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.create_project.setFont(font)
        self.create_project.setObjectName("create_project")
        self.maingrid.addWidget(self.create_project, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("basis33")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.maingrid.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "cozy crafter"))
        self.resume_project.setText(_translate("MainWindow", "resume project"))
        self.create_project.setText(_translate("MainWindow", "new project"))
        self.label.setText(_translate("MainWindow", "welcome to cozy crafter! let\'s get crafty"))
