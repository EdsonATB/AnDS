import streamlit as st
import pandas as pd
from app.youtube_comment_extractor import YouTubeCommentExtractor
from sentiment_analysis import analyze_sentiments
from YouTubeScraper import  robo_get_video_id
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

if search_button and search_text:
    pesquisa = search_text
    with st.spinner('Aguarde, estamos buscando os comentários...'):
           # Obter o ID do vídeo
            video_id = robo_get_video_id(pesquisa)

            # Extrair comentários do YouTube
            extractor = YouTubeCommentExtractor(api_key, video_id)
            try:
                comments = extractor.run(file_path)  # Certifique-se de que 'run' retorna a lista de comentários
            except Exception as e:
                print ("error: Erro ao extrair comentários: {str(e)}")

            # Certificar-se de que os comentários são uma lista válida
            if not comments or not isinstance(comments, list):
                print("error: Nenhum comentário foi extraído ou o formato dos dados está incorreto.")

            # Analisar sentimentos dos comentários
            sentiment_results = analyze_sentiments(comments)
            print(sentiment_results)
            
            df = pd.DataFrame(sentiment_results)
            st.write("Comentários analisados:")
            st.dataframe(df, use_container_width=True)
            
            
        
