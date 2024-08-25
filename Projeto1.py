import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados do arquivo CSV usando o caminho fornecido
file_path = r"C:\Users\01002452\OneDrive - Faculdade São Leopoldo Mandic\Área de Trabalho\PYTHON\amazon.csv"
data = pd.read_csv(file_path, encoding='latin1')

# Título da Aplicação
st.title('Análise de Incêndios Florestais no Brasil')

# Exibição da tabela de dados
st.subheader('Dados dos Incêndios Florestais')
st.dataframe(data)

# Gráfico de tendência de incêndios ao longo do tempo
st.subheader('Tendência de Incêndios ao Longo dos Anos')
fig, ax = plt.subplots()
sns.lineplot(data=data, x='year', y='number', hue='state', ax=ax)
plt.title('Número de Incêndios por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Incêndios')
st.pyplot(fig)

# Gráfico de sazonalidade
st.subheader('Sazonalidade dos Incêndios')
fig2, ax2 = plt.subplots()
sns.boxplot(data=data, x='month', y='number', ax=ax2)
plt.title('Distribuição Mensal dos Incêndios')
plt.xlabel('Mês')
plt.ylabel('Número de Incêndios')
st.pyplot(fig2)

# Gráfico de distribuição geográfica
st.subheader('Distribuição Geográfica dos Incêndios')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(data=data.groupby('state')['number'].sum().reset_index().sort_values('number', ascending=False), x='number', y='state', ax=ax3)
plt.title('Número Total de Incêndios por Estado')
plt.xlabel('Número de Incêndios')
plt.ylabel('Estado')
st.pyplot(fig3)
