import Statistique_descriptive as sd

class Centrage:
    def __init__(self):
        self.centree="False"
        
    def centrer(self):
        n=len(self)
        p='''nombre de variable'''
        for j in range (0,n):
            U=[individu[j] for individu in self] # On selectionne la j ème colonne de notre base de donnée
            moyenne=sd.U.moyenne
            for i in range (0,n):
                self[i][j]=self[i][j]-moyenne
        self.centree="True"
