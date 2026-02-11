import streamlit as st
import pandas as pd
import plotly.express as px
from funcoes import *
from data_frames import *
from patrocinio import calcular_valor_patrocinio

def main():
    st.set_page_config(page_title="Fut.Analytica Portfolio", layout="wide", page_icon="⚽")
    
    st.title("Fut.Analytica Portfolio ⚽")
    st.write("Análise de dados de futebol para tomada de decisão em patrocínios.")

    # Sidebar
    st.sidebar.header("Filtros")
    ligas_disponiveis = [
        "Campeonato Brasileiro Série A", "Premier League", 
        "Ligue 1", "Bundesliga", "Serie A", "La Liga"
    ]
    escolha_liga = st.sidebar.selectbox("Escolha um campeonato:", ligas_disponiveis)
    
    anos = [str(y) for y in range(2024, 2020, -1)]
    escolha_season = st.sidebar.selectbox("Temporada:", anos)

    if st.sidebar.button("Analisar Dados"):
        codigo_liga = obter_codigo_liga(escolha_liga)
        
        if codigo_liga:
            with st.spinner("Buscando dados na API..."):
                dados, fonte = obter_dados_ligas(codigo_liga, escolha_season)
                dados_artilheiros = obter_dados_artilheiros(codigo_liga, escolha_season)
            
            if dados:
                # Processamento
                df_tabela = data_frames(dados)
                
                # Layout de Colunas
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.subheader("Tabela de Classificação")
                    st.dataframe(
                        df_tabela[['posicao', 'escudo', 'nome', 'pontos', 'jogos', 'vitorias', 'gols_pro', 'saldo_gols']],
                        column_config={
                            "escudo": st.column_config.ImageColumn("Escudo"),
                            "nome": "Time",
                            "gols_pro": "GP"
                        },
                        hide_index=True,
                        use_container_width=True
                    )
                    
                with col2:
                    st.subheader("Top Artilheiros")
                    if dados_artilheiros:
                        df_art = data_frames_artilheiros(dados_artilheiros)
                        st.dataframe(
                            df_art[['nome', 'gols', 'time']].head(10),
                            hide_index=True,
                            use_container_width=True
                        )
                
                # Gráficos de Análise
                st.divider()
                st.subheader("📊 Análise de Performance")
                
                fig = px.scatter(
                    df_tabela, x='gols_pro', y='gols_contra',
                    text='nome', size='pontos',
                    title=f"Ataque vs Defesa - {escolha_liga}",
                    labels={'gols_pro': 'Gols Marcados', 'gols_contra': 'Gols Sofridos'},
                    color='saldo_gols', color_continuous_scale='RdYlGn'
                )
                fig.update_traces(textposition='top center')
                st.plotly_chart(fig, use_container_width=True)
                
                # Valuation
                st.divider()
                st.subheader("💰 Valuation Inteligente")
                
                df_val = calcular_valor_patrocinio(codigo_liga, escolha_season)
                
                if df_val is not None:
                    col_val1, col_val2 = st.columns(2)
                    
                    with col_val1:
                        st.markdown("##### Oportunidade de Ouro (ROI)")
                        best_roi = df_val.sort_values(by='ROI_Score', ascending=False).iloc[0]
                        st.success(f"💎 O time **{best_roi['Time']}** é a melhor oportunidade custo-benefício.")
                        st.metric("Gols Entregues", best_roi['GP'])
                        st.metric("Score de Custo", f"{best_roi['Valor_Patrocinio']:,.0f}")
                        
                    with col_val2:
                        st.markdown("##### Top 5 Patrocínios Mais Caros")
                        st.dataframe(
                            df_val[['Time', 'Valor_Patrocinio', 'ROI_Score']].sort_values(by='Valor_Patrocinio', ascending=False).head(5),
                            hide_index=True
                        )

if __name__ == "__main__":
    main()
