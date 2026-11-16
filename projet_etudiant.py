import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from pathlib import Path

sns.set_theme(style="whitegrid")
ALPHA = 0.05
df = pd.read_csv(Path(__file__).parent/"files"/"donnees_projet.csv")

#TODO 0.1

print("Dimensions : ",df.shape)
print("Type : \n", df.dtypes)
print("Valeurs manquantes : \n", df.isnull().sum())#en veut voir toutes les cases vides et en veut compter la somme de toutes les cases vides pour chaque variable

#TODO 0.2
print(df['heures_etude'].describe())
plt.figure(figsize=(8,4))
sns.boxplot(x=df['heures_etude'])
plt.title('Distribution des heures d\'étude')
plt.xlabel('Heures d\'étude par semaine')
plt.show()

#Calcule Avec la methode tukey
Q1 = df["heures_etude"].quantile(0.25)
Q3 = df["heures_etude"].quantile(0.75)
IQR = Q3 - Q1

b_inf = Q1 - 1.5*IQR
b_sup = Q3 + 1.5*IQR
print('Bornes inférieures :', b_inf)
print('Bornes supérieures :', b_sup)

aberrantes = df[
    (df['heures_etude'] < b_inf) | 
    (df['heures_etude'] > b_sup)
]

print('Nombre d\'aberrations :', len(aberrantes))
print(aberrantes[['id','heures_etude']])

#don kefma shefna hna on va change 95 par un valeur manquante aussi 
df.loc[df['heures_etude'] == 95, 'heures_etude'] = np.nan

print('Valeurs manquantes après traitement :', df['heures_etude'].isnull().sum())

#TODO 0.3
print('Lignes avec valeurs manquantes : ', df.isnull().any(axis=1).sum())
print(df[df.isnull().any(axis=1)][
    ['id','heures_etude','heures_sommeil']
])  

variables = ['filiere','sexe','logement',
             'assiduite','moyenne_bac',
             'heures_etude','note_stat']
d = df.dropna(subset=variables).copy()

print('Dimension de tableau d\'analyse d : ', d.shape)
print('Valeurs manquantes dans les variables utilisées :\n', d[variables].isnull().sum())
print('Nombre d\'observations supprimées :', len(df)-len(d))

