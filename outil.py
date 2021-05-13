from chargementdedonneesjson import ChargementDeDonneesjson
from operation import Operation
from datetime import datetime


class Outil(Operation):
    def __init__(self):
        pass
    
    def chercher_vacances(vacances, annee_scolaire):
        VacancesScolaires=ChargementDeDonneesjson("C:/Users/maroi/Projet_td/Projet/VacancesScolaires.json").transforme()
        Liste=VacancesScolaires['Calendrier']
        L=[]
        for k in range(len(Liste)):
            if Liste[k]["Description"]==vacances:
                L.append(k)
            
        for k in range(len(L)):
            if Liste[L[k]]["annee_scolaire"]==annee_scolaire:
                indice=L[k]
            
        return(Liste[indice])
        
    def convertirdate(datestr):
        #Exemple de datestr : "2020-03-19"
        return datetime.strptime(datestr,"%Y-%m-%d")
    
    
