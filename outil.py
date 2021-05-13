from chargementdedonneesjson import ChargementDeDonneesjson
from operation import Operation
from datetime import datetime
from donnees import Donnees
import random


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
    
    def calcul_centres(table,centres,nombre_classe,nombre_variable,colonne_classe):
        for i in range(nombre_classe):
            population = 0
            new_centre=[0 for m in range(nombre_variable)]
            for q in range(len(table.lignes)):
                if table.lignes[q][colonne_classe] == i :
                    population += 1
                    for p in range(nombre_variable):
                        new_centre[p]+=table.lignes[q][p]
            for j in range(nombre_variable):
                if population != 0 :
                    new_centre[p]=new_centre[p]/population
                if population == 0:
                    new_centre = [int(random.random()*10) for j in range(nombre_variable)]
            centres[i]=new_centre

    def distance(X,Y,nombre_variable):
        
        distance=0
        for i in range(nombre_variable):
            distance+=(X[i]-Y[i])**2
        return(distance**(1/2))

    def extrait_colonne(table,nom_colonne):
        indice=table.noms_colonnes.index(nom_colonne)
        colonne_extraite=[]
        for ligne in table.lignes:
            colonne_extraite.append(ligne[indice])
        return (nom_colonne,colonne_extraite)

    
    def changement_ordre(table,colonnes):
        Table_bis=Donnees(['Classes'],[[0] for k in range(len(table.lignes))])
        for nom in colonnes :
            extrait=Outil.extrait_colonne(table,nom)
            Table_bis.ajouter_colonne(extrait[0],extrait[1])
           
        for nom in table.noms_colonnes :
            if nom not in colonnes :
                extrait2=Outil.extrait_colonne(table,nom)
                Table_bis.ajouter_colonne(extrait2[0],extrait2[1])
        return(Table_bis)
    
    def convertisseur_str_float(table,nom_colonnes):
        j=table.noms_colonnes.index(nom_colonnes)
        for i in range(len(table.lignes)):
            table.lignes[i][j]=float(table.lignes[i][j])
        return table
    
    
