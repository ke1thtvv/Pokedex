from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from info import Ui_InfoWindow
from functools import partial


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setWindowTitle("MENU")
        MenuWindow.resize(1000, 800)
        # MenuWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MenuWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MenuWindow.setStyleSheet("background-color: rgb(60, 67, 74);")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setStyleSheet("QScrollBar:vertical{\n"
                                         "    border: none;\n"
                                         "    border-radius: 0px;\n"
                                         "    width: 15px;\n"
                                         "    margin: 0 0 0 0;\n"
                                         "    background-color: rgb(60, 67, 74);\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical{\n"
                                         "    background-color: rgb(50, 56, 62);\n"
                                         "    border-radius: 7px;\n"
                                         "    min-height: 30px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover{\n"
                                         "    background-color: rgb(40, 45, 50);\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:pressed{\n"
                                         "    background-color: rgb(34, 39, 43);\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical{\n"
                                         "    border: none;\n"
                                         "    background-color: rgb(35, 39, 43);\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
                                         "    background-color: rgb(60, 67, 74);\n"
                                         "}")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setGeometry(QtCore.QRect(0, -102, 983, 17868))
        self.VLayout = QtWidgets.QVBoxLayout(self.scrollWidget)

        self.frame = QtWidgets.QFrame(self.scrollWidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(963, 17850))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 981, 17802))

        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(50)

        self.buttonlist = []
        for i in range (0,50):
            for j in range (0,3):
                btn = QtWidgets.QPushButton(self.gridLayoutWidget)
                btn.setMaximumSize(QtCore.QSize(220, 300))
                btn.setStyleSheet("QPushButton{\n"
                                  "    background-color: rgb(51, 57, 63);\n"
                                  "    border-radius: 15px;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "    background-color: rgb(47, 52, 58);\n"
                                  "    border-radius: 15px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color: rgb(45, 50, 56);\n"
                                  "    border-radius: 15px;\n"
                                  "}")
                btn.setText("")
                img = (1+i*3+j)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(f"pokemons/{img}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                btn.setIcon(icon)
                btn.setIconSize(QtCore.QSize(200, 300))
                self.grid.addWidget(btn, i, j, 1, 1)
                self.buttonlist.append(btn)

        for index, button in enumerate(self.buttonlist):
            button.clicked.connect(partial(self.OpenWindow, index))

        Lbtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        Lbtn.setMaximumSize(QtCore.QSize(220, 300))
        Lbtn.setStyleSheet("QPushButton{\n"
                               "    background-color: rgb(51, 57, 63);\n"
                               "    border-radius: 15px;\n"
                               "}\n"
                               "QPushButton:hover{\n"
                               "    background-color: rgb(47, 52, 58);\n"
                               "    border-radius: 15px;\n"
                               "}\n"
                               "QPushButton:pressed{\n"
                               "    background-color: rgb(45, 50, 56);\n"
                               "    border-radius: 15px;\n"
                               "}")
        Lbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"pokemons/151.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Lbtn.clicked.connect(lambda: self.OpenWindow(150))
        Lbtn.setIcon(icon)
        Lbtn.setIconSize(QtCore.QSize(200, 300))
        self.grid.addWidget(Lbtn, 50, 1, 1, 1)

        self.frameUP = QtWidgets.QFrame(self.centralwidget)
        self.frameUP.setGeometry(QtCore.QRect(1, 1, 70, 70))
        self.frameUP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameUP.setFrameShadow(QtWidgets.QFrame.Raised)

        # self.btnCLOSE = QtWidgets.QPushButton(self.frameUP)
        # self.btnCLOSE.setGeometry(QtCore.QRect(10, 10, 30, 30))
        # self.btnCLOSE.setStyleSheet("QPushButton{\n"
        #                         "    background-color: rgb(51, 57, 63);\n"
        #                         "    border-radius: 5px;\n"
        #                         "}\n"
        #                         "QPushButton:hover{\n"
        #                         "    background-color: rgb(47, 52, 58);\n"
        #                         "    border-radius: 5px;\n"
        #                         "}\n"
        #                         "QPushButton:pressed{\n"
        #                         "    background-color: rgb(45, 50, 56);\n"
        #                         "    border-radius: 5px;\n"
        #                         "}")
        # self.btnCLOSE.setText("")
        # iconx = QtGui.QIcon()
        # iconx.addPixmap(QtGui.QPixmap("icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btnCLOSE.setIcon(iconx)
        # self.btnCLOSE.setIconSize(QtCore.QSize(20, 20))
        # self.btnCLOSE.clicked.connect(lambda: app.exit())

        self.VLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollWidget)
        MenuWindow.setCentralWidget(self.centralwidget)

    def OpenWindow(self, num):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self.window, num)
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())
