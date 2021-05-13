import random
from donnees import Donnees
from estimateur import Estimateur
from normalisation import Normalisation
from outil import Outil


class Kmeans(Estimateur):
    

    def __init__(self,nombre_classe,colonnes):
        self.nombre_classe = nombre_classe
        self.colonnes = colonnes #Liste des colonnes qui vont être utilisé pour le kmeans
        

    def estime(self,table):
        New_Table=Outil.changement_ordre(table,self.colonnes)
        nombre_variable=len(self.colonnes)
        k=self.nombre_classe
        
        for nom in self.colonnes :
            New_Table=Outil.convertisseur_str_float(New_Table,nom)
        N=Normalisation(self.colonnes)
        N.transforme(New_Table)
        n=len(New_Table.lignes)
        indice_classe=New_Table.noms_colonnes.index('Classes')
        #centres=[]
        #for i in range(k):
        #    centres.append(New_Table.lignes[i][1:(nombre_variable+1)])
        
        centres=[[int(random.random()*10) for j in range(nombre_variable)] for i in range(k)]
        classes=Outil.extrait_colonne(New_Table,'Classes')[1]
        classes2=[]
        for _ in range(len(New_Table.lignes)):
            classes2.append(-1)


        iteration=0
        while classes != classes2 and iteration<200:
            '''nb est un cap arbitraire pas trop grand pour éviter les boucles infinies si une observation oscille'''
            iteration+=1
            for s in range(len(New_Table.lignes)):
                classes2[s]=classes[s]
            #classes2=[[classes[k]] for k in range(len(New_Table.lignes))]
            for j in range (n):
                T=[] #La liste des distance de cet individu avec les centres
                for centre in centres:
                    T.append(Outil.distance(New_Table.lignes[j][1:], centre,nombre_variable))
                New_Table.lignes[j][indice_classe] = T.index(min(T))
                
            Outil.calcul_centres(New_Table,centres,k,nombre_variable,indice_classe)
            classes=Outil.extrait_colonne(New_Table,'Classes')[1]
        #print(New_Table.noms_colonnes)
        #print(New_Table.lignes)
        #table.ajouter_colonne('Classes',classes)
        print(classes)
        return New_Table


