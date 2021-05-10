import Statistique_descriptive as sd

class Normalisation:
    def __init__(self):
        self.normalisee="False"
        
    def normaliser(self):
        n=len(self)
        p='''nombre de variables'''
        for j in range (0,p):
            U=[individu[j] for individu in self] # On selectionne la j ème colonne de notre base de donnée
            ecart_type=sd.U.ecart_type
            for i in range (0,n):
                self[i][j]=self[i][j]/ecart_type
        self.normalisee="True"
        
        
        
