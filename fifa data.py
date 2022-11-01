# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:32:54 2020

@author: Nicolas Cruz
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/nicoc/OneDrive/Desktop/Futbol/players_20.csv")
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
  "Arsenal", "Bournemouth", "Brighton & Hove Albion", "Burnley",
  "Cardiff City", "Chelsea", "Crystal Palace", "Everton", "Fulham",
  "Huddersfield Town", "Leicester City", "Liverpool", "Manchester City",
  "Manchester United", "Newcastle United", "Southampton", 
  "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers" 
]

laliga = [
  "Athletic Club de Bilbao", "Atlético Madrid", "CD Leganés",
  "Deportivo Alavés", "FC Barcelona", "Getafe CF", "Girona FC", 
  "Levante UD", "Rayo Vallecano", "RC Celta", "RCD Espanyol", 
  "Real Betis", "Real Madrid", "Real Sociedad", "Real Valladolid CF",
  "SD Eibar", "SD Huesca", "Sevilla FC", "Valencia CF", "Villarreal CF"
]

seriea = [
  "Atalanta","Bologna","Cagliari","Chievo Verona","Empoli", "Fiorentina","Frosinone","Genoa",
  "Inter","Juventus","Lazio","Milan","Napoli","Parma","Roma","Sampdoria","Sassuolo","SPAL",
  "Torino","Udinese"
]

superlig = [
  "Akhisar Belediyespor","Alanyaspor", "Antalyaspor","Medipol Başakşehir FK","BB Erzurumspor","Beşiktaş JK",
  "Bursaspor","Çaykur Rizespor","Fenerbahçe SK", "Galatasaray SK","Göztepe SK","Kasimpaşa SK",
  "Kayserispor","Atiker Konyaspor","MKE Ankaragücü", "Sivasspor","Trabzonspor","Yeni Malatyaspor"
]

ligue1 = [
  "Amiens SC", "Angers SCO", "AS Monaco", "AS Saint-Étienne", "Dijon FCO", "En Avant de Guingamp",
  "FC Nantes", "FC Girondins de Bordeaux", "LOSC Lille", "Montpellier HSC", "Nîmes Olympique", 
  "OGC Nice", "Olympique Lyonnais","Olympique de Marseille", "Paris Saint-Germain", 
  "RC Strasbourg Alsace", "Stade Malherbe Caen", "Stade de Reims", "Stade Rennais FC", "Toulouse Football Club"
]

eredivisie = [
  "ADO Den Haag","Ajax", "AZ Alkmaar", "De Graafschap","Excelsior","FC Emmen","FC Groningen",
  "FC Utrecht", "Feyenoord","Fortuna Sittard", "Heracles Almelo","NAC Breda",
  "PEC Zwolle", "PSV","SC Heerenveen","Vitesse","VVV-Venlo","Willem II"
]

liganos = [
  "Os Belenenses", "Boavista FC", "CD Feirense", "CD Tondela", "CD Aves", "FC Porto",
  "CD Nacional", "GD Chaves", "Clube Sport Marítimo", "Moreirense FC", "Portimonense SC", "Rio Ave FC",
  "Santa Clara", "SC Braga", "SL Benfica", "Sporting CP", "Vitória Guimarães", "Vitória de Setúbal"
]

ligamx = [
    "Tigres U.N.L.A.", "Monterrey", "Cruz Azul", "Club América", "Club León", "Club Tijuana",
    "Santo Laguna", "Pachuca", "Guadalajara", "U.N.A.M.", "Deportivo Toluca", "Club Atlas", 
    "Atlético de San Luis", "Puebla FC", "Mazatlán FC", "FC Juárez", "Club Necaxa", "Querétaro"
]

df_chile.reset_index(inplace=True)
df_chile['League'] = ['Liga']*370
for i in df_chile.index:
    conditions = [
    (df_chile.loc[i]['club'] in bundesliga),
    (df_chile.loc[i]['club'] in premierLeague),
    (df_chile.loc[i]['club'] in laliga),
    (df_chile.loc[i]['club'] in seriea),
    (df_chile.loc[i]['club'] in superlig),
    (df_chile.loc[i]['club'] in ligue1),
    (df_chile.loc[i]['club'] in eredivisie),
    (df_chile.loc[i]['club'] in liganos),
    (df_chile.loc[i]['club'] in ligamx),
    ]
    choices = ['bundesliga',"premier league","la liga","serie a","super liga","ligue 1","eredivise","liganos", "ligamx"]
    df_chile['League'][i] = np.select(conditions, choices, default = 'Other')  



df_uruguay.reset_index(inplace=True)
df_uruguay['League'] = ['Liga']*164
for i in df_uruguay.index:
    conditions = [
    (df_uruguay.loc[i]['club'] in bundesliga),
    (df_uruguay.loc[i]['club'] in premierLeague),
    (df_uruguay.loc[i]['club'] in laliga),
    (df_uruguay.loc[i]['club'] in seriea),
    (df_uruguay.loc[i]['club'] in superlig),
    (df_uruguay.loc[i]['club'] in ligue1),
    (df_uruguay.loc[i]['club'] in eredivisie),
    (df_uruguay.loc[i]['club'] in liganos),
    (df_uruguay.loc[i]['club'] in ligamx),
    ]
    choices = ['bundesliga',"premier league","la liga","serie a","super liga","ligue 1","eredivise","liganos", "ligamx"]
    df_uruguay['League'][i] = np.select(conditions, choices, default = 'Other')  

for league in choices:  
    plt.bar(league, (df_chile['League']==league).sum(), color = 'tab:red', align='edge')
    plt.bar(league + '1', (df_uruguay['League']==league).sum(), color = 'tab:cyan') 
    plt.xticks(np.arange(0.5,18.5,2), choices)
    plt.xticks(rotation = 'vertical')
    plt.title('Numero de Jugadores Participando por Liga')
    plt.legend(['Chile', 'Uruguay'])
plt.tight_layout()
plt.savefig('Numero de jugadores participando por liga.png', dpi = 300)

