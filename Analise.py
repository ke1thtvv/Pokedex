import numpy as np
import pandas as pd


class Analyse():

    def __init__(self):
        df = pd.read_csv("pokemonStats.csv", sep=";")
        columns = df.columns.values.tolist()
        self.pokedex_number = np.array(df[columns[0]])
        self.name = np.array(df[columns[1]])
        self.status = np.array(df[columns[2]])
        self.type_number = np.array(df[columns[3]])
        self.type_1 = np.array(df[columns[4]])
        self.type_2 = np.array(df[columns[5]])
        self.hp = np.array(df[columns[6]])
        self.attack = np.array(df[columns[7]])
        self.defense = np.array(df[columns[8]])
        self.speed = np.array(df[columns[9]])

    def GetPokedexNumber(self, a):
        return str(self.pokedex_number[a])

    def GetName(self, a):
        return str(self.name[a])

    def GetStatus(self, a):
        return str(self.status[a])

    def GetTypeNumber(self, a):
        return int(self.type_number[a])

    def GetType1(self, a):
        return str(self.type_1[a])

    def GetType2(self, a):
        return str(self.type_2[a])

    def GetHP(self, a):
        return int(self.hp[a])

    def GetAttack(self, a):
        return int(self.attack[a])

    def GetDefense(self, a):
        return int(self.defense[a])

    def GetSpeed(self, a):
        return int(self.speed[a])

    def GetPicture(self, a):
        return "info/a" + str(self.pokedex_number[a]) + ".png"

    def nameList(self):
        return self.name

    def pokedexNumberList(self):
        return self.pokedex_number
