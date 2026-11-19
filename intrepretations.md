# Partie 0 — Chargement et nettoyage des données

## TODO 0.1 — Exploration initiale

Le jeu de données contient **300 observations et 10 variables**.

Les variables quantitatives sont : `moyenne_bac`, `heures_etude`, `heures_sommeil` et `note_stat`. Les autres variables sont qualitatives, à l'exception de `id`, qui représente un identifiant.

L'analyse des valeurs manquantes montre que **6 valeurs sont absentes pour `heures_etude` et 4 pour `heures_sommeil`**. Les autres variables ne présentent aucune valeur manquante.

Il est donc nécessaire de traiter ces valeurs manquantes avant de poursuivre les analyses statistiques.

### TODO 0.2 — Détection et traitement des valeurs aberrantes

L'analyse de la variable `heures_etude` révèle 6 valeurs atypiques selon la méthode de Tukey, avec une borne supérieure de 17,925 heures.

Parmi ces valeurs, 95 heures par semaine représente une observation extrêmement élevée par rapport au reste des données. Nous avons donc choisi de la considérer comme manquante pour l'analyse principale, afin de limiter son influence sur les résultats statistiques.

Les cinq autres valeurs atypiques, comprises entre 18,2 et 24,9 heures, ont été conservées car elles restent plausibles pour des heures d'étude hebdomadaires.

### TODO 0.3 — Construction du tableau d'analyse

Après le traitement de la valeur extrême de 95 heures, nous avons identifié 11 observations contenant au moins une valeur manquante : 7 pour les heures d'étude et 4 pour les heures de sommeil.

Nous avons supprimé les 7 observations incomplètes sur les variables nécessaires aux analyses statistiques. Les valeurs manquantes des heures de sommeil ont été conservées, car cette variable n'intervient pas dans les trois méthodes étudiées.

Le tableau d'analyse final contient ainsi **293 étudiants**, avec des données complètes sur toutes les variables utilisées.

## Partie 1 — Analyse descriptive

### TODO 1.1 — Statistiques descriptives

L'analyse descriptive porte sur 293 étudiants après le nettoyage des données.

La moyenne au baccalauréat est de **12,89/20**, avec un écart-type de 1,31, ce qui indique des résultats relativement regroupés autour de la moyenne.

Les étudiants consacrent en moyenne **8,95 heures par semaine** à leurs études, avec un écart-type de 3,55 heures. Le temps d'étude varie donc d'un étudiant à l'autre.

Enfin, la note moyenne en statistique est de **11,08/20**, avec un écart-type de 2,86. Les notes varient entre 2,99 et 20, ce qui montre des différences de performance entre les étudiants.

Ces résultats permettent de décrire les données, mais ne suffisent pas à déterminer quels facteurs sont associés aux notes en statistique.

### TODO 1.2 — Analyse par filière et répartition des étudiants

L'analyse des notes moyennes par filière montre que les étudiants en Informatique obtiennent la moyenne la plus élevée (12,75/20), suivis de ceux en Biologie (10,95/20) et en Chimie (9,90/20). Ces différences seront étudiées à l'aide de l'ANOVA afin de vérifier leur significativité statistique.

Concernant la répartition des 293 étudiants, on compte 159 femmes et 134 hommes. La location est le mode de logement le plus fréquent (115 étudiants), tandis que l'assiduité moyenne représente la catégorie la plus nombreuse (116 étudiants).

Enfin, 187 étudiants sont admis contre 106 ajournés, soit un taux de réussite d'environ 63,8 %.

### TODO 1.3 — Histogramme des notes en statistique

L'histogramme montre que les notes en statistique sont principalement concentrées entre 8 et 14/20, avec un maximum de fréquence autour de 11 à 12/20.

La distribution présente une forme approximativement en cloche, avec peu de notes très faibles ou très élevées. Cette répartition est cohérente avec la moyenne de 11,08/20 observée précédemment.

## Partie 2 - Régression linéaire

### TODO 2.1 — Nuage de points

Le nuage de points montre une tendance croissante entre les heures d'étude hebdomadaires et la note en statistique. Les étudiants qui consacrent davantage de temps à l'étude ont généralement tendance à obtenir de meilleures notes.

La relation semble approximativement linéaire, malgré une certaine dispersion des points. Une régression linéaire simple paraît donc envisageable, sous réserve de vérifier les conditions du modèle.

### TODO 2.2 — Corrélation linéaire

Le coefficient de corrélation de Pearson est de **r = 0,6773**, ce qui indique une corrélation linéaire positive assez forte entre les heures d'étude et la note en statistique.

La p-value obtenue (environ \(1,11 \times 10^{-40}\)) est inférieure au seuil de signification de 5 %.

Nous rejetons donc l'hypothèse nulle \(H_0\). La corrélation observée est statistiquement significative : les étudiants qui étudient davantage ont généralement tendance à obtenir de meilleures notes, sans que cela démontre une relation de cause à effet.

### TODO 2.3 — Droite de régression linéaire

La droite de régression estimée est :

**Note_stat = 0,5442 × heures_etude + 6,2049**

La pente positive de 0,5442 indique qu'une heure d'étude hebdomadaire supplémentaire est associée à une augmentation moyenne prédite de 0,5442 point de la note en statistique.

L'ordonnée à l'origine, égale à 6,2049, représente la note prédite pour zéro heure d'étude. Cette valeur doit être interprétée avec prudence, car elle se situe en dehors des heures d'étude observées.

### TODO 2.4 — Qualité du modèle et significativité de la pente

Le coefficient de détermination est de **R² = 0,4588**, ce qui signifie que le modèle linéaire basé sur les heures d'étude explique environ 45,88 % de la variabilité des notes en statistique.

Le test de significativité de la pente donne une statistique t = 15,7056 et une p-value d'environ 1,11 × 10⁻⁴⁰, inférieure au seuil de 5 %. Nous rejetons donc l'hypothèse nulle H₀ : a = 0.

L'intervalle de confiance à 95 % de la pente est [0,4760 ; 0,6124]. Il ne contient pas zéro, ce qui confirme que la pente est statistiquement significative et positive.

Ces résultats indiquent une association linéaire positive entre le temps d'étude et les notes, sans démontrer une relation de causalité.

### TODO 2.5 — Vérification manuelle des coefficients

Les calculs effectués à partir des formules du cours donnent une pente de 0,5442 et une ordonnée à l'origine de 6,2049.

Ces résultats sont identiques, à la précision numérique près, à ceux obtenus avec la fonction `stats.linregress()`. Cette comparaison confirme la cohérence de l'estimation de notre droite de régression.

### TODO 2.6 — Prédictions

Pour un étudiant consacrant 10 heures par semaine à ses études, la régression linéaire prédit une note d'environ **11,65/20**.

En revanche, pour 40 heures d'étude, le modèle prédit environ 27,97/20. Cette valeur n'est pas réaliste, car la note maximale est de 20/20 et 40 heures se situe en dehors de l'intervalle observé [2,5 ; 24,9].

Il s'agit donc d'une extrapolation, dont le résultat ne peut pas être considéré comme fiable.