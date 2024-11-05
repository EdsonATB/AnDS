import streamlit as st
import pandas as pd
from main import YouTubeCommentExtractor
from sentiment_analysis import analyze_sentiments
from YouTubeScraper import  robo_get_video_id
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
file_path = os.getenv('FILE_PATH')

st.set_page_config(page_title='Comment Gauge', page_icon='📊', layout='wide')



st.title('Comment Gauge')

col1, col2 = st.columns([3, 1])	


with col1:
    search_text = st.text_input("Digite o tema")


with col2:
    search_button = st.button("Buscar", use_container_width=True)


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
            
            #python -m streamlit run app\streamlit.py use este comando para rodar o streamlit
        
