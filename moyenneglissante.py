# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:28:58 2021

@author: id1776
"""

from transformation import Transformation
from estimateur import Estimateur
from donnees import Donnees
from datetime import datetime

class MoyenneGlissante(Transformation):
    def __init__(self,table,nom_variable,periode):
        self.table=table
        self.periode=periode #nombre impair
        self.nom_variable=nom_variable
    def transforme(self):
        mg=[]
        j=self.table.noms_colonnes.index("jour")
        v=self.table.noms_colonnes.index(self.nom_variable)
        for i in range(len(self.table.lignes)+1):
            #Si la date est proche du début ou de la fin des données, on met une valeur manquante
            if convertirdate(self.table.lignes[i][j]) - datetime.timedelta((self.periode-1)/2) < convertirdate(self.table.lignes[0][j]) or convertirdate(self.table.lignes[i][j]) + datetime.timedelta((self.periode-1)/2) > convertirdate(self.table.lignes[-1][j]):
                mg.insert(i,None)
            else:
                donneesperiode=[[self.nom_variable]]
                #On compare les valeurs des autres variables
                l=self.table.noms_colonnes.index("dep") or l=self.table.noms_colonnes.index("numReg") or l=self.table.noms_colonnes.index("reg")
                m=self.table.noms_colonnes.index("sexe") or n=self.table.noms_colonnes.index("cl_age90")
                for k in range(len(self.table.lignes)+1):
                    #Pour faire la moyenne, on conserve seulement les valeurs du même département, de la même région, du même sexe, de la même classe d'âge
                    #On prend les valeurs qui sont dans la bonne période
                    if self.table.lignes[k][l]==self.table.lignes[i][l] and self.table.lignes[k][m]==self.table.lignes[i][m] and convertirdate(self.table.lignes[k][j]) >= convertirdate(self.table.lignes[i][j]) - datetime.timedelta((self.periode-1)/2) and convertirdate(self.table.lignes[k][j]) <= convertirdate(self.table.lignes[i][j]) + datetime.timedelta((self.periode-1)/2):
                        donneesperiode.append(self.table.lignes[k][v])
                dataperiode=Donnees(donneesperiode[0],donneesperiode[1:])
                mg.insert(i,Moyenne.estime(dataperiode))
        res=Donnees.ajouter_colonne("moyenne glissante" + self.nom_variable, mg, position = -1)
        return res