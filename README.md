# Fut.Analytica Portfolio ⚽

Projeto de análise de dados de futebol desenvolvido em Python e Streamlit. Focado em extração de dados via API, manipulação de DataFrames e visualização interativa para tomada de decisão estratégica (Valuation de Patrocínio).

## 📊 Funcionalidades
- **Classificação e Estatísticas**: Tabelas atualizadas das principais ligas (Brasileirão, Premier League, La Liga, etc).
- **Análise de Performance**: Gráficos de dispersão interativos (Ataque vs Defesa) para identificar padrões táticos.
- **Valuation Inteligente**: Algoritmo de decisão que cruza dados de engajamento e performance para sugerir o "ROI de Patrocínio" (Retorno sobre Investimento) dos times.

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem principal.
- **Streamlit**: Framework para construção do Web App interativo.
- **Pandas**: Limpeza e manipulação de dados complexos.
- **Plotly**: Visualizações dinâmicas e interativas.
- **API Integration**: Consumo da API `football-data.org` com autenticação segura.

## 🚀 Como Executar o Projeto

1. **Clone este repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/fut-analytics-portfolio.git
   cd fut-analytics-portfolio
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure a Segurança (Token)**
   - Este projeto usa variáveis de ambiente para proteger a chave da API.
   - Crie um arquivo chamado `.env` na raiz do projeto.
   - Adicione sua chave (que pode ser obtida gratuitamente no [football-data.org](https://www.football-data.org)):
     ```env
     API_KEY=sua_chave_api_aqui
     ```

4. **Execute a aplicação**
   ```bash
   streamlit run main.py
   ```

## 🎯 Objetivo do Projeto
Demonstrar competências em Engenharia de Dados (Coleta/API), Análise Exploratória e Business Intelligence aplicado ao esporte.

---
**Autor:** [Seu Nome Aqui]
**Contato:** [Seu LinkedIn/Email]
