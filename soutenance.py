'''----------------------------------------------------------------'''
'''                       Soutenance                               '''
'''----------------------------------------------------------------'''


##Question : Combien de décès par région sur la semaine dernière ?

#On commence par charger les données :
table=ChargementDeDonneescsv("C:/Users/maroi/Projet_Code_Final/donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv").transforme()

#On crée un element de la classe pipeline
pip=Pipeline()

#On s'interesse à une période temporelle en particulier donc on réalise un fenetrage
pip.ajoute_etape(Fenetrage('2021-02-25', '2021-03-03'))

#Sur cette période temporelle, on réalise une agrégation spatiale.
#Dans l'objectif de passer d'une echelle departementale à régionale
pip.ajoute_etape(AgregationSpatiale_reg_dep('dep',[1],'C:/Users/maroi/Projet_Code_Final/VacancesScolaires.json'))

#On applique maintenant la fonction d'agrégation qui est somme.

pip.ajoute_etape(AgregationSomme('region', 'incid_dc'))

#On lance maintenant le pipeline
resultat_final=pip.run(resultat_intermediaire)

cp = CartoPlot()
dictionnaire = {}
for i in len(resultat_final.lignes):
    region=resultat_final.lignes[i][0]
    dictionnaire[str(region)] = resultat_final.lignes[i][1]
fig = cp.plot_reg_map(data=dictionnaire, x_lim=(-6, 10), y_lim=(41, 52))
#fig.show()
fig.savefig('nombre_deces_par_region.jpg')

