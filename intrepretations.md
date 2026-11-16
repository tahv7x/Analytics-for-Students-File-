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