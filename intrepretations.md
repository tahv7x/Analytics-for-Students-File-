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