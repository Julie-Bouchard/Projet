# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:25:37 2021

@author: id1776
"""


from transformation import Transformation
from donnees import Donnees

class AgregationSpatiale_reg_dep(Transformation):
    def __init__(self,table,echelle):
        self.table=table
        self.echelle=echelle
    def transforme(self):
        Tableau1=ChargementDeDonneesjson("P:/ProjetTraitement/VacancesScolaires.json")
        Tableau2=ChargementDeDonneesjson.transforme(Tableau1)
        res={}
        for i in Tableau2["Academie"]:
            res[i["Code_Dpt"]] = i["Region"]
        departement1=SelectionVariablecsv(self.table,self.echelle)
        departement2=SelectionVariablecsv.transforme(departement1)
        region=[]
        for depp in departement2.lignes:
            region.append(res['{}'.format(depp[0])])
        new=[self.table.noms_colonnes]
        new+=[self.table.lignes[i] for i in range (0, len(self.table.lignes))]
        j=new[0].index(self.echelle)
        new[0][j]="region"
        for i in range(1,len(self.table.lignes)+1):
            new[i][j]=region[i-1]
        data=Donnees(new[0],new[1:])
        return data