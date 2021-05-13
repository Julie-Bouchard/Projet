from operation import Operation
from estimateur import Estimateur
from ecarttype import EcartType
from selectionvariablecsv import SelectionVariablecsv
from centrage import Centrage

class Normalisation:
    def __init__(self, Liste_variable):
        self.Liste_variable=Liste_variable
        
    def transforme(self,table):
        
        table=Centrage(self.Liste_variable).transforme(table)
        n=len(table.lignes)+1
        p=len(table.noms_colonnes)
        for j in range (0,p):
            if table.noms_colonnes[j] in self.Liste_variable:
                colonne=SelectionVariablecsv(table.noms_colonnes[j]).transforme(table)# On selectionne la j ème colonne de notre base de donnée
                sd=EcartType().estime(colonne)
                for i in range (1,n):
                    table.lignes[i-1][j]=float(table.lignes[i-1][j])/float(sd.lignes[0][0])
        
        return table
     
        
        
        
