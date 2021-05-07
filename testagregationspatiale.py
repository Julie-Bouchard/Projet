# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:38:34 2021

@author: id1776
"""

def selectionvariable(Donnees,nom_variable):
        variable=[]
        for j in range(len(Donnees[0])):
            if Donnees[0][j]==nom_variable:
                for i in range(len(Donnees)):
                    variable.append([Donnees[i][j]])
        return variable

def reg_dep(Donnees,echelle1):
        res={}
        for i in Tableau2["Academie"]:
            res[i["Code_Dpt"]] = i["Region"]
        departement=selectionvariable(Donnees,echelle1)
        region=[]
        for dep in departement:
            if dep!="dep":
                region.append(res["dep"])
            else:
                return False
        new=Donnees[:]
        j=new[0].index(echelle1)
        new[0][j]="region"
        for i in range(1,len(Donnees)):
            new[i][j]=region[i]
        return new
        
reg_dep(Tableau1,"dep")

res=[]
for i in range(107):
    res.append({"Code_Dpt":Tableau2["Academie"][i]["Code_Dpt"],"Region":Tableau2["Academie"][i]["Region"]})
print(res)