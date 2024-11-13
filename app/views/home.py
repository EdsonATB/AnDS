import streamlit as st
from PIL import Image


# Título e subtítulo com emojis
st.title("🎉 Comment Gauge 🎉")
st.write("### Análise de Sentimentos de Comentários no YouTube")

st.write("""
**Bem-vindo ao _Comment Gauge_** 🎬, a solução completa para obter insights sobre a opinião pública em vídeos do YouTube!
""")

# Banner ou imagem ilustrativa (se tiver uma)
# image = Image.open(r"C:\Users\gabri\OneDrive\Documentos\GitHub\AnDS\app\logo\ANDS_logo.jpg")  # Substitua com o caminho da sua imagem
# st.image(image, use_column_width=True)

# Seções de Introdução e Funcionalidades
st.header("💡 O que é o Comment Gauge?")
st.write("""
**Comment Gauge** é uma ferramenta de análise de sentimentos projetada para **criadores de conteúdo, pesquisadores e marcas** que desejam entender as opiniões dos espectadores. Com ele, você pode:
""")
st.markdown("""
- **📥 Extrair comentários** de vídeos do YouTube com facilidade.
- **📈 Analisar o sentimento** dos comentários (positivo, negativo, neutro) usando técnicas avançadas de NLP.
- **📊 Visualizar a distribuição** dos sentimentos com gráficos e relatórios detalhados.
- **📤 Exportar o relatório** em PDF e enviar por e-mail para fácil compartilhamento.
""")

st.header("⚙️ Como Funciona?")
st.write("""
Para começar, basta escolher uma das opções abaixo para buscar o vídeo desejado:
""")
st.markdown("""
- 🔍 **Pesquisar por Nome**: Insira um termo para buscar o vídeo.
- 🆔 **Pesquisar por ID**: Insira diretamente o ID do vídeo para realizar a análise.
""")

# Botão para Navegar até a Análise de Sentimentos
st.write("🚀 Pronto para começar? Clique em **📊 Analisador de Sentimentos** para iniciar sua análise!")  # Adicione o redirecionamento para a página de análise, se necessário

# Link para a página Sobre Nós
st.write("---")
st.write("👥 Quer saber mais sobre a gente? Dê uma passadinha na página **📋 Sobre Nós**.")
