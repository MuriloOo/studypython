#Import Libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import base
xbox = pd.read_csv('Gamepass_Games_v1.csv')
#xbox = pd.read_csv('/kaggle/input/xbox-game-pass-games-library/Gamepass_Games_v1.csv')
xbox.head(10)

xbox.rename(columns={'COMP %': 'Porcentagem'}, inplace=True)

#Resum DataFrame
xbox.info()

#Type data columns
xbox.dtypes

#Resum Statiscts DataFrame
xbox.describe()

#Amount Rows and Columns
xbox.shape

xbox.index

#Verifying DataSet Columns
xbox.columns

#Verifying Columns with NULL
xbox.isna().any()

#Verifying Amount of Columns with NULL
xbox.isnull().sum()

#Removing Null Values
xbox.dropna(subset = ['GAME', 'RATIO', 'GAMERS', 'Porcentagem', 'TIME', 'RATING', 'ADDED','True_Achievement', 'Game_Score'], inplace = True)

#Checking for Null Values
xbox.isnull().sum()

#Cheking Columns and Rows
xbox.shape

#Checking Data from Distinct Columns
print(xbox['TIME'].unique())
print('\n')
print(xbox['Porcentagem'].unique())

#remove duplicate columns
xbox[xbox.duplicated()]

#CREATING FUNCTION TO ROUND RATING SCORES
def agrupar_notas(xbox, RATING):
  xbox['Nota_round'] = xbox[RATING].round().astype(int)
  return xbox

#CREATE FUNCTION TO ROUND %
def agrupar_Porcentagem(xbox, Porcentagem):
  xbox['Porcen_round'] = xbox[Porcentagem].round().astype(int)
  return xbox

xbox = agrupar_notas(xbox, 'RATING')
xbox = agrupar_Porcentagem(xbox ,'Porcentagem')
xbox

#Checking the Distinct Data of the Columns
print('Porcentagem = ' , xbox['Porcen_round'].unique())
print('\n')
print('Nota = ' , xbox['Nota_round'].unique())
print('\n')
print('Tempo = ', xbox['TIME'].unique())

#Creating Count for the 'TIME' Column
cont_tempo = xbox['TIME'].value_counts()

#Creating Graphics
cont_tempo.plot.barh(stacked = True , color = ['chocolate'])
plt.xlabel('Amount')
plt.ylabel('Average time to finish the game')
plt.title('Amount of Time to End Game')

#Grouping Percent column
bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 100]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
xbox['agrupamento_Porcen_round'] = pd.cut(xbox['Porcen_round'], bins=bins, labels=labels)
xbox.head()

#Count Grouping Percent
cont_porcentagem = xbox['agrupamento_Porcen_round'].value_counts()
cont_porcentagem

#Grouping Percent column
plt.bar(cont_porcentagem.index,
        cont_porcentagem.values,
        color = ['blue'])
plt.xlabel('Amount')
plt.ylabel('%')
plt.title('Percentage of players who beat the games')
plt.show()
print('\n')
print(cont_porcentagem)

#Creating Count for the 'Nota_round' Column
cont_nota = xbox['Nota_round'].value_counts()

#Grapichs Nota
plt.bar(cont_nota.index,
        cont_nota.values,
        color = ['black'])
plt.xlabel('Amount')
plt.ylabel('Notas')
plt.title('Rating')
plt.show()
print('\n')
print(cont_nota)

xbox['GAMERS'].max

#CREATE FUNCTION TO GAMERS

#CONVERT FORMAT OF ROWS "," to " "
xbox['GAMERS'] = xbox['GAMERS'].str.replace(',', '').astype(int)

#Setting Group Boundaries
bins = [0, 50000, 80000, 120000, 200000, 230000]
labels = ['0-49.999', '50.000-79.999', '80.000-119.999', '120.000-199.999', '200.000-230.000']

#Creating the new 'GAMERS_GROUP' column with the groups
xbox['qtd_gamers'] = pd.cut(xbox['GAMERS'], bins=bins, labels=labels, include_lowest = True )

#PRINT
xbox.head(10)

#COUNT qtd_gamers
cont_qtd_gamers = xbox['qtd_gamers'].value_counts()

#Grapichs qtd_gamers
plt.figure(figsize=(8,4))
plt.bar(cont_qtd_gamers.index,
        cont_qtd_gamers.values,
        color = ['red'])
plt.xlabel('Amount')
plt.ylabel('Notas')
plt.title('Rating')
plt.show()
print('\n')
print(cont_qtd_gamers)

#Graphic Amount Gamers per game vs Rating 
plt.figure(figsize = (10,6))
sns.histplot(data = xbox, x='qtd_gamers', hue = 'Nota_round', palette='viridis')
plt.show()
