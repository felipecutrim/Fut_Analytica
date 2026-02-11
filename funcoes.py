import requests
import os
import streamlit as st
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4/"

def obter_codigo_liga(nome_liga):
    """Retorna o código da liga com base no nome selecionado."""
    codigos = {
        "Campeonato Brasileiro Série A": "BSA",
        "Premier League": "PL",
        "Ligue 1": "FL1",
        "Bundesliga": "BL1",
        "Serie A": "SA",
        "La Liga": "PD",
        "Eredivisie": "DED",
        "Primeira Liga": "PPL"
    }
    return codigos.get(nome_liga)

@st.cache_data(ttl=3600)  # Cache de 1 hora para economizar requisições
def obter_dados_ligas(codigo_liga, temporada):
    """Busca a tabela de classificação da liga na API."""
    url = f"{BASE_URL}competitions/{codigo_liga}/standings?season={temporada}"
    headers = {"X-Auth-Token": API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # A API retorna standings = lista de tabelas (TOTAL, HOME, AWAY)
        # Vamos pegar a tabela TOTAL (índice 0)
        tabela_total = data['standings'][0]['table']
        return tabela_total, "API Online"
        
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return None, "Erro"

@st.cache_data(ttl=3600)
def obter_dados_artilheiros(codigo_liga, temporada):
    """Busca os artilheiros da liga."""
    url = f"{BASE_URL}competitions/{codigo_liga}/scorers?season={temporada}&limit=20"
    headers = {"X-Auth-Token": API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['scorers']
    except Exception as e:
        st.error(f"Erro ao buscar artilheiros: {e}")
        return None

def obter_dados_historicos(codigo_liga, temporada_atual):
    """Simula busca de dados históricos recursivamente para as últimas 3 temporadas."""
    historico = {}
    ano_atual = int(temporada_atual)
    
    # Busca dados dos últimos 3 anos
    for ano in range(ano_atual, ano_atual - 3, -1):
        dados, status = obter_dados_ligas(codigo_liga, str(ano))
        if status == "API Online" and dados:
            # Simplificando os dados para salvar no histórico
            lista_times = []
            for time in dados:
                lista_times.append({
                    'nome': time['team']['shortName'],
                    'gols_pro': time['goalsFor'],
                    'pontos': time['points']
                })
            historico[str(ano)] = lista_times
            
    return historico
