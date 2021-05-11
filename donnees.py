# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:37:32 2021
@author: id1776
"""

class Donnees():
    def __init__(self,noms_colonnes,lignes):
        self.noms_colonnes=noms_colonnes
        self.lignes=lignes
    def ajouter_ligne(self,ligne, position = -1):
        self.lignes.insert(position,ligne)
    def enlever_ligne(self,position):
        del(self.lignes[position])
    def ajouter_colonne(self,nom, colonne, position = -1):
        self.noms_colonnes.insert(position,nom)
        for i in range(len(self.lignes)):
            self.lignes[i].insert(position,colonne[i])
    def enlever_colonne(self,position=-1):
        for i in range(len(self.lignes)):
            del(self.lignes[i][position])
