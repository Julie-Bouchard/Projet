# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:35:22 2021

@author: maroi
"""

class Kmeans:
    def __init__(self, nombre_classe):
        self.nombre_classe=nombre_classe
        
    def algorithme(self):
        n,p=self.shape
        #On considère que notre table est sous forme de matrice.
        #Disons une matrice de taille n,p. Il y'a donc n individus et p variables.
        #La première etape consite à initialiser l'algorithme et désigner des centres au hasard
        #On selectionne les k premiers individus de la table.
        L=[] #La liste des centres mobiles à l'étape n
        for k in range (0, self.nombre_classe):
            L.append([self[k]])
        #Une fois que l'initialisation est faite il faut faire bouger les centres jusqu'à avoir une partition stable.
        while '''norme(S[k])>10**(-2)''':
            M=[] #La liste des centres mobiles à l'étape n+1
            S=[] #La liste des différence entre l'étape n et n+1
            #On partitionne maintenant notre table
            #On calcule toute les distances
            for individu in L :
                T=[]
                for centre in L:
                    #Il faut trouver une distance
                    T.append('''distance (individu, centre)''')
                    classe=T.index(min(T))
                    L[classe].append(individu)#On place les individu dans les classes associés aux centre duquel ils sont les plus proches
                    
            #On calcule maintenant les nouveaux centres
            for k in range (0, len(L)):
                moyenne=0
                for j in range (0, len (L[k])):
                    moyenne+=L[k][j]
                moyenne=moyenne/len(L[k])
                M.append(moyenne)
                S.append(L[k]-M[k])
            
            
                    