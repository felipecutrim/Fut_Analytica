import pandas as pd
import streamlit as st

def data_frames(dados_json):
    """Transforma o JSON da classificação em um DataFrame Pandas."""
    lista_times = []
    
    for item in dados_json:
        time_info = {
            'posicao': item['position'],
            'escudo': item['team']['crest'],
            'nome': item['team']['shortName'],
            'pontos': item['points'],
            'jogos': item['playedGames'],
            'vitorias': item['won'],
            'empates': item['draw'],
            'derrotas': item['lost'],
            'gols_pro': item['goalsFor'],
            'gols_contra': item['goalsAgainst'],
            'saldo_gols': item['goalDifference']
        }
        lista_times.append(time_info)
        
    df = pd.DataFrame(lista_times)
    return df

def data_frames_artilheiros(dados_json):
    """Transforma o JSON de artilheiros em DataFrame."""
    lista_artilheiros = []
    
    for item in dados_json:
        jogador = {
            'nome': item['player']['name'],
            'gols': item['goals'],
            'assistencias': item.get('assists', 0), # Alguns podem não ter esse campo
            'time': item['team']['shortName'],
            'escudo': item['team']['crest']
        }
        lista_artilheiros.append(jogador)
        
    df = pd.DataFrame(lista_artilheiros)
    return df

def melhor_ataque(df):
    """Retorna o time com mais gols marcados."""
    if df.empty: return None
    return df.sort_values(by='gols_pro', ascending=False).iloc[0].to_dict()

def melhor_defesa(df):
    """Retorna o time com menos gols sofridos."""
    if df.empty: return None
    return df.sort_values(by='gols_contra', ascending=True).iloc[0].to_dict()
