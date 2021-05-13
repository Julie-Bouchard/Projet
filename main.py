from donnees import Donnees
from transformation import Transformation
from estimateur import Estimateur
from chargementdedonneescsv import ChargementDeDonneescsv

a=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
table=ChargementDeDonneescsv.transforme(a)
table.lignes=table.lignes[:300]


a2=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-covid19-2021-03-03-17h03.csv")
tablea=ChargementDeDonneescsv.transforme(a2)
tablea.lignes=tablea.lignes[:10]

table2=Fenetrage("2020-03-19","2020-03-20").transforme(table)
print(table2.lignes)
print(table2.noms_colonnes)

table3=SelectionVariablecsv('dep').transforme(table)
print(table3.lignes)

table4=AgregationSpatiale_reg_dep('dep',[1],'C:/Users/maroi/Projet_td/Projet/VacancesScolaires.json').transforme(table)
print(table4.lignes)

table5=Jointure(table,'dep').transforme(tablea)
print(table5.noms_colonnes)
print(table5.lignes)

table6=SelectionVariablecsv('incid_hosp').transforme(table)
print(table6.lignes)

moyenne=Moyenne().estime(table6)
print(moyenne.lignes)

variance=Variance().estime(table6)
print(variance.lignes)

ecart=EcartType().estime(table6)
print(ecart.lignes)

somme=Somme().estime(table6)
print(somme.lignes)

mg=MoyenneGlissante('incid_hosp',3).transforme(table)
print(mg.lignes)


a=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
table=ChargementDeDonneescsv.transforme(a)
table.lignes=table.lignes[:300]
k=Kmeans(3, ['incid_hosp', 'incid_rea', 'incid_dc', 'incid_rad']).estime(table)
print(k.lignes)


a=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")
table=ChargementDeDonneescsv.transforme(a)
table.lignes=table.lignes[:5000]
classi=Kmeans(4, ['incid_hosp', 'incid_rea', 'incid_dc', 'incid_rad']).estime(table)
print(classi.lignes)

mgg=MoyenneGlissante('incid_hosp',3).process(table)
print(mgg.lignes)

agregat=AgregationSomme('dep', 'incid_rea').transforme(table)
print(agregat.lignes)

normalisation=Normalisation(['incid_hosp', 'incid_rea', 'incid_dc', 'incid_rad']).transforme(table)
print(normalisation.lignes)


pip=Pipeline()
pip.ajoute_etape(MoyenneGlissante('incid_hosp',3))
print(pip.Liste_Operation)
data=pip.run(table)
print(data.lignes)

'''------------------------------------------'''

##Question 1 : — Quel est le nombre total d’hospitalisations dues au Covid-19?
##On commence par charger la table avec les données qui nous interesse
##Qui est : " donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv "
## Car il suffit de sommer la colonne "incid_hosp" car il s'agit des nouvelles hospitalisation
table1=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()
pip1=Pipeline()
pip1.ajoute_etape(SelectionVariablecsv('incid_hosp'))
pip1.ajoute_etape(Somme())
resultat1=pip1.run(table1)
print(resultat1.lignes)


##Question 2: - Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers 
## jours dans chaque département?
##On commence par charger la table avec les données qui nous interesse
##Qui est : " donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv "
##Ensuite on réalise un fenetrage sur une periode de 7 jours
##Puis on réalise une agrégation par departement et on applique comme fonction d'agregation "somme"
table2=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()
pip2=Pipeline()
pip2.ajoute_etape(Fenetrage('2021-02-25', '2021-03-03'))
pip2.ajoute_etape(AgregationSomme('dep', 'incid_hosp'))
resultat2=pip2.run(table2)
print(resultat2.lignes)




##Question 3: — Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à
##              celle de la semaine dernière ?
##On commence par charger la table avec les données qui nous interesse
##Qui est : " donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv "
##On va calculer deux moyennes différentes et les comparer
##On réaliser deux fenetrage, un premier sur la periode du 17 au 24 février, 
## et un autre du 24 février au 3 mars.
## Puis on selectionne la variable "incid_hosp" et on calcule la moyenne

table3=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()
pip3a=Pipeline()
pip3a.ajoute_etape(Fenetrage('2021-02-17','2021-02-24'))
pip3a.ajoute_etape(SelectionVariablecsv('incid_hosp'))
pip3a.ajoute_etape(Moyenne())
Moyenne_premiere_semaine=pip3a.run(table3)
print(Moyenne_premiere_semaine.lignes)

pip3b=Pipeline()
pip3b.ajoute_etape(Fenetrage('2021-02-25','2021-03-03'))
pip3b.ajoute_etape(SelectionVariablecsv('incid_hosp'))
pip3b.ajoute_etape(Moyenne())
Moyenne_seconde_semaine=pip3b.run(table3)
print(Moyenne_seconde_semaine.lignes)

##Moyenne_premiere_semaine.lignes=13.810643564356436 et Moyenne_seconde_semaine.lignes=13.497878359264497
##La moyenne des nouvelles hospitalisation a diminué cette semaine par rapport à la semaine dernière


##Question 4 : — Quel est le résultat de k-means avec k = 3 sur les données des départements du mois de Janvier 2021, 
##               lissées avec une moyenne glissante de 7 jours?
table4=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()
pip4=Pipeline()
pip4.ajoute_etape(Fenetrage('2020-12-24', '2021-02-07'))
pip4.ajoute_etape(MoyenneGlissante('incid_hosp',7))
pip4.ajoute_etape(MoyenneGlissante('incid_rea',7))
pip4.ajoute_etape(MoyenneGlissante('incid_dc',7))
pip4.ajoute_etape(MoyenneGlissante('incid_rad',7))
pip4.ajoute_etape(Fenetrage('2021-01-01','2021-01-31'))
#table_intermediaire=pip4.run(table4)
#print(table_intermediaire.lignes)
pip4.ajoute_etape(Kmeans(3,['moyenneglissante_incid_hosp', 'moyenneglissante_incid_rea', 'moyenneglissante_incid_dc', 'moyenneglissante_incid_rad'] ))
resultat4=pip4.run(table4)
print(resultat4.lignes)

##Question 5 : — Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?
##On commence par charger la table avec les données qui nous interesse
##Qui est : " donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv "
##On utilise la fonction "chercher_vacance" de notre classe outil pour determiner la periode qui nous interesse
Informations=chercher_vacances("Vacances de la Toussaint", "2020-2021")
datefin=Informations['DateFin']
##On realise ensuite un fenetrage entre datefin et datefin+7 jours
table5=ChargementDeDonneescsv("C:/Users/maroi/Projet_td/Projet/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()
pip5=Pipeline()
pip5.ajoute_etape(Fenetrage('2020-11-02','2020-11-09'))
pip5.ajoute_etape(SelectionVariablecsv('incid_rea'))
pip5.ajoute_etape(Somme())
resultat5=pip5.run(table5)
print(resultat5.lignes)


VacancesScolaire['Calendrier']
Tableau2[]


print(SelectionVariablejson(VacancesScolaires,'annee_scolaire').transforme())


