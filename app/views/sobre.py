# streamlit_pages/about.py

import streamlit as st

def sobre():
    st.title("Sobre o Projeto Comment Gauge")
    st.markdown("""
    ## Bem-vindo ao Comment Gauge!
    
    O Comment Gauge é uma ferramenta de análise de sentimentos focada em comentários do YouTube. Nosso objetivo é ajudar a identificar
    o sentimento geral do público em torno de tópicos específicos, fornecendo insights úteis para criadores de conteúdo, pesquisadores, e marcas.

    ### Funcionalidades
    - **Extração de Comentários**: Coleta de comentários do YouTube com base em palavras-chave ou URLs de vídeos.
    - **Análise de Sentimentos**: Utiliza técnicas de NLP para categorizar os comentários em sentimentos como positivo, negativo ou neutro.
    - **Visualização de Dados**: Exibe os resultados da análise de forma clara e interativa.

    ### Equipe
    Este projeto foi desenvolvido por uma equipe apaixonada por tecnologia e dados, que acredita no poder da análise de sentimentos
    para fornecer insights sobre opiniões e tendências.

    ### Contato
    Para mais informações, entre em contato conosco:
    - Email: contato@commentgauge.com
    - GitHub: [github.com/commentgauge](https://github.com/commentgauge)

    Esperamos que esta ferramenta seja útil para você!
    """)
sobre()