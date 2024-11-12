import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import plotly.express as px
from sentiment_analysis import analyze_sentiments
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
file_path = os.getenv('FILE_PATH')

st.title('Relatório de Sentimentos dos Comentários do YouTube')
st.write(" ")
st.write(" ")
left, right = st.columns(2, vertical_alignment="bottom")

search_text = left.text_input("Digite o texto a ser pesquisado")
search_button = right.button("Pesquisar 🔍")

# Criar um DataFrame vazio com 10 linhas de dados fictícios
empty_data = {
    "text": [
        "Comentário 1", "Comentário 2", "Comentário 3", "Comentário 4", "Comentário 5",
        "Comentário 6", "Comentário 7", "Comentário 8", "Comentário 9", "Comentário 10"
    ],
    "sentiment": [
        "Positive", "Negative", "Neutral", "Positive", "Negative",
        "Neutral", "Positive", "Neutral", "Negative", "Positive"
    ],
    "confidence": [
        "80%", "55%", "60%", "90%", "70%",
        "65%", "85%", "75%", "50%", "95%"
    ]
}

empty_df = pd.DataFrame(empty_data)

def search_youtube_video_id(query, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 1,
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("items")
        if results:
            return results[0]["id"]["videoId"]
        else:
            return None
    else:
        print("Erro na requisição:", response.status_code)
        return None

def get_youtube_comments(video_id, api_key, max_results=11):
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": max_results,
        "order": "time",
        "textFormat": "plainText",
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        comments_data = response.json().get("items", [])
        comments = []

        # Extrai o conteúdo de cada comentário
        for item in comments_data:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            author = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            comments.append({"author": author, "comment": comment})

        return comments
    else:
        print("Erro na requisição:", response.status_code)
        return None

# Exibir DataFrame vazio com 10 linhas de exemplo caso não haja pesquisa
if not search_text:
    st.write("Comentários analisados:")
    st.dataframe(empty_df, use_container_width=True)

# Executa a pesquisa e análise se houver um texto de pesquisa
elif search_button and search_text:
    pesquisa = search_text
    with st.spinner('Aguarde, estamos buscando os comentários...'):
        video_id = search_youtube_video_id(pesquisa, api_key)
        
        if not video_id:
            st.error("Não foi possível encontrar um vídeo com a pesquisa fornecida.")
        else:
            comments = get_youtube_comments(video_id, api_key, max_results=11)
            
            if not comments:
                st.error("Nenhum comentário foi extraído ou o formato dos dados está incorreto.")
            else:
                # Analisar sentimentos dos comentários
                sentiment_results = analyze_sentiments([comment['comment'] for comment in comments])
                
                # Criar DataFrame com sentimentos
                df = pd.DataFrame(sentiment_results)
                st.write("Comentários analisados:")
                st.dataframe(df, use_container_width=True)
                
                # Contagem de sentimentos para os gráficos e cards
                sentiment_counts = df['sentiment'].value_counts()

                # Exibir as métricas lado a lado
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Comentários Positivos", sentiment_counts.get('Positive', 0))
                with col2:
                    st.metric("Comentários Negativos", sentiment_counts.get('Negative', 0))
                with col3:
                    st.metric("Comentários Neutros", sentiment_counts.get('Neutral', 0))

                # Criar um expander para os gráficos
                with st.expander("Ver Gráficos"):
                    # Criar colunas para gráficos lado a lado dentro do expander
                    col1, col2 = st.columns(2)

                    # Gráfico de barras usando matplotlib (tamanho ajustado)
                    with col1:
                        fig, ax = plt.subplots(figsize=(4, 2))  # Tamanho reduzido do gráfico
                        ax.bar(sentiment_counts.index, sentiment_counts.values, color=['#FF6F61', '#6BAED6', '#B3DE69'])
                        ax.set_title("Distribuição de Sentimentos", fontsize=10, color='white')  # Diminuir o tamanho da fonte do título
                        ax.set_xlabel("Sentimento", fontsize=8, color='white')  # Diminuir tamanho e mudar cor
                        ax.set_ylabel("Quantidade de Comentários", fontsize=8, color='white')  # Diminuir tamanho e mudar cor
                        
                        # Personalizar o tamanho e a cor das legendas dos eixos
                        ax.tick_params(axis='x', labelsize=5, labelcolor='white')  # Diminuir e mudar cor dos rótulos do eixo X
                        ax.tick_params(axis='y', labelsize=5, labelcolor='white')  # Diminuir e mudar cor dos rótulos do eixo Y
                        
                        fig.patch.set_facecolor('none')  # Fundo transparente
                        st.pyplot(fig)

                    # Gráfico de pizza usando Plotly (tamanho ajustado)
                    with col2:
                        fig_pie = px.pie(
                            values=sentiment_counts.values, 
                            names=sentiment_counts.index,
                            title="Distribuição de Sentimentos",
                            color_discrete_sequence=px.colors.qualitative.Pastel
                        )
                        fig_pie.update_layout(
                            width=350, height=450,  # Tamanho ajustado
                            font=dict(size=10, color='darkblue'),  # Ajuste da cor das legendas
                            title_font=dict(size=15, color='white')  # Título em branco
                        )
                        st.plotly_chart(fig_pie)
