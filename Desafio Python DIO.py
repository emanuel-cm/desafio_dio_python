#extraindo relatório csv que contem a lista dos moradores da vila do Chaves e agrupando por casa, salvando em novo arquivo.
import pandas as pd

base_de_dados = 'Base de Dados Desafio.csv'

dados = pd.read_csv(C:\Users\emanu\OneDrive\Área de Trabalho\Bootcamp Santander)

dados_agrupados = dados.groupby('Casa').mean()
print(dados_agrupados)

dados.to_csv('dados_agrupados.csv', index = False)