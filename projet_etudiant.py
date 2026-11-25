import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from pathlib import Path



sns.set_theme(style="whitegrid")
ALPHA = 0.05
#Dossier pour sauvgarder notre graphes
FIG_DIR = Path(__file__).parent/"Figures"
FIG_DIR.mkdir(exist_ok=True)
#Fonction pour enregistre graphes
def sauvegarder_graph(nom):
    plt.tight_layout()
    plt.savefig(
        FIG_DIR / nom,
        dpi = 300,
        bbox_inches = 'tight'
    )
    plt.close()
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
sauvegarder_graph("01_boxplot_heures.png")
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

#donc kefma shefna hna on va change 95 par un valeur manquante aussi 
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
sauvegarder_graph("02_histogramme_notes.png")
#boite a moustaches 
plt.figure(figsize=(8,5))
sns.boxplot(data=d,x='filiere',y='note_stat',order=['Biologie','Chimie','Informatique'])
plt.title('Distribution des notes par filière')
plt.xlabel('Filière')
plt.ylabel('Note en statistique (/20)')
plt.tight_layout()
#plt.show()
sauvegarder_graph("03_boxplot_filieres.png")

#TODO 2.1
plt.figure(figsize=(8,5))
sns.scatterplot(data=d,x='heures_etude',y='note_stat')
plt.title('Relation entre heures d\'étude et note en statistique')
plt.xlabel('Heures d\'étude par semaine')
plt.ylabel('Note en statistique (/20)')
plt.tight_layout()
#plt.show()
sauvegarder_graph("04_nuage_points.png")

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
sauvegarder_graph("05_regression.png")

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
sauvegarder_graph("06_residus.png")

plt.figure(figsize=(8,5))
stats.probplot(residus, dist="norm", plot=plt)
plt.title("QQ-plot des résidus")
plt.xlabel("Quantiles théoriques")
plt.ylabel("Quantiles observés")
plt.tight_layout()
#plt.show()
sauvegarder_graph("07_qqplot.png")

W,p_shapiro = stats.shapiro(residus)
print("Statistique W :", round(W, 4))
print("P-value Shapiro :", p_shapiro)

if p_shapiro < ALPHA:
    print("On rejette H0 : normalité non vérifiée")
else:
    print("On ne rejette pas H0 : normalité non rejetée")

#BONUS 2.8

x_multiple = d[['heures_etude','moyenne_bac']]
y_multiple = d['note_stat']
modele_multiple = LinearRegression()
modele_multiple.fit(x_multiple,y_multiple)
b0 = modele_multiple.intercept_
b1 = modele_multiple.coef_[0]
b2 = modele_multiple.coef_[1]
print('Constante B0 : ',round(b0,4))
print('Coefficient heures_etude : ',round(b1,4))
print('Coefficient moyenne_bac : ',round(b2,4))

print(f'Equation : note_stat = {b0:.4f}'
      f' + {b1:.4f} * heures_etude'
      f' + {b2:.4f} * moyenne_bac'
)

R2_multiple = modele_multiple.score(x_multiple,y_multiple)
print('R² regression simple : ',round(R2,4))
print('R² regression multiple :',round(R2_multiple,4))

print('Gain de R² : ',round(R2_multiple - R2,4))
#TODO 3.1

# H0 : Les moyennes des trois filieres sont egales
# H1 : Au moins une moyenne est differente
# Seuil de signification : alpha = 0.05e
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


#ETUDE 1 : LOGEMENT x ASSIDUITE
# #TODO 4.1

# H0 : logement et assiduite sont independants
# H1 : logement et assiduite sont associes
observe = pd.crosstab(d['logement'],d['assiduite'])
print('Effectifs observees : ',observe)

#TODO 4.2

total_lignes = observe.sum(axis=1)
total_colonnees = observe.sum(axis=0)
n_total = observe.to_numpy().sum()

effectifs_theo = np.outer(
    total_lignes,
    total_colonnees
)/n_total

theorique = pd.DataFrame(
    effectifs_theo,
    index=observe.index,
    columns=observe.columns
)

print('Effectifs théoriques : ',theorique.round(2))

#TODO 4.3

contributions = (observe - theorique)**2/theorique
print('Contributions de chaque cellule : ')
print(contributions.round(4))

khi2_manuel = contributions.to_numpy().sum()
print('khi-2 calcule manuellement : ',round(khi2_manuel,4))

#TODO 4.4
L,C = observe.shape
ddl_khi2 = (L-1)*(C-1)

khi2_critique = stats.chi2.ppf(
    1-ALPHA,df=ddl_khi2
)
p_manuel = stats.chi2.sf(
    khi2_manuel,df=ddl_khi2
)
print('Degres de liberte : ',ddl_khi2)
print('khi-2 critique : ',round(khi2_critique,4))
print(f'P-value manuelle : {p_manuel:.4e}')

khi2_scipy,p_scipy,ddl_scipy,E_scipy = (
    stats.chi2_contingency(observe)
)
print('khi-2 avec scipy : ',round(khi2_scipy,4))
print(f'P-value scipy : {p_scipy:.4e}')
print('ddl scipy : ',ddl_scipy)

print('Résultats identiques : ',np.isclose(khi2_manuel,khi2_scipy))

#TODO 4.5

print('Effectif théorique minimum : ',round(theorique.to_numpy().min(),4))
condition = (theorique.to_numpy() >= 5).all()
print('tous les effectifs théoriques >= 5 : ',condition)
if condition : 
    if khi2_manuel > khi2_critique : 
        print('khi2 > khi_2 critique : rejet H0')
    else :
        print('khi2 < khi2_critique : on ne rejet pas H0') 
    if p_scipy < ALPHA :
        print('Association statistiquement significative')
    else:
        print('Association non significative')
else : 
    print('Condition E<=5 non respectee')

#TODO 4.6

V_cramer = np.sqrt(khi2_manuel/(n_total*min(L-1,C-1)))
print('V de cramer : ',round(V_cramer,4))
# Graphique en barres empilées en pourcentages
pourcentages = observe.div(
    observe.sum(axis=1),axis=0
)*100

print('Pourcentages par longement : ')
print(pourcentages.round(2))

pourcentages.plot(
    kind='bar',
    stacked = True,
    figsize=(9,5)
)
plt.title("Répartition de l'assiduité selon le logement")
plt.xlabel('Type de logement')
plt.ylabel('Pourcentage des etudaints (%)')
plt.legend(title='Assiduite')
plt.xticks(rotation=0)
plt.ylim(0,100)
plt.tight_layout()
#plt.show()
sauvegarder_graph("08_khi2_logement.png")

# ETUDE 2 : SEXE × FILIERE
#TODO 4.1
# H0 : Le sexe et la filiere sont independants
# H1 : Le sexe et la filiere sont associes
# Seuil de signification : alpha = 0.05

observe2 = pd.crosstab(d['sexe'],d['filiere'])
print('Effectifs observes : ')
print(observe2)

#TODO 4.2
total_lignes2 = observe2.sum(axis=1)
total_colonnes2 = observe2.sum(axis=0)
n_total2 = observe2.to_numpy().sum()
effectifs_theoriques2 = np.outer(
    total_lignes2,
    total_colonnes2
)/n_total2
theorique2 = pd.DataFrame(
    effectifs_theoriques2,
    index=observe2.index,
    columns=observe2.columns
)
print('Effectifs theoriques : ',theorique2.round(4))

#TODO 4.3

contributions2 = (observe2 - theorique2)**2/theorique2
print('Contributions de chaque cellule : ',contributions2.round(4))
khi2_manuel2 = contributions2.to_numpy().sum()
print('Khi2 cellule manuellement : ',round(khi2_manuel2,4))

#TODO 4.4

L2,C2 = observe2.shape
ddl_khi2_2 = (L2 - 1) * (C2 - 1)
khi2_critique2 = stats.chi2.ppf(
    1-ALPHA,df=ddl_khi2_2
)
p_manuel2 = stats.chi2.sf(khi2_manuel2,df=ddl_khi2_2)
print('Degres de liberte : ',ddl_khi2_2)
print('khi-2 critique : ', round(khi2_critique2,4))
print(f'P value : {p_manuel2:.4e}')

khi2_scipy2, p_scipy2, ddl_scipy2, E_scipy2 = (
    stats.chi2_contingency(observe2)
)
print('khi-2 avec scipy : ',round(khi2_scipy2,4))
print(f'P-Value Scipy : {p_scipy2:.4e}')
print('ddl Scipy : ',ddl_scipy2)

print('Resultats Identiques : ',np.isclose(khi2_manuel2,khi2_scipy2))
print('Effectifs theoriques identiques : ',np.allclose(effectifs_theoriques2,E_scipy2))

print('Effetif theoriques minimum : ',round(theorique2.to_numpy().min(),4))
condition2 = (theorique2.to_numpy() >= 5).all()
print('Tous les effectifs theoriques >= 5 : ',condition2)

if condition2 : 
    if khi2_manuel2 > khi2_critique2 : 
        print('khi-2 > khi-2 critique : rejet H0')
    else : 
        print('Khi-2 <= khi-2 critique : H0 non rejete ')
    if p_scipy2 < ALPHA : 
        print("Association statistiquement significative")
    else :
        print('Association non significative')
else : 
    print("Condition E >= 5 non respectee")
    print("La validite du test doit etre examinee")

V_cramer2 = np.sqrt(khi2_manuel2/(n_total2 * min(L2-1,C2-1)))
print('V de cramer : ',round(V_cramer2, 4))
pourcentages2 = observe2.div(observe2.sum(axis=1),axis=0)*100
print('Pourcentages par sexe : ',pourcentages2.round(2))

pourcentages2.plot(
    kind='bar',
    stacked=True,
    figsize=(9, 5)
)
plt.title('Répartition des filières selon le sexe')
plt.xlabel('Sexe')
plt.ylabel('Pourcentage des étudiants (%)')
plt.legend(title='Filière')
plt.xticks(rotation=0)
plt.ylim(0,100)
plt.tight_layout()
#plt.show()
sauvegarder_graph("09_khi2_sexe.png")