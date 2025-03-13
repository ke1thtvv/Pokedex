#Gui
import sys, res
from PyQt5 import  QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import  QLabel,  QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

#klasy z innych
from Analise import Analyse
from info import Ui_InfoWindow
from menu import Ui_MenuWindow

#muzyka w tle
from pygame import mixer

#upload przetrenowanego modelu
import pathlib
from fastai.vision.all import load_learner

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
path = "train/export.pkl"
learn_inf = load_learner(path)

#Klasa potrzebna do drag n drop
class ImageLabel(QLabel):
    def __init__(self,frame):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.setFont(font)
        self.setText('\n\n Wstaw zdjęcie \n\n')
        self.setParent(frame)

    def setPixmap(self, image):
        super().setPixmap(image)




class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1118, 889)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAcceptDrops(True)
        self.setAcceptDrops(True)

        mixer.init()
        mixer.music.load('Theme_Song.wav')
        mixer.music.set_volume(0.08)
        mixer.music.play(loops=-1)

        self.centralwidget = QtWidgets.QWidget(self)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 1050, 850))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 1000, 800))
        self.label.setStyleSheet("border-image: url(:/images/poked.png);")
        self.label.setText("")


        self.btnACCEPT = QtWidgets.QPushButton(self.frame)
        self.btnACCEPT.setGeometry(QtCore.QRect(600, 250, 331, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.btnACCEPT.setFont(font)
        self.btnACCEPT.setStyleSheet("QPushButton{\n"
                                 "    background-color:rgb(38,179,0);\n"
                                 "    border-radius:15px;\n"
                                 "    color:rgb(255,255,255);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    background-color:rgb(43,204,0);\n"
                                 "    border-radius:15px;\n"
                                 "    color:rgb(255,255,255);\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:rgb(38,179,0);\n"
                                 "    border-radius:15px;\n"
                                 "    color:rgb(255,255,255);\n"
                                 "}")
        self.btnACCEPT.setText("Wybierz Samemu")
        self.btnACCEPT.clicked.connect(self.openWindow)


        self.btnX = QtWidgets.QPushButton(self.frame)
        self.btnX.setGeometry(QtCore.QRect(243, 99, 31, 31))
        self.btnX.setStyleSheet("QPushButton{\n"
                                "    border-radius: 15px;\n"
                                "    background-color:transparent;\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                "    background-color:rgb(255, 1, 2);\n"
                                "    border-radius:15px;\n"
                                "}\n"
                                "QPushButton:pressed{\n"
                                "    background-color:transparent;\n"
                                "    border-radius:15px;\n"
                                "}")
        self.btnX.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnX.setIcon(icon)
        self.btnX.setIconSize(QtCore.QSize(20, 20))
        self.btnX.clicked.connect(lambda: app.exit())

        self.btnSQUARE = QtWidgets.QPushButton(self.frame)
        self.btnSQUARE.setGeometry(QtCore.QRect(292, 99, 31, 31))
        self.btnSQUARE.setStyleSheet("QPushButton{\n"
                                     "    border-radius: 15px;\n"
                                     "    background-color:transparent;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "    background-color:rgb(254, 203, 101);\n"
                                     "    border-radius:15px;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:transparent;\n"
                                     "    border-radius:15px;\n"
                                     "}")
        self.btnSQUARE.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSQUARE.setIcon(icon1)
        self.btnSQUARE.setIconSize(QtCore.QSize(20, 20))

        self.btnMIN = QtWidgets.QPushButton(self.frame)
        self.btnMIN.setGeometry(QtCore.QRect(342, 99, 30, 31))
        self.btnMIN.setStyleSheet("QPushButton{\n"
                                  "    border-radius: 15px;\n"
                                  "    background-color:transparent;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "    background-color:rgb(50, 202, 100);\n"
                                  "    border-radius:15px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color:transparent;\n"
                                  "    border-radius:15px;\n"
                                  "}")
        self.btnMIN.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMIN.setIcon(icon2)
        self.btnMIN.setIconSize(QtCore.QSize(20, 20))
        self.btnMIN.clicked.connect(lambda: self.showMinimized())

        self.photoViewer = ImageLabel(self.frame)
        self.photoViewer.setGeometry(QtCore.QRect(120, 284, 336, 235))

        font.setPointSize(16)
        self.pokeName = QLabel(self.frame)
        self.pokeName.setGeometry(QtCore.QRect(195, 660, 191, 71))
        self.pokeName.setFont(font)


        self.setCentralWidget(self.centralwidget)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def upload_image(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.window.show()

    #Obsługa eventów
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            self.window = QtWidgets.QMainWindow()
            self.info = Ui_InfoWindow()
            self.data = Analyse()
            self.pokemonNamesList = self.data.nameList()
            self.pokemonIndexList = self.data.pokedexNumberList()
            whos_that_pokemon, _, prob = learn_inf.predict(file_path)
            self.pokeName.setText(whos_that_pokemon)
            for i in range(0, len(self.pokemonNamesList)):
                if whos_that_pokemon == self.pokemonNamesList[i] and whos_that_pokemon != "Bulbasaur":
                    self.number = self.pokemonIndexList[i - 1]
                elif whos_that_pokemon == "Bulbasaur":
                    self.number = 0
            self.info.setupUi(self.window, self.number)
            self.window.show()
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        pixmap = QPixmap(file_path).scaled(336, 235, QtCore.Qt.KeepAspectRatio)
        self.photoViewer.setPixmap(pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
