# %% [markdown]
# # PROJET : Analyse de données · régression linéaire, ANOVA, khi-2
# Nom, prénom : ......................   Groupe : ............
# Bibliothèques : pandas, numpy, scipy, matplotlib, seaborn (statsmodels autorisé en option).
# Complétez les zones "# TODO". Commentez vos choix et interprétez TOUS vos résultats par écrit.
# %%
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from scipy import stats
sns.set_theme(style="whitegrid")
ALPHA = 0.05

# %% PARTIE 0 : chargement et nettoyage (2 pts)
df = pd.read_csv("donnees_projet.csv")
# TODO 0.1 : dimensions, types, valeurs manquantes par variable
# TODO 0.2 : repérer une valeur aberrante dans heures_etude (describe, boxplot). Que faites-vous ? Justifiez.
# TODO 0.3 : construire le tableau d'analyse "d" sans valeurs manquantes sur les variables utilisées

# %% PARTIE 1 : analyse descriptive (2 pts)
# TODO 1.1 : moyenne, écart-type, min, max de moyenne_bac, heures_etude, note_stat
# TODO 1.2 : moyenne de note_stat par filière ; effectifs de chaque modalité qualitative
# TODO 1.3 : 2 graphiques commentés (histogramme et boxplot par exemple)

# %% PARTIE 2 : régression linéaire simple, note_stat ~ heures_etude (6 pts)
# TODO 2.1 : nuage de points. La relation semble-t-elle linéaire ?
# TODO 2.2 : coefficient de corrélation r et son test
# TODO 2.3 : estimer la droite (stats.linregress) ; écrire l'équation ; interpréter pente et ordonnée
# TODO 2.4 : R², p-value de la pente, intervalle de confiance de la pente
# TODO 2.5 : retrouver pente et ordonnée "à la main" (formules du cours) et comparer
# TODO 2.6 : prédire la note pour 10 h d'étude par semaine ; peut-on prédire pour 40 h ? pourquoi ?
# TODO 2.7 : résidus : graphique résidus vs ajustées, QQ-plot, test de Shapiro ; conditions respectées ?
# BONUS 2.8 : régression multiple (heures_etude + moyenne_bac) avec scikit-learn ou statsmodels ; comparer les R²

# %% PARTIE 3 : ANOVA à un facteur, note_stat ~ filiere (5 pts)
# TODO 3.1 : H0 et H1 ; boxplot de la note par filière
# TODO 3.2 : vérifier les conditions : normalité par groupe (Shapiro), égalité des variances (Levene)
# TODO 3.3 : calculer SC_entre, SC_intra, CM, F, ddl à la main puis comparer avec stats.f_oneway
# TODO 3.4 : F critique (stats.f.ppf) ; décision par comparaison F / F critique ET par la p-value
# TODO 3.5 : taille d'effet η² ; interprétation
# TODO 3.6 : comparaisons par paires (stats.tukey_hsd) : quelles filières diffèrent ?
# BONUS 3.7 : test non paramétrique (stats.kruskal) ; conclusion identique ?

# %% PARTIE 4 : khi-2 d'indépendance (5 pts)
# Deux couples à tester : (logement, assiduite) et (sexe, filiere)
# Pour CHAQUE couple :
# TODO 4.1 : H0, H1 ; tableau croisé observé (pd.crosstab)
# TODO 4.2 : tableau des effectifs théoriques calculés avec la formule du cours (ligne x colonne / total)
# TODO 4.3 : contribution de chaque cellule (O-E)²/E, puis le χ² total
# TODO 4.4 : ddl, χ² critique, p-value ; comparer avec stats.chi2_contingency
# TODO 4.5 : vérifier la condition E >= 5 ; décision ; conclusion en une phrase
# TODO 4.6 : V de Cramér ; graphique en barres empilées en pourcentages
# Question de réflexion : pourquoi un khi-2 significatif ne prouve-t-il pas une relation de cause à effet ?

# %% PARTIE 5 : synthèse (clarté, 0 pt ici, évalué dans le rapport)
# Rédigez dans le rapport une conclusion de 10 lignes reliant les trois méthodes.
