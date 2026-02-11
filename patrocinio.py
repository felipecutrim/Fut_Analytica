import pandas as pd
import numpy as np
import streamlit as st
from funcoes import obter_dados_ligas

def calcular_valor_patrocinio(codigo_liga, temporada):
    """
    Calcula um 'Score de Valuation' fictício para patrocínio.
    Lógica: (Pontos * 1000) + (Gols * 500) + (Fator Aleatório de Engajamento)
    """
    dados, status = obter_dados_ligas(codigo_liga, temporada)
    
    if not dados:
        return None
        
    lista_valuation = []
    
    # Criando fatores de mercado fictícios para simular valuation
    fator_liga = 1.5 if codigo_liga in ['PL', 'PD'] else 1.0  # Premier League vale mais
    
    for time in dados:
        pontos = time['points']
        gols = time['goalsFor']
        posicao = time['position']
        
        # Fórmula de Valuation Simplificada
        # Quanto menor a posição (1º, 2º...), maior o valor
        bonus_campeao = 50000 if posicao == 1 else 0
        
        valor_base = (pontos * 2500) + (gols * 1000) + bonus_campeao
        valor_final = valor_base * fator_liga
        
        # ROI Score: Retorno sobre Investimento (Eficiência)
        # Gols por Milhão Investido (simulado)
        roi_score = (gols / valor_final) * 10000 
        
        lista_valuation.append({
            'Time': time['team']['shortName'],
            'Escudo': time['team']['crest'],
            'Posição': posicao,
            'GP': gols,
            'Pontos': pontos,
            'Valor_Patrocinio': valor_final,
            'ROI_Score': roi_score
        })
        
    df = pd.DataFrame(lista_valuation)
    return df
