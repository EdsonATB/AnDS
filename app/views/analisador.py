import os
import re
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from translatepy import Translator
from enviar_email import enviar_email
from gerar_pdf import gerar_pdf
from sentiment_analysis import analyze_sentiments
from YouTubeScraper import search_youtube_video_id, get_youtube_comments

load_dotenv()

api_key = os.getenv('API_KEY')

st.title('Relatório de Sentimentos dos Comentários do YouTube')
st.write(" ")
st.write(" ")
left, right, radio_btn = st.columns(3, vertical_alignment="bottom")

radio_buton = radio_btn.radio("Escolha uma opção", ["Pesquisar por nome", "Pesquisar por id"],
                            help="Onde conseguir o id do video ? O ID do vídeo é a sequência de caracteres depois de v= no link do vídeo no YouTube. Por exemplo, no link https://www.youtube.com/watch?v=abc123, abc123 é o ID do vídeo.")

if radio_buton == "Pesquisar por nome":
    search_text = left.text_input("Digite o texto a ser pesquisado")
if radio_buton == "Pesquisar por id":
    search_text = left.text_input("Digite o id do video")
    

search_button = right.button("Pesquisar 🔍")

# Pesquisa o texto digitado e exibe os comentários e análises de sentimentos
if search_button or search_text:
    with st.spinner('Aguarde, estamos buscando os comentários...'):

            if radio_buton == "Pesquisar por nome":
                pesquisa = search_text
                video_id = search_youtube_video_id(pesquisa, api_key)
                if not video_id:
                    st.error("Não foi possível encontrar um vídeo com a pesquisa fornecida.")


            if radio_buton == "Pesquisar por id":
                video_id = search_text
                if not video_id:
                    st.error("Não foi possível encontrar um vídeo com o id fornecido.")


            comments = get_youtube_comments(video_id, api_key, max_results=50)
            
            if not comments:
                st.error("Não foi possível encontrar um vídeo com o id fornecido.")
            else:
                # Traduzindo os comentários para o português
                translator = Translator()
                translated_comments = []
                for comment in comments:
                    try:
                        translated = translator.translate(comment['comment'], 'English')
                        translated_comments.append(translated.result)
                    except Exception as e:
                        print(f"Erro ao traduzir o comentário: {e}")
                        translated_comments.append(comment['comment'])  # Se falhar, mantém o comentário original

                # Realizando a análise de sentimentos nos comentários traduzidos
                sentiment_results = analyze_sentiments(translated_comments)
                
                # Convertendo os resultados para DataFrame e exibindo a url do video que foi ultilizada.
                df = pd.DataFrame(sentiment_results)
                video_url_used = f"https://www.youtube.com/watch?v={video_id}"
                st.markdown(f"[Ver o vídeo ultilizado]({video_url_used})", unsafe_allow_html=True)
                st.write("Comentários analisados:")
                st.dataframe(df, use_container_width=True)
            
                sentiment_counts = df['sentiment'].value_counts()
                

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Comentários Positivos", sentiment_counts.get('Positive', 0))
                with col2:
                    st.metric("Comentários Negativos", sentiment_counts.get('Negative', 0))
                with col3:
                    st.metric("Comentários Neutros", sentiment_counts.get('Neutral', 0))


                with st.expander("Ver Gráficos"):
                    col1, col2 = st.columns(2)

                    # Gráfico de barras usando matplotlib 
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

                    # Gráfico de pizza usando Plotly 
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
                email, dowload = st.columns(2, vertical_alignment="bottom")
                
                pdf_buf = gerar_pdf(df, video_url_used, sentiment_counts)
                
                @st.dialog("Enviar Relatório por E-mail 📧")
                def email_dialog():
                    with st.form("Envio de formulario por email"):
                        email = st.text_input("Digite o e-mail para envio do relatório")
                        submit_button = st.form_submit_button("Enviar")
                        if submit_button:
                            padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Regex que valida um e-mail

                            if re.match(padrao_email, email):
                                enviar_email(email, pdf_buf)  # Corrigido: passando o argumento necessário
                                st.success("E-mail enviado com sucesso!")
                            else:
                                st.error("E-mail inválido. Por favor, insira um e-mail válido.")

                email_button = email.button("Enviar Relatório por E-mail 📧")
                if email_button:
                    email_dialog()
                
                # Disponibilizar o PDF para download
                dowload = st.download_button(
                    label="Baixar Relatório em PDF",
                    data=pdf_buf,
                    file_name="relatorio_sentimentos_youtube.pdf",
                    mime="application/pdf"
                )
