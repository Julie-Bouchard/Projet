# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:35:22 2021

@author: maroi
"""
import numpy as np


class Kmeans:
    def __init__(self, nombre_classe):
        self.nombre_classe=nombre_classe
        
    def produit_scalaire(U,V):
        #U, V deux vecteurs de même taille
        n,p=U.shape
        P=0 #Vecteur P=U-V
        for i in range (0,n):
            P+=U[i]*V[i]    
        return P[0]
            
    def norme(U):
        norm=(produit_scalaire(U,U))**(1/2)
        return norm
        
    def distance(U,V):
        S=U-V
        distance=norme(S)
        return distance
    
    def algorithme(self):
        n,p=self.shape
        #On considère que notre table est sous forme de matrice.
        #Disons une matrice de taille n,p. Il y'a donc n individus et p variables.
        #La première etape consite à initialiser l'algorithme et désigner des centres au hasard
        #On selectionne les k premiers individus de la table.
        L=[] #La liste des centres mobiles à l'étape 0
        for k in range (0, self.nombre_classe):
            L.append([self[k]])
        M=L
        S=L
        i=0
        #Une fois que l'initialisation est faite il faut faire bouger les centres jusqu'à avoir une partition stable.
        while norme(S[k])>10**(-2) and i<50 :
            i+=1
            N=M #La liste des centres mobiles à l'étape n
            M=[] #La liste des centres mobiles à l'étape n+1
            S=[] #La liste des différence entre l'étape n et n+1
            #On partitionne maintenant notre table
            #On calcule toute les distances
            for i in range (0,n) :
                T=[] #La liste des distance de cet individu avec les centres
                for centre in N:
                    #Il faut trouver une distance
                    T.append(distance (self[i], centre))
                classe=T.index(min(T))
                N[classe].append(self[i])#On place les individu dans les classes associés aux centre duquel ils sont les plus proches
                #A ce moment de l'algorithme, la partition est faite    
            #On calcule maintenant les nouveaux centres
            for k in range (0, len(N)):
                moyenne=0
                for j in range (0, len (N[k])):
                    moyenne+=N[k][j]
                moyenne=moyenne/len(N[k])
                M.append(moyenne)
                S.append(N[k][0]-M[k])
            
            
                    