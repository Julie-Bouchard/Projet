from operation import Operation
from transformation import Transformation
from donnees import Donnees
from chargementdedonneesjson import ChargementDeDonneesjson
from selectionvariablecsv import SelectionVariablecsv


class AgregationSpatiale_reg_dep(Transformation):
   def __init__(self,echelle, Liste_agregat_bis, emplacement_json):
        self.echelle=echelle
        self.Liste_agregat_bis=Liste_agregat_bis
        self.emplacement_json=emplacement_json
   
    
   def transforme(self,table):
        
        #On réalise un travail préliminaire qui permet d'avoir une dictionnaire qui lie Departement et région
        Tableau1=ChargementDeDonneesjson(self.emplacement_json)
        Tableau2=ChargementDeDonneesjson.transforme(Tableau1)
        res={}
        for i in Tableau2["Academie"]:
            res[i["Code_Dpt"]] = i["Region"]
        
        #Avant de réaliser l'agrégation on crée une table intermediaire où à la place
        #des département on aura le nom des régions associés
        
        #departement1=SelectionVariablecsv(self.table,self.echelle)
        #departement2=SelectionVariablecsv.transforme(departement1)
        departement=[]
        
        
        s=table.noms_colonnes.index(self.echelle)
        for i in range (0, len(table.lignes)):
            departement.append(table.lignes[i][s])
        
        region=[]
        for depp in departement:
            region.append(res['{}'.format(depp)])
        
        '''
        new=[[]*len(self.table.noms_colonnes)]*(len(self.table.lignes)+1)
        for i in range (len(self.table.lignes)+1):
            print(new)
            for j in range(len(self.table.noms_colonnes)):
                new[i].append(self.table.lignes[i-1][j])
                
        '''
        
        new=[table.noms_colonnes]
        #à remodifier pour copier par element et non par liste
        new+=[table.lignes[i] for i in range (0, len(table.lignes))]
        '''
        new=[[None]*len(self.table.noms_colonnes)]*(len(self.table.lignes)+1)
        print(new)
        for i in range (0,len(self.table.lignes)):
            for j in range (len(self.table.noms_colonnes)):
                new[i+1][j]=self.table.lignes[i][j]
        #for j in range(len(self.table.noms_colonnes)):
        #    new[0][j]=self.table.noms_colonnes[j]
        print(new)
        
        '''
        j=new[0].index(self.echelle)
        new[0][j]="region"
        
        
        
        for i in range(1,len(table.lignes)+1):
            new[i][j]=region[i-1]
        data=Donnees(new[0],new[1:])
        
        
        #Maintenant on crée la table finale où on réalise l'agrégation
        Table_agre=Donnees([],[[]])
        Table_agre.noms_colonnes=data.noms_colonnes
        Table_agre.enlever_ligne(0)
        
        #Deux listes qui seront utile
        #Complement est la liste composé des indices des variables qui ne sont pas des agregats
        #Present est une liste qui permet de savoir si une region (en + des autres agregats) est bien dans la table final
        #Si c'est le cas il suffira d'appliquer la fonction d'agregation aux autres variables
        Present=[]
        Complement=[]
        for k in range(len(data.noms_colonnes)):
            if k!=data.noms_colonnes.index("region") and k not in self.Liste_agregat_bis:
                Complement.append(k)
        
        for k in range(len(data.lignes)): 
            L=[data.lignes[k][0]]
            for h in range(len(self.Liste_agregat_bis)):
                L.append(data.lignes[k][self.Liste_agregat_bis[h]])
            
            if L not in Present :
                
                Table_agre.ajouter_ligne(data.lignes[k])
                Present.append(L)
            else:
                
                indice=None
                #On commence par chercher à quel ligne se trouve L dans la Table_agre
        
                for f in range(len(Table_agre.lignes)):
                    Verif=[Table_agre.lignes[f][0]]
                    for q in self.Liste_agregat_bis:
                        Verif.append(Table_agre.lignes[f][q])
                        
                    if L==Verif:
                        indice=f
                
                for i in Complement:
                    Table_agre.lignes[indice][i]=str(int(Table_agre.lignes[indice][i])+int(data.lignes[k][i]))
        return Table_agre
