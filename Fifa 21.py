# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:44:00 2020

@author: Nicolas Cruz
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/nicoc/OneDrive/Desktop/Futbol/FIFA-21 Complete.csv", delimiter = ';')
df.head()

df.info()
df.columns
df_chile = df.loc[df['nationality']=='Chile']
df_uruguay = df.loc[df['nationality']=='Uruguay']
df_uruguay.info
df_chile.info

#%%
#Create leagues

bundesliga = [
  "1. FC Nürnberg", "1. FSV Mainz 05", "Bayer 04 Leverkusen", "FC Bayern München",
  "Borussia Dortmund", "Borussia Mönchengladbach", "Eintracht Frankfurt",
  "FC Augsburg", "FC Schalke 04", "Fortuna Düsseldorf", "Hannover 96",
  "Hertha BSC", "RB Leipzig", "SC Freiburg", "TSG 1899 Hoffenheim",
  "VfB Stuttgart", "VfL Wolfsburg", "SV Werder Bremen"
]

premierLeague = [
  "Arsenal", "AFC Bournemouth", "Brighton & Hove Albion", "Burnley",
  "Cardiff City", "Chelsea", "Crystal Palace", "Everton", "Fulham",
  "Huddersfield Town", "Leicester City", "Liverpool", "Manchester City",
  "Manchester United", "Newcastle United", "Southampton", 
  "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers" 
]

laliga = [
  "Athletic Club", "Atlético Madrid", "CD Leganés",
  "D. Alavés", "FC Barcelona", "Getafe CF", "Girona FC", 
  "Levante UD", "Rayo Vallecano", "RC Celta", "RCD Espanyol", 
  "Real Betis", "Real Madrid", "Real Sociedad", "R. Valladolid CF",
  "SD Eibar", "SD Huesca", "Sevilla FC", "Valencia CF", "Villarreal CF"
]

seriea = [
  "Atalanta","Bologna","Cagliari","Chievo Verona","Empoli", "Fiorentina","Frosinone","Genoa",
  "Inter","Juventus","Lazio","Milan","Napoli","Parma","Roma","Sampdoria","Sassuolo","SPAL",
  "Torino","Udinese"
]

superlig = [
  "Akhisar Belediyespor","Alanyaspor", "Antalyaspor","Medipol Basaksehir FK","BB Erzurumspor","Besiktas JK",
  "Bursaspor","Çaykur Rizespor","Fenerbahçe SK", "Galatasaray SK","Göztepe SK","Kasimpasa SK",
  "Kayserispor","Konyaspor","MKE Ankaragücü", "Sivasspor","Trabzonspor","Yeni Malatyaspor"
]

ligue1 = [
  "Amiens SC", "Angers SCO", "AS Monaco Football Club SA", "AS Saint-Étienne", "Dijon FCO", "En Avant Guingamp",
  "FC Nantes", "FC Girondins de Bordeaux", "LOSC Lille", "Montpellier Hérault SC", "Nîmes Olympique", 
  "OGC Nice", "Olympique Lyonnais","Olympique de Marseille", "Paris Saint-Germain", 
  "RC Strasbourg Alsace", "Stade Malherbe Caen", "Stade de Reims", "Stade Rennais FC", "Toulouse Football Club"
]

eredivisie = [
  "ADO Den Haag","Ajax", "AZ", "De Graafschap","Excelsior","FC Emmen","FC Groningen",
  "FC Utrecht", "Feyenoord","Fortuna Sittard", "Heracles Almelo","NAC Breda",
  "PEC Zwolle", "PSV","SC Heerenveen","Vitesse","VVV-Venlo","Willem II"
]

liganos = [
  "Belenenses", "Boavista FC", "CD Feirense", "CD Tondela", "Desportivo das Aves", "FC Porto",
  "CD Nacional", "GD Chaves", "Marítimo", "Moreirense FC", "Portimonense SC", "Rio Ave FC",
  "Santa Clara", "SC Braga", "SL Benfica", "Sporting CP", "Vitória Guimarães", "Vitória Setúbal"
]

ligamx = [
    "Tigres U.A.N.L.", "Monterrey", "Cruz Azul", "Club América", "Club León", "Club Tijuana",
    "Santos Laguna", "Pachuca", "Guadalajara", "U.N.A.M.", "Deportivo Toluca", "Club Atlas", 
    "Club Atlético de San Luis", "Puebla FC", "Mazatlán FC", "Fútbol Club Juárez", "Club Necaxa", "Gallos Blancos de Querétaro"
]


 #%%
 #TEST
df.reset_index(inplace=True)
df['League'] = ['Liga']*17981
df['team'] = df['team'].str.strip()
for i in df.index:
    conditions = [
    (df.loc[i]['team'] in bundesliga),
    (df.loc[i]['team'] in premierLeague),
    (df.loc[i]['team'] in laliga),
    (df.loc[i]['team'] in seriea),
    (df.loc[i]['team'] in superlig),
    (df.loc[i]['team'] in ligue1),
    (df.loc[i]['team'] in eredivisie),
    (df.loc[i]['team'] in liganos),
    (df.loc[i]['team'] in ligamx),
    ]
    choices = ['bundesliga',"premier league","la liga","serie a","super liga","ligue 1","eredivise","liganos", "ligamx"]
    df['League'][i] = np.select(conditions, choices, default = 'Other')     

for league in choices:  
    plt.bar(league, (df['League']==league).sum(), color = 'tab:red', align='edge') 
    plt.xticks(rotation = 'vertical')
    plt.title('Numero de Jugadores Participando por Liga (FIFA21)')
plt.tight_layout()
#%%
#TEST
agg = 0
ligas = [bundesliga, premierLeague, laliga, seriea,superlig, ligue1, eredivisie, liganos, ligamx]
for liga in ligas:
    for team in liga:
        for i in df.index:
            agg = agg + int(team == df.loc[i]['team'])
        if agg == 0:
            print(team,agg)
        agg=0
     



#%%
df_chile.reset_index(inplace=True)
df_chile['League'] = ['Liga']*318
df_chile['team'] = df_chile['team'].str.strip()
for i in df_chile.index:
    conditions = [
    (df_chile.loc[i]['team'] in bundesliga),
    (df_chile.loc[i]['team'] in premierLeague),
    (df_chile.loc[i]['team'] in laliga),
    (df_chile.loc[i]['team'] in seriea),
    (df_chile.loc[i]['team'] in superlig),
    (df_chile.loc[i]['team'] in ligue1),
    (df_chile.loc[i]['team'] in eredivisie),
    (df_chile.loc[i]['team'] in liganos),
    (df_chile.loc[i]['team'] in ligamx),
    ]
    choices = ['bundesliga',"premier league","la liga","serie a","super liga","ligue 1","eredivise","liganos", "ligamx"]
    df_chile['League'][i] = np.select(conditions, choices, default = 'Other')  
df_chile.loc[df_chile['team']=='FC Barcelona']

df_uruguay.reset_index(inplace=True)
df_uruguay['League'] = ['Liga']*352
df_uruguay['team'] = df_uruguay['team'].str.strip()
for i in df_uruguay.index:   
    conditions = [
    (df_uruguay.loc[i]['team'] in bundesliga),
    (df_uruguay.loc[i]['team'] in premierLeague),
    (df_uruguay.loc[i]['team'] in laliga),
    (df_uruguay.loc[i]['team'] in seriea),
    (df_uruguay.loc[i]['team'] in superlig),
    (df_uruguay.loc[i]['team'] in ligue1),
    (df_uruguay.loc[i]['team'] in eredivisie),
    (df_uruguay.loc[i]['team'] in liganos),
    (df_uruguay.loc[i]['team'] in ligamx),
    ]
    choices = ['bundesliga',"premier league","la liga","serie a","super liga","ligue 1","eredivise","liganos", "ligamx"]
    df_uruguay['League'][i] = np.select(conditions, choices, default = 'Other')  

for league in choices:  
    plt.bar(league, (df_chile['League']==league).sum(), color = 'tab:red', align='edge')
    plt.bar(league + '1', (df_uruguay['League']==league).sum(), color = 'tab:cyan') 
    plt.yticks(np.arange(0,20,2))
    plt.xticks(np.arange(0.5,18.5,2), choices)
    plt.xticks(rotation = 'vertical')
    plt.title('Numero de Jugadores Participando por Liga (FIFA21)')
    plt.legend(['Chile', 'Uruguay'])
plt.tight_layout()
plt.savefig('Numero de jugadores participando por liga (FIFA 21).png', dpi = 300)