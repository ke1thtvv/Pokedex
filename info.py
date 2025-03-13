from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Analise import Analyse


class Ui_InfoWindow(object):
    def setupUi(self, MainWindow, num):
        Data = Analyse()
        MainWindow.setWindowTitle("POKEMON")
        MainWindow.resize(500, 700)
        MainWindow.setStyleSheet("background-color: rgb(39, 44, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # TU TE IKONY POKSOW SA KOLEJNO PONUMEROWANE a1-a151 ZROBIC AUTOMATYCZNIE W TWORZENIU BUTTONU

        self.pokemongraph = QtWidgets.QLabel(self.centralwidget)
        self.pokemongraph.setGeometry(QtCore.QRect(0, 0, 500, 250))
        self.pokemongraph.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                        "background-color: rgb(164, 185, 206);\n"
                                        "border-bottom-left-radius:35px;\n"
                                        "border-bottom-right-radius:35px;")
        self.pokemongraph.setText("")
        self.pokemongraph.setPixmap(QtGui.QPixmap(Data.GetPicture(num)))
        self.pokemongraph.setScaledContents(False)
        self.pokemongraph.setAlignment(QtCore.Qt.AlignCenter)
        self.pokemongraph.setIndent(-1)

        # W SET TEXCIE Z KEGGLA TEN NUMER Z POKEDEXU ZA #

        self.pokedexid = QtWidgets.QLabel(self.centralwidget)
        self.pokedexid.setGeometry(QtCore.QRect(445, 5, 50, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pokedexid.sizePolicy().hasHeightForWidth())
        self.pokedexid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pokedexid.setFont(font)
        self.pokedexid.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pokedexid.setText("#"+Data.GetPokedexNumber(num))

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 250, 500, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 441, 221))

        self.info1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.info1.setContentsMargins(0, 0, 0, 0)
        self.info1.setSpacing(0)

        # NAZWA POKSA TEZ TAM JEST I ZIMPORTOWAĆ

        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 255, 255);")
        self.name.setText(Data.GetName(num))
        self.name.setAlignment(QtCore.Qt.AlignCenter)


        self.layoutTYPES = QtWidgets.QHBoxLayout()

        self.frameTYPE1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frameTYPE1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTYPE1.setFrameShadow(QtWidgets.QFrame.Raised)

        self.type = QtWidgets.QLabel(self.frameTYPE1)
        if(Data.GetTypeNumber(num) == 2):
            self.type.setGeometry(QtCore.QRect(45, 20, 150, 31))
        else:
            self.type.setGeometry(QtCore.QRect(145, 20, 150, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.type.setFont(font)
        self.type.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: " + self.GetBackground(Data.GetType1(num)) + ";\n"
                                "border-radius: 15px;")
        self.type.setText(Data.GetType1(num))
        self.type.setAlignment(QtCore.Qt.AlignCenter)

        if(Data.GetTypeNumber(num) == 2):
            self.frameTYPE2 = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.frameTYPE2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frameTYPE2.setFrameShadow(QtWidgets.QFrame.Raised)

            self.type2 = QtWidgets.QLabel(self.frameTYPE2)
            self.type2.setGeometry(QtCore.QRect(15, 20, 150, 31))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            self.type2.setFont(font)
            self.type2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: " + self.GetBackground(Data.GetType2(num)) + ";\n"
                                     "border-radius: 15px;\n"
                                     # "background-color: rgb(150, 150, 150);\n"
                                     # "background-color: rgb(140, 0, 0);\n"
                                     # "background-color: rgb(177, 178, 249);\n"
                                     # "background-color: rgb(160, 0, 240);\n"
                                     "")
            self.type2.setText(Data.GetType2(num))
            self.type2.setAlignment(QtCore.Qt.AlignCenter)

        self.BaseStats = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(50)
        self.BaseStats.setFont(font)
        self.BaseStats.setStyleSheet("color: rgb(255, 255, 255);")
        self.BaseStats.setText("Bazowe Statystyki")
        self.BaseStats.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 220, 441, 211))

        self.info2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.info2.setContentsMargins(0, 0, 0, 0)

        self.layoutINFO = QtWidgets.QVBoxLayout()

        self.layoutATTACK = QtWidgets.QHBoxLayout()
        self.layoutATTACK.setSpacing(0)
        self.layoutDEFENSE = QtWidgets.QHBoxLayout()
        self.layoutDEFENSE.setSpacing(0)
        self.layoutHEALTH = QtWidgets.QHBoxLayout()
        self.layoutHEALTH.setSpacing(0)
        self.layoutSPEED = QtWidgets.QHBoxLayout()
        self.layoutSPEED.setSpacing(0)

        self.attack = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.attack.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.attack.setFont(font)
        self.attack.setStyleSheet("color: rgb(255, 255, 255);")
        self.attack.setText("ATK")
        self.attack.setAlignment(QtCore.Qt.AlignCenter)

        self.defense = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.defense.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.defense.setFont(font)
        self.defense.setStyleSheet("color: rgb(255, 255, 255);")
        self.defense.setText("DEF")
        self.defense.setAlignment(QtCore.Qt.AlignCenter)

        self.health = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.health.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.health.setFont(font)
        self.health.setStyleSheet("color: rgb(255, 255, 255);")
        self.health.setText("HP")
        self.health.setAlignment(QtCore.Qt.AlignCenter)

        self.speed = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.speed.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.speed.setFont(font)
        self.speed.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed.setText("SPD")
        self.speed.setAlignment(QtCore.Qt.AlignCenter)

        # W TYCH JAK MASZ SET PROPERTY I TA LICZBA NP 99 TO WARTOŚĆ ZIMPORTOWAC Z TEGO KEGGLA JAKOŚ AUTOMATYCZNIE

        self.ATTACKbar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ATTACKbar.setFont(font)
        self.ATTACKbar.setStyleSheet("QProgressBar {\n"
                                     "    border-radius: 8px;\n"
                                     "    background-color: rgb(213, 213, 213);\n"
                                     " }\n"
                                     "QProgressBar::chunk {   \n"
                                     "    border-radius: 8px;  \n"
                                     "    background-color: rgb(211, 58, 73);\n"
                                     " }")

        # self.ATTACKbar.setMaximum(185)
        self.ATTACKbar.setMaximum(134)
        self.ATTACKbar.setValue(Data.GetAttack(num))
        self.ATTACKbar.setFormat("%v/%m")
        self.ATTACKbar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.DEFENSEbar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.DEFENSEbar.setFont(font)
        self.DEFENSEbar.setStyleSheet("QProgressBar {\n"
                                      "    border-radius: 8px;\n"
                                      "    background-color: rgb(213, 213, 213);\n"
                                      " }\n"
                                      "QProgressBar::chunk {\n"
                                      "    border-radius: 8px;     \n"
                                      "    background-color: rgb(0, 146, 228);\n"
                                      " }")
        self.DEFENSEbar.setMaximum(180)
        self.DEFENSEbar.setValue(Data.GetDefense(num))
        self.DEFENSEbar.setFormat("%v/%m")
        self.DEFENSEbar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.HEALTHbar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.HEALTHbar.setFont(font)
        self.HEALTHbar.setStyleSheet("QProgressBar {\n"
                                     "    border-radius: 8px;\n"
                                     "    background-color: rgb(213, 213, 213);\n"
                                     " }\n"
                                     "QProgressBar::chunk {\n"
                                     "    border-radius: 8px;   \n"
                                     "    background-color: rgb(57, 142, 56);\n"
                                     " }")
        self.HEALTHbar.setMaximum(250)
        self.HEALTHbar.setValue(Data.GetHP(num))
        self.HEALTHbar.setFormat("%v/%m")
        self.HEALTHbar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.SPEEDbar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.SPEEDbar.setFont(font)
        self.SPEEDbar.setStyleSheet("QProgressBar {\n"
                                    "    border-radius: 8px;\n"
                                    "    background-color: rgb(213, 213, 213);\n"
                                    " }\n"
                                    "QProgressBar::chunk {         \n"
                                    "    border-radius: 8px;\n"
                                    "    background-color: rgb(247, 157, 1);\n"
                                    " }")
        self.SPEEDbar.setMaximum(150)
        self.SPEEDbar.setValue(Data.GetSpeed(num))
        self.SPEEDbar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SPEEDbar.setFormat("%v/%m")
        self.SPEEDbar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)

        self.info1.addWidget(self.name)
        self.layoutTYPES.addWidget(self.frameTYPE1)
        if (Data.GetTypeNumber(num) == 2):
            self.layoutTYPES.addWidget(self.frameTYPE2)
        self.info1.addWidget(self.BaseStats)
        self.layoutATTACK.addWidget(self.attack)
        self.layoutATTACK.addWidget(self.ATTACKbar)
        self.layoutDEFENSE.addWidget(self.defense)
        self.layoutDEFENSE.addWidget(self.DEFENSEbar)
        self.layoutHEALTH.addWidget(self.health)
        self.layoutHEALTH.addWidget(self.HEALTHbar)
        self.layoutSPEED.addWidget(self.speed)
        self.layoutSPEED.addWidget(self.SPEEDbar)

        self.info1.addLayout(self.layoutTYPES)
        self.layoutINFO.addLayout(self.layoutATTACK)
        self.layoutINFO.addLayout(self.layoutDEFENSE)
        self.layoutINFO.addLayout(self.layoutHEALTH)
        self.layoutINFO.addLayout(self.layoutSPEED)
        self.info2.addLayout(self.layoutINFO)
        MainWindow.setCentralWidget(self.centralwidget)

#         BO CHYBA NAJLEPIEJ ZEBY ZROBIC PETLE W KTOREJ ROBI SIE BUTTON W ZALEZNOSCI OD TEGO KTORY SIE KLIKNIE W MENU
# I IMPORTUJE SIE WTEDY TE STATYSTYKI I WSZYSTKO AUTOMATYCZNIE :))


    def GetBackground(self, type):
        thisdict = {
            "Bug": "rgb(154, 194, 55)",
            "Dark": "rgb(99, 103, 122)",
            "Dragon": "rgb(5, 119, 190)",
            "Electric": "rgb(250, 216, 91)",
            "Fairy": "rgb(243, 162, 228)",
            "Fighting": "rgb(213, 66, 93)",
            "Fire": "rgb(255, 162, 80)",
            "Flying": "rgb(151, 182, 228)",
            "Ghost": "rgb(102, 109, 189)",
            "Grass": "rgb(97, 189, 89)",
            "Ground": "rgb(173, 92, 39)",
            "Ice": "rgb(125, 213, 200)",
            "Normal": "rgb(152, 160, 163",
            "Poison": "rgb(186, 96, 209)",
            "Psychic": "rgb(255, 137, 137)",
            "Rock": "rgb(213, 190, 136)",
            "Steel": "rgb(83, 159, 169)",
            "Water": "rgb(104, 181, 227)"
        }
        return thisdict[type]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InfoWindow()
    ui.setupUi(MainWindow, 149)
    MainWindow.show()
    sys.exit(app.exec_())
