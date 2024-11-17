import streamlit as st

st.set_page_config(page_title='Comment Gauge', page_icon='📊', layout='wide')



sobre_page = st.Page(
    page="views/sobre.py",
    title="Sobre Nós",
    icon="📋",

)

analisador_page = st.Page(
    page="views/analisador.py",
    title="Analisador de Sentimentos",
    icon="📊",

)

pg = st.navigation(
    { 
        "Analisador de Sentimentos": [analisador_page],
        "Sobre Nós": [sobre_page],
    }
)

st.sidebar.text('Desenvolvido por alunos de ti 🤓')

pg.run()

#python -m streamlit run app\streamlit.py use este comando para rodar o streamlit