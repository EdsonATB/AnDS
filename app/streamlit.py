import streamlit as st

st.set_page_config(page_title='Comment Gauge', page_icon='📊', layout='wide')

home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠",
)

analisador_page = st.Page(
    page="views/analisador.py",
    title="Analisador de Sentimentos",
    icon="📊",

)

pg = st.navigation(
    { 
        "Home": [home_page],
        "Analisador de Sentimentos": [analisador_page],
    }
)

st.sidebar.text('Desenvolvido por alunos de ti 🤓')



pg.run()

#python -m streamlit run app\streamlit.py use este comando para rodar o streamlit