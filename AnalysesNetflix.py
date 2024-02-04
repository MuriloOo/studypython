#IMPORTANDO LIBS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Extraindo os dados e Analisando as primeiras linhas
netflix = pd.read_csv('netflix_titles.csv')
netflix.head()

#Verificando as ultimas linhas
netflix.tail()

#Resumo do dataframe
netflix.info()

#Tipos dos dados das colunas
netflix.dtypes

#Resumo Estatistico do DataFrame
netflix.describe()

#Quantidade de Linhas e Colunas
netflix.shape

netflix.index

#Verificando quaias colunas tem valores Nulos ou Vazios
netflix.isna().any()

#Verificando a Quatidade de Nulos e Vazios por coluna
netflix.isnull().sum()

#Retirando todas as linhas com valores Nulos
netflix.dropna(subset =['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description'], inplace = True)

#Novo total de colunas
netflix.shape

#Verificar quais sao os dados variaveis das colunas abaixo
print(netflix['type'].unique())
print(netflix['director'].unique())
print(netflix['rating'].unique())
print(netflix['release_year'].unique())

#Remover posssiveis colunas duplicados
netflix[netflix.duplicated()]

#Removendo linhas duplicadas e vende a QTD de linhas que ainda esta duplicadas
netflix.drop_duplicates(inplace = True)
netflix.duplicated().sum()

netflix

netflix["type"] = netflix["type"].astype("category")
netflix["country"] = netflix["country"].astype("category")
netflix["listed_in"] = netflix["listed_in"].astype("category")
netflix

netflix.dtypes

#Criando coluna do mes
netflix["added_month"] = netflix["date_added"].astype(str).str[:3]
netflix

# Contando a coluna types por valor
contagem_type = netflix['type'].value_counts()

# Criação do grafico
plt.figure(figsize=(6,4))
plt.bar(contagem_type.index,
        contagem_type.values,
        color = ['blue' , 'red'])
plt.title ('Qtd Movies x TV Shows')
plt.xlabel('Tipo')
plt.ylabel('Quantidade')
plt.show()

cont_teste = netflix['type'].value_counts()
print(cont_teste)

# Contando a coluna types por valor
contagem_year = netflix['release_year'].value_counts()

# Criação do grafico
plt.figure(figsize=(10,6))
plt.bar(contagem_year.index,
        contagem_year.values,
        color = ['skyblue'])
plt.title ('Lançamento por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.show()

contagem_anos = netflix['release_year'].value_counts().head(10)
print(contagem_anos)

# Contando a coluna types por valor
contagem_rating = netflix['rating'].value_counts()

# Criação do grafico
plt.figure(figsize=(8,4))
plt.bar(contagem_rating.index,
        contagem_rating.values,
        color = ['black'])
plt.title ('Rating')
plt.xlabel('Rating')
plt.ylabel('Quantidade')
plt.show()

# Criação do grafico
contagem_rating.plot.barh(stacked = True)
plt.xlabel('Rating')
plt.ylabel('Quantidade')
plt.gca().invert_yaxis() #Caso quiser inverter o valor dos dados
