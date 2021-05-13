from transformation import Transformation
from donnees import Donnees

class AgregationSomme(Transformation):
    def __init__(self, variable_agregat, variable_operation):
        self.variable_agregat=variable_agregat
        self.variable_operation=variable_operation
        
    def transforme(self, table):
        
        Dictionnaire={}
        U=[]
        j=table.noms_colonnes.index(self.variable_agregat)
        for i in range (0, len(table.lignes)):
            U.append(table.lignes[i][j])
        
        #U=SelectionVariablecsv.transforme(SelectionVariablecsv(self.table1, self.variable_cle))
        print(U)
        for k in range(0,len(table.lignes)):
            if U[k] in Dictionnaire:
                Dictionnaire[U[k]].append(k)
            else:
                Dictionnaire[U[k]]=[k]
        
        print(Dictionnaire)
        Table_agre=Donnees([self.variable_agregat, self.variable_operation],[[]])
        Table_agre.enlever_ligne(0)
        
        for cle in Dictionnaire:
            Table_agre.ajouter_ligne([cle, 0])
            
        p=table.noms_colonnes.index(self.variable_operation)
        for i in range(len(Table_agre.lignes)):
            for apparition in Dictionnaire[Table_agre.lignes[i][0]]:
                Table_agre.lignes[i][1]+=int(table.lignes[apparition][p])
                
        return Table_agre
