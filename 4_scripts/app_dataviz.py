import streamlit as st
import pandas as pd
import plotly.express as px

#Inserir um texto no site
st.write('***APP Futebol***')

#Inserir uma barra lateral com cabeçalho
st.sidebar.header('Escolha dos times')

#Fazer a leitura do BD que vamos trabalhar
df = pd.read_csv('../1_bases_tratadas/dadostratados.csv', sep=';', encoding='utf-8')

#Filtro com os times
times = df['home_team_name'].drop_duplicates()

#Inserir uma caixa de seleção na barra lateral
escolha_time = st.sidebar.selectbox('Escolha um time', times)

#Filtrando o BD com base na escolha do usuário
df2 = df[df['home_team_name']==escolha_time]

#Adiciona o texto que o usuário irá enxergar
st.write('Pontos por jogo do time mandante')

#Criar uma imagem do gráfico de caixa com a variável x da coluna home_ppg
fig = px.box (df2, x = 'home_ppg')

#Exibir a imagem do gráfico
st.plotly_chart(fig)

