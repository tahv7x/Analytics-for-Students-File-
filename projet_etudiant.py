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
#plt.show()
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
print()
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

#TODO 1.1
print('Analyse Descriptive')
variables_quanti = [
    'moyenne_bac','heures_etude','note_stat'
]
stat_desc = d[variables_quanti].agg(['mean','std','min','max'])
print(stat_desc.round(2))
#TODO 1.2
print('Moyenne de note stat  par filière :\n', d.groupby('filiere')['note_stat'].mean().round(2))
variables_quali = [
    'filiere','sexe','logement',
    'assiduite','reussite'
]

for v in variables_quali: 
    print(f"Effectifs de {v} :")
    print(d[v].value_counts())

#TODO 1.3
plt.figure(figsize=(8,5))
sns.histplot(data=d,x='note_stat',bins=15,color='steelblue',edgecolor='white')
plt.title('Distribution des notes en statistiques')
plt.xlabel('Note en statistique (/20)')
plt.ylabel('Nombre d\'étudiants')
plt.tight_layout()
#plt.show()
#boite a moustaches 
plt.figure(figsize=(8,5))
sns.boxplot(data=d,x='filiere',y='note_stat',order=['Biologie','Chimie','Informatique'])
plt.title('Distribution des notes par filière')
plt.xlabel('Filière')
plt.ylabel('Note en statistique (/20)')
plt.tight_layout()
#plt.show()

#TODO 2.1
plt.figure(figsize=(8,5))
sns.scatterplot(data=d,x='heures_etude',y='note_stat')
plt.title('Relation entre heures d\'étude et note en statistique')
plt.xlabel('Heures d\'étude par semaine')
plt.ylabel('Note en statistique (/20)')
plt.tight_layout()
#plt.show()

#TODO 2.2
x = d['heures_etude']
y = d['note_stat']

r, pval = stats.pearsonr(x,y)

print('Coefficient r : ',round(r,4))
print('P valuer : ',pval)

if pval < ALPHA: #ALPHA valeur est : 0.05/5%
    print('On rejette H0 : corrélation significative')
else :
    print('On ne rejette pas H0 : corrélation non significative')

#TODO 2.3 
reg = stats.linregress(x, y)

a = reg.slope
b = reg.intercept

print("Pente a : ",round(a,4))
print("Ordonnée à l'origine b : ",round(b,4))

print(f"Equation : note_stat = {a:.4f} * heures_etude + {b:.4f}" )

plt.figure(figsize=(8,5))

sns.regplot(data=d,x='heures_etude',y='note_stat',ci=None,line_kws={"color" : "purple"})

plt.title('Droite de regression linéaire')
plt.xlabel('Heures d\'étude par semaine')
plt.ylabel('Note en statistique (/20)')
plt.tight_layout()
#plt.show()

#TODO 2.4
n =  len(d)
ddl = n - 2

R2 = reg.rvalue**2
print('R² : ',round(R2,4))
print('R² en pourcentage : ',round(r**2*100,2),'%')
t_cal = a/reg.stderr
p_cal = 2*stats.t.sf(abs(t_cal),df=ddl)

print('Statistique t : ',round(t_cal,4))
print('P valeur calculée : ',p_cal)
print('P valeur lingress : ',reg.pvalue)

t_crit = stats.t.ppf(1-ALPHA/2,df=ddl)

IC_inf = a - t_crit*reg.stderr
IC_sup = a + t_crit*reg.stderr

print('IC Intervalle de confiance a 95% : ',round(IC_inf,4),';',round(IC_sup,4))

if reg.pvalue < ALPHA : 
    print('On rejette H0 : pente significative')
else : 
    print('On ne rejette pas H0 : pente non significative')
#TODO 2.5

xbar = x.mean()
ybar = y.mean()

numerateur = ((x-xbar)*(y-ybar)).sum()
denominateur = ((x-xbar)**2).sum()

a_manuel = numerateur/denominateur
b_manuel = ybar - a_manuel*xbar

print('Moyenne X : ',round(xbar,4))
print('Moyenne Y : ',round(ybar,4))

print('Pentre calculee manuellement : ',round(a_manuel,4))
print('Ordonnee calculee manuellemnt : ',round(b_manuel,4))

print('Pente avec lingress : ',round(a,4))
print('Ordonnee avec lingress : ',round(b,4))

print('Pentres identiques :',np.isclose(a_manuel,a))
print('Ordonnees identiques : ',np.isclose(b_manuel,b))

#TODO 2.6

note_10 = a*10+b
print('Note predite pour 10h : ',round(note_10,2))
note_40 = a*40+b
print('Note predite pour 40h : ',round(note_40,2))

x_min = x.min()
x_max = x.max()

print('Heures observees : ',x_min,'a',x_max)

if x_min <= 40 <= x_max:
    print('40h : predicition dans le plage observee')
else : 
    print('40h : extrapolation,prediction non fiable')
#TODO 2.7
y_pred = a*x+b
residus = y-y_pred

print('Moyenne des residus : ',round(residus.mean(),6))
print('Ecart-types des residus : ',round(residus.std(),4))

plt.figure(figsize=(8,5))
sns.scatterplot(x = y_pred,y=residus)
plt.axhline(y=0,color='red',linestyle='--')
plt.title('Résidus en fonction des valeurs ajustées')
plt.xlabel('Notes prédites (/20)')
plt.ylabel('Résidus')
plt.tight_layout()
#plt.show()

plt.figure(figsize=(8,5))
stats.probplot(residus, dist="norm", plot=plt)
plt.title("QQ-plot des résidus")
plt.xlabel("Quantiles théoriques")
plt.ylabel("Quantiles observés")
plt.tight_layout()
#plt.show()

W,p_shapiro = stats.shapiro(residus)
print("Statistique W :", round(W, 4))
print("P-value Shapiro :", p_shapiro)

if p_shapiro < ALPHA:
    print("On rejette H0 : normalité non vérifiée")
else:
    print("On ne rejette pas H0 : normalité non rejetée")

#TODO 3.1

bio = d[d['filiere'] == 'Biologie']['note_stat']
chimie = d[d['filiere'] == 'Chimie']['note_stat']
info = d[d['filiere'] == 'Informatique']['note_stat']
#on a deja fait le boxplot dans le TODO 1.3
#TODO 3.2

for nom,groupe in [
    ('Biologie',bio),
    ('Chimie',chimie),
    ('Informatique',info)
]:
    W,p = stats.shapiro(groupe)
    print(f'{nom} : ')
    print('W = ',round(W,4))
    print('p = ',round(p,4))

    if p < ALPHA : 
        print('Normalite rejetee')
    else : 
        print('Normalite non rejetee')

stat_levene, p_levene = stats.levene(bio,chimie,info,center='median')
print('Test de Levene')
print('Statistique : ',round(stat_levene,4))
print('P value : ',round(p_levene,4))

if p_levene < ALPHA : 
    print('On rejette H0 : variances differentes')
else : 
    print('On ne rejette pas H0 : égalité des variances non rejette ')

#TODO 3.3

groupes = [bio,chimie,info]

k = len(groupes)
n = len(d)

moyenne_generale = d['note_stat'].mean()
SC_entre = sum(
    len(g) * (g.mean()-moyenne_generale)**2
    for g in groupes
)
SC_intra = sum(
    ((g-g.mean())**2).sum()
    for g in groupes
)

ddl_entre = k-1
ddl_intra = n-k

CM_entre = SC_entre / ddl_entre
CM_intra = SC_intra / ddl_intra

F_manuel = CM_entre / CM_intra 

print("Moyenne générale :", round(moyenne_generale, 4))
print("SC entre :", round(SC_entre, 4))
print("SC intra :", round(SC_intra, 4))
print("ddl entre :", ddl_entre)
print("ddl intra :", ddl_intra)
print("CM entre :", round(CM_entre, 4))
print("CM intra :", round(CM_intra, 4))
print("F manuel :", round(F_manuel, 4))

f_scipy,p_anova= stats.f_oneway(bio,chimie,info)

print('F avec F_oneway : ',round(f_scipy,4))
print(f'P value : {p_anova:.4e}')
print('Resultats identiques : ',np.isclose(F_manuel,f_scipy))

#TODO 3.4
F_critique = stats.f.ppf(1-ALPHA,ddl_entre,ddl_intra)

print('F calcule : ',round(F_manuel,4))
print('F critique : ',round(F_critique,4))
print(f'P value : {p_anova:.4e}')

if F_manuel > F_critique : 
    print('F > F critique : on rejette H0')
else : 
    print('F <= F critique : on ne rejtte pas H0 ')
if p_anova < ALPHA : 
    print('p < 0.05 : difference significative')
else : 
    print('p => 0.05 : doifference non significative')

#TODO 3.5

SC_totale = SC_entre + SC_intra
eta2 = SC_entre / SC_totale

print('SC totale : ',round(SC_totale,4))
print('Eta² : ',round(eta2,4))
print('Eta² en pourcentage : ',round(eta2*100,2),"%")

#TODO 3.6

tukey = stats.tukey_hsd(bio,chimie,info)
noms = ['Biologie','Chimie','Informatique']

IC_tukey = tukey.confidence_interval(confidence_level = 1 - ALPHA)
for i in range(3):
    for j in range(i+1,3):
        difference = tukey.statistic[i,j]
        p = tukey.pvalue[i,j]
        print(f"{noms[i]} vs {noms[j]}")
        print("Différence de moyennes :", round(difference, 4))
        print("P-value :", f"{p:.4e}")     

        print('IC a 95% : ',round(IC_tukey.low[i,j],4),
              ";",
              round(IC_tukey.high[i,j],4)
        )
        if p < ALPHA : 
            print('Différence significative : rejet de H0')
        else : 
            print('Différence non significative : H0 non rejetée')

# TODO 3.7

H,p_kruskal = stats.kruskal(bio,chimie,info)

print('Statistique H : ',round(H,4))
print(f'P value : {p_kruskal:.4e}')
if p_kruskal < ALPHA:
    print("On rejette H0 : différence significative")
else:
    print("On ne rejette pas H0 : différence non significative")
if (p_kruskal < ALPHA) == (p_anova < ALPHA):
    print("Conclusion identique à l'ANOVA au seuil de 5 %")
else:
    print("Conclusion différente de l'ANOVA au seuil de 5 %")