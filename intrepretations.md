Partie 0 — Chargement et nettoyage des données
TODO 0.1 — Exploration initiale
Le jeu de données contient 300 observations et 10 variables.

Les variables quantitatives sont : moyenne_bac, heures_etude, heures_sommeil et note_stat. Les autres variables sont qualitatives, à l'exception de id, qui représente un identifiant.

L'analyse des valeurs manquantes montre que 6 valeurs sont absentes pour heures_etude et 4 pour heures_sommeil. Les autres variables ne présentent aucune valeur manquante.

Il est donc nécessaire de traiter ces valeurs manquantes avant de poursuivre les analyses statistiques.
TODO 0.2 — Détection et traitement des valeurs aberrantes
L'analyse de la variable heures_etude révèle 6 valeurs atypiques selon la méthode de Tukey, avec une borne supérieure de 17,925 heures.

Parmi ces valeurs, 95 heures par semaine représente une observation extrêmement élevée par rapport au reste des données. Nous avons donc choisi de la remplacer par une valeur manquante pour l'analyse principale, afin de limiter son influence sur les résultats statistiques.

Les cinq autres valeurs atypiques, comprises entre 18,2 et 24,9 heures, ont été conservées car elles restent plausibles pour des heures d'étude hebdomadaires.
TODO 0.3 — Construction du tableau d'analyse
Après le traitement de la valeur extrême de 95 heures, nous avons identifié 11 observations contenant au moins une valeur manquante : 7 pour les heures d'étude et 4 pour les heures de sommeil.

Nous avons supprimé les 7 observations incomplètes sur les variables nécessaires aux analyses statistiques. Les valeurs manquantes des heures de sommeil ont été conservées, car cette variable n'intervient pas dans les trois méthodes étudiées.

Le tableau d'analyse final contient ainsi 293 étudiants, avec des données complètes sur toutes les variables utilisées.
Partie 1 — Analyse descriptive
TODO 1.1 — Statistiques descriptives
L'analyse descriptive porte sur 293 étudiants après le nettoyage des données.

La moyenne au baccalauréat est de 12,89/20, avec un écart-type de 1,31, ce qui indique des résultats relativement regroupés autour de la moyenne.

Les étudiants consacrent en moyenne 8,95 heures par semaine à leurs études, avec un écart-type de 3,55 heures. Le temps d'étude varie donc d'un étudiant à l'autre.

Enfin, la note moyenne en statistique est de 11,08/20, avec un écart-type de 2,86. Les notes varient entre 2,99 et 20, ce qui montre des différences de performance entre les étudiants.

Ces résultats permettent de décrire les données, mais ne suffisent pas à déterminer quels facteurs sont associés aux notes en statistique.
TODO 1.2 — Analyse par filière et répartition des étudiants
L'analyse des notes moyennes par filière montre que les étudiants en Informatique obtiennent la moyenne la plus élevée (12,75/20), suivis de ceux en Biologie (10,95/20) et en Chimie (9,90/20). Ces différences seront étudiées à l'aide de l'ANOVA afin de vérifier leur significativité statistique.

Concernant la répartition des 293 étudiants, on compte 159 femmes et 134 hommes. La location est le mode de logement le plus fréquent (115 étudiants), tandis que l'assiduité moyenne représente la catégorie la plus nombreuse (116 étudiants).

Enfin, 187 étudiants sont admis contre 106 ajournés, soit un taux de réussite d’environ 63,8 %.
TODO 1.3 — Histogramme des notes en statistique
L'histogramme montre que les notes en statistique sont principalement concentrées entre 8 et 14/20, avec un maximum de fréquence autour de 11 à 12/20.

La distribution présente une forme approximativement en cloche, avec peu de notes très faibles ou très élevées. Cette répartition est cohérente avec la moyenne de 11,08/20 observée précédemment.
Partie 2 — Régression linéaire
TODO 2.1 — Nuage de points
Le nuage de points montre une tendance croissante entre les heures d'étude hebdomadaires et la note en statistique. Les étudiants qui consacrent davantage de temps à l'étude ont généralement tendance à obtenir de meilleures notes.

La relation semble approximativement linéaire, malgré une certaine dispersion des points. Une régression linéaire simple paraît donc envisageable, sous réserve de vérifier les conditions du modèle.
TODO 2.2 — Corrélation linéaire
Le coefficient de corrélation de Pearson est de r = 0,6773, ce qui indique une corrélation linéaire positive assez forte entre les heures d'étude et la note en statistique.

La p-value obtenue (environ \(1,11 \times 10^{-40}\)) est inférieure au seuil de signification de 5 %.

Nous rejetons donc l'hypothèse nulle \(H_0\). La corrélation observée est statistiquement significative : les étudiants qui étudient davantage ont généralement tendance à obtenir de meilleures notes, sans que cela démontre une relation de cause à effet.
TODO 2.3 — Droite de régression linéaire
La droite de régression estimée est :

Note_stat = 0,5442 × heures_etude + 6,2049

La pente positive de 0,5442 indique qu'une heure d'étude hebdomadaire supplémentaire est associée à une augmentation moyenne prédite de 0,5442 point de la note en statistique.

L'ordonnée à l'origine, égale à 6,2049, représente la note prédite pour zéro heure d'étude. Cette valeur doit être interprétée avec prudence, car elle se situe en dehors des heures d'étude observées.
TODO 2.4 — Qualité du modèle et significativité de la pente
Le coefficient de détermination est de R² = 0,4588, ce qui signifie que le modèle linéaire basé sur les heures d'étude explique environ 45,88 % de la variabilité des notes en statistique.

Le test de significativité de la pente donne une statistique t = 15,7056 et une p-value d'environ 1,11 × 10⁻⁴⁰, inférieure au seuil de 5 %. Nous rejetons donc l'hypothèse nulle H₀ : a = 0.

L'intervalle de confiance à 95 % de la pente est [0,4760 ; 0,6124]. Il ne contient pas zéro, ce qui confirme que la pente est statistiquement significative et positive.

Ces résultats indiquent une association linéaire positive entre le temps d'étude et les notes, sans démontrer une relation de causalité.
TODO 2.5 — Vérification manuelle des coefficients
Les calculs effectués à partir des formules du cours donnent une pente de 0,5442 et une ordonnée à l'origine de 6,2049.

Ces résultats sont identiques, à la précision numérique près, à ceux obtenus avec la fonction stats.linregress(). Cette comparaison confirme la cohérence de l'estimation de notre droite de régression.
TODO 2.6 — Prédictions
Pour un étudiant consacrant 10 heures par semaine à ses études, la régression linéaire prédit une note d'environ 11,65/20.

En revanche, pour 40 heures d'étude, le modèle prédit environ 27,97/20. Cette valeur n'est pas réaliste, car la note maximale est de 20/20 et 40 heures se situe en dehors de l'intervalle observé [2,5 ; 24,9].

Il s'agit donc d'une extrapolation, dont le résultat ne peut pas être considéré comme fiable.
TODO 2.7 — Analyse des résidus et vérification de la normalité
Le graphique des résidus montre une dispersion globalement autour de zéro, sans structure systématique évidente. Le QQ-plot indique que les résidus suivent approximativement une distribution normale.

Le test de Shapiro-Wilk donne une statistique W = 0,9952 et une p-value de 0,4899, supérieure au seuil de 5 %.

Nous ne rejetons donc pas l'hypothèse nulle de normalité des résidus. Ces résultats sont compatibles avec l'hypothèse de normalité, sans démontrer l'indépendance ni l'homogénéité des variances des erreurs.
BONUS 2.8 — Régression linéaire multiple
La régression multiple a été réalisée en utilisant les heures d'étude et la moyenne au baccalauréat comme variables explicatives de la note en statistique.

Le modèle obtenu est :

Note_stat = −0,1852 + 0,5459 × heures_etude + 0,4945 × moyenne_bac

Les deux coefficients estimés sont positifs, ce qui indique une association positive de chaque variable avec la note, lorsque l'autre variable est maintenue constante.

Le coefficient de détermination passe de 45,88 % pour la régression simple à 51,05 % pour la régression multiple, soit un gain de 5,17 points de pourcentage.

L'ajout de la moyenne au baccalauréat améliore donc l'ajustement du modèle sur notre échantillon. Cependant, cette amélioration ne suffit pas à démontrer une relation de causalité ni une meilleure performance prédictive sur de nouvelles données.
Partie 3 — ANOVA à un facteur
TODO 3.1 — Comparaison graphique des notes par filière
Le diagramme en boîtes montre des différences dans la distribution des notes en statistique selon la filière.

Les étudiants en Informatique présentent globalement des notes plus élevées, suivis des étudiants en Biologie, puis de ceux en Chimie.

Cependant, cette observation graphique ne suffit pas à confirmer que les différences sont statistiquement significatives. Une ANOVA sera donc réalisée afin de comparer les moyennes des trois filières.
TODO 3.2 — Vérification des conditions de l'ANOVA
Les tests de Shapiro-Wilk donnent des p-values de 0,8997 pour la Biologie, 0,1175 pour la Chimie et 0,4666 pour l'Informatique. Toutes ces valeurs sont supérieures au seuil de 5 %. L'hypothèse de normalité n'est donc rejetée dans aucun des trois groupes.

Le test de Levene donne une statistique de 0,4372 et une p-value de 0,6463. Nous ne rejetons pas l'hypothèse d'égalité des variances.

En supposant l'indépendance des observations, les conditions vérifiées ne révèlent pas d'obstacle majeur à l'application de l'ANOVA classique.
TODO 3.3 — Calcul manuel de l'ANOVA
L'analyse de la variance donne une somme des carrés entre les groupes de 402,7140 et une somme des carrés intra-groupes de 1 978,2839.

Les carrés moyens correspondants sont respectivement de 201,3570 et 6,8217, ce qui donne une statistique F de 29,5173.

Le calcul manuel et la fonction stats.f_oneway() donnent le même résultat, ce qui confirme la cohérence des calculs.

Cette statistique suggère des différences entre les moyennes des filières, dont la significativité est évaluée au seuil de 5 %.
TODO 3.4 — Décision statistique
La statistique F calculée (29,5173) est supérieure à la valeur critique (3,0269). De plus, la p-value est inférieure au seuil de 5 %.

Nous rejetons donc l'hypothèse nulle d'égalité des moyennes. Au moins une moyenne de filière diffère significativement des autres.
TODO 3.5 — Taille d'effet
La taille d'effet η² est d'environ 0,1691, soit 16,91 %. Cela signifie que les différences entre les filières représentent environ 16,91 % de la variabilité totale des notes dans l'échantillon.

Ce résultat mesure l'importance de l'association, sans établir une relation de causalité.
TODO 3.6 — Comparaisons par paires (Tukey)
Le test de Tukey révèle des différences statistiquement significatives entre les trois filières prises deux à deux.

Les étudiants en Biologie obtiennent une moyenne supérieure à ceux en Chimie de 1,0541 point (p = 0,0119).

Les étudiants en Informatique présentent une moyenne supérieure à ceux en Biologie de 1,7956 point (p < 0,001) et à ceux en Chimie de 2,8496 points (p < 0,001).

Ainsi, les étudiants en Informatique obtiennent les meilleures notes moyennes, suivis de ceux en Biologie, puis en Chimie. Ces différences sont statistiquement significatives, mais ne démontrent pas que la filière est directement responsable des résultats.
BONUS 3.7 — Test de Kruskal-Wallis
Le test non paramétrique de Kruskal-Wallis donne une statistique H = 53,9048 et une p-value de 1,9712 × 10⁻¹², inférieure au seuil de 5 %.

Nous rejetons donc l'hypothèse nulle d'égalité des distributions des trois filières. Le test met en évidence une différence statistiquement significative entre au moins deux groupes.

Cette décision est cohérente avec celle obtenue par l'ANOVA, ce qui renforce notre constat de différences entre les filières, bien que les deux tests ne portent pas exactement sur la même hypothèse.
Partie 4 — Tests du Khi-2 d’indépendance
Étude 1 — Logement × Assiduité
TODO 4.1 et 4.2 — Effectifs observés et théoriques
Le tableau de contingence présente la répartition des 293 étudiants selon leur logement et leur assiduité.

On observe que les étudiants résidant en cité universitaire présentent fréquemment une assiduité forte (52 étudiants sur 79), tandis que l'assiduité moyenne est la plus représentée chez les étudiants vivant en famille ou en location.

La comparaison entre les effectifs observés et théoriques montre plusieurs écarts, notamment pour les étudiants résidant en cité universitaire. Le test du Khi-2 permettra de déterminer si ces écarts sont statistiquement significatifs.
TODO 4.3 — Calcul manuel du Khi-2
Le calcul des contributions de chaque cellule donne une statistique du Khi-2 égale à 40,2762.

Les contributions les plus importantes concernent notamment les étudiants résidant en cité universitaire avec une assiduité forte (16,2775) et ceux vivant en location avec une assiduité forte (7,0830).

Ces écarts contribuent fortement à la statistique globale. Il reste à vérifier leur significativité à l'aide de la valeur critique et de la p-value.
TODO 4.4 et 4.5 — Test du Khi-2 et décision
Le test du Khi-2 donne une statistique de 40,2762, supérieure à la valeur critique de 9,4877, avec 4 degrés de liberté.

La p-value obtenue (3,7950 × 10⁻⁸) est inférieure au seuil de 5 %. Nous rejetons donc l'hypothèse nulle d'indépendance.

Par ailleurs, tous les effectifs théoriques sont supérieurs à 5, avec un minimum de 17,7952, ce qui respecte la condition demandée pour l'application du test.

Nous concluons qu'il existe une association statistiquement significative entre le type de logement et le niveau d'assiduité, sans pouvoir établir une relation de causalité.
TODO 4.6 — V de Cramér et graphique
Le V de Cramér est d'environ 0,2622, indiquant une association d'intensité limitée à modérée entre le logement et l'assiduité.

Le graphique montre que 65,82 % des étudiants résidant en cité universitaire présentent une assiduité forte, contre 33,33 % pour ceux vivant en famille et 22,61 % pour ceux en location.

Ces différences illustrent l'association significative détectée par le test du Khi-2, sans établir de relation de cause à effet.
Étude 2 — Sexe × Filière
TODO 4.1 à 4.5 — Test du Khi-2 et décision
Le test du Khi-2 donne une statistique de 2,5489 avec 2 degrés de liberté. Cette valeur est inférieure à la valeur critique de 5,9915.

La p-value obtenue est de 0,2796, supérieure au seuil de 5 %. Nous ne rejetons donc pas l'hypothèse nulle d'indépendance.

Tous les effectifs théoriques sont supérieurs à 5, avec un minimum de 39,7884.

Le V de Cramér est égal à 0,0933, indiquant une association très faible. Les résultats ne montrent donc pas d'association statistiquement significative entre le sexe et la filière.
TODO 4.6 — Interprétation du graphique
Le graphique en barres empilées présente la répartition des filières selon le sexe.

Chez les femmes, la Chimie représente 40,88 % des étudiantes, suivie de la Biologie (33,33 %) et de l'Informatique (25,79 %).

Chez les hommes, la Chimie représente 36,57 %, l'Informatique 34,33 % et la Biologie 29,10 %.

Malgré ces différences descriptives, le test du Khi-2 donne une p-value de 0,2796, supérieure au seuil de 5 %. Les résultats ne permettent donc pas de conclure à une association statistiquement significative entre le sexe et la filière.
Partie 5 — Synthèse générale
L'objectif de ce projet était d'étudier les facteurs associés à la note en statistique des étudiants.

Après nettoyage des données, 293 observations ont été retenues pour l'analyse.

La corrélation de Pearson révèle une relation positive et significative entre les heures d'étude et la note (r = 0,6773).

La régression linéaire simple explique 45,88 % de la variabilité des notes.

L'ajout de la moyenne au baccalauréat porte ce pourcentage à 51,05 % dans le modèle multiple.

L'ANOVA montre des différences significatives entre les moyennes des trois filières (p < 0,05).

Le test de Tukey confirme que les étudiants en Informatique obtiennent, en moyenne, les notes les plus élevées.

Le test du Khi-2 révèle une association significative entre le logement et l'assiduité.

En revanche, aucune association statistiquement significative n'est mise en évidence entre le sexe et la filière.

Ces résultats permettent d'identifier plusieurs relations statistiques, sans démontrer nécessairement des liens de causalité.