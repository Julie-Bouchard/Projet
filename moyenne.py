from operation import Operation
from estimateur import Estimateur
from donnees import Donnees

class Moyenne(Estimateur):
    
    """Classe Moyenne.

    Cette classe est une sous classe de la classe Estimateur.
    Elle nous permettra de calculer la moyenne d'une variable quantitative.
    
    La Variable devra cependant être du type Donnees.

    Examples
    --------
    Premier exemple :

        >>> table=Donnees(['Prénom', 'Age'],[['Lisa', '14'], ['François', '18'], ['Pierre', '50']])
        >>> variable=SelectionVariablecsv('Age').transforme(table)
        >>> Moyenne=Moyenne().estime(variable)
        >>> Moyenne.lignes[0][0]
        27.333333333333332

    """
    
    def __init__(self):
        pass
    
    def estime(self,variable):   
        
    """Il s'agit donc de la fonction qui va calculer la moyenne

    Cette fonction retourne la moyenne d'une variable suggeré par l'utilisateur.
    Cette moyenne sera sous forme de donnée donc pour avoir un chiffre il faudra utiliser
    les attributs de la classe Donnees et donc ecrire moyenne.lignes[0][0]

    Parameters
    ----------
    variable : Donnees
        Il s'agit d'un element de Donnees.
        Mais pour être plus précis il s'agit d'un element qui aura uniquement une colonne donc
        qui sera de la forme -> Donnees(['nom_variable'],[[valeur1], [valeur2], ... , [valeur n]])

    Returns
    -------
    Donnees
        Il s'agit d'un element de Donnees mais d'une forme particuliere. Il sera de
        la forme -> Donnees(['Moyenne'],[[valeur_de_la_moyenne]]

    """  
        n= len(variable.lignes)+1
        moyenne=0
        for i in range (1,n):
            moyenne+=float(variable.lignes[i-1][0])
        moyenne= moyenne / (n-1)
        res=Donnees(['Moyenne'],[[moyenne]])
        return res

    
    
    
table=Donnees(['Prénom', 'Age'],[['Lisa', '10'], ['François', '20'], ['Pierre', '30']])
variable=SelectionVariablecsv('Age').transforme(table)
Moyenne=Moyenne().estime(variable)
Moyenne.lignes[0][0]

class moyenneTest(unittest.TestCase):
    def test_calcul(self):
        self.assertEqual(Moyenne.lignes[0][0],20)
        
unittest.main()
    
