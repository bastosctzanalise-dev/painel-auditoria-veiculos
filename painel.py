import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Painel de Auditorias de Veículos 🚗")

uploaded_file = st.file_uploader("Carregue o relatório (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel("Relatorio_Empresas_Abril_2026.xlsx")


    st.subheader("📊 Dados brutos")
    st.dataframe(df)

    # Filtro por empresa
    empresa = st.selectbox("Selecione a empresa:", df["Empresa"].unique())
    df_empresa = df[df["Empresa"] == empresa]
    st.write(df_empresa)

    # Gráfico de barras por categoria da empresa selecionada
    st.subheader(f"Distribuição de categorias - {empresa}")
    fig, ax = plt.subplots()
    df_empresa["Categoria"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # Gráfico de pizza por empresa
    st.subheader(f"Proporção de categorias - {empresa}")
    fig3, ax3 = plt.subplots()
    df_empresa["Categoria"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax3)
    ax3.set_ylabel("")  # remove label lateral
    st.pyplot(fig3)

    # Gráfico consolidado por empresa e categoria
    st.subheader("📈 Comparativo Consolidado entre Empresas")
    resumo = df.groupby(["Empresa", "Categoria"]).size().unstack(fill_value=0)

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    resumo.plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Quantidade de Auditorias")
    ax2.set_title("Resumo por Empresa e Categoria")
    st.pyplot(fig2)

    st.write("Resumo consolidado em tabela:")
    st.dataframe(resumo)
else:
    st.info("Por favor, carregue o arquivo Excel para visualizar o painel.")
