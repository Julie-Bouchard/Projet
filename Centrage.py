from operation import Operation
from estimateur import Estimateur
from moyenne import Moyenne
from selectionvariablecsv import SelectionVariablecsv 

class Centrage:
    def __init__(self,Liste_variable):
        self.Liste_variable=Liste_variable
    
    def transforme(self,table):
        n=len(table.lignes)+1
        p=len(table.noms_colonnes)
        for j in range (0,p):
            if table.noms_colonnes[j] in self.Liste_variable:
                colonne=SelectionVariablecsv(table.noms_colonnes[j]).transforme(table)# On selectionne la j ème colonne de notre base de donnée 
                moyenne=Moyenne().estime(colonne)
                for i in range (1,n):
                    table.lignes[i-1][j]=float(table.lignes[i-1][j])-float(moyenne.lignes[0][0])
        return table
