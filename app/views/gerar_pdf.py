from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

def gerar_pdf(df, video_url, sentiment_counts):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Configuração da página
    page_width, page_height = letter  # Dimensões da página

    # Título em negrito e centralizado
    title = "Relatório de Sentimentos dos Comentários do YouTube"
    c.setFont("Helvetica-Bold", 16)  # Fonte em negrito e tamanho maior para o título

    # Calcula a posição x para centralizar o título
    title_width = c.stringWidth(title, "Helvetica-Bold", 16)
    title_x = (page_width - title_width) / 2
    c.drawString(title_x, 750, title)  # Centralizado horizontalmente na posição vertical 750

    # Fonte para o restante do documento
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, f"Vídeo Analisado: {video_url}")

    # Contagem de sentimentos
    c.drawString(100, 710, "Análise de Sentimentos:")
    y_position = 690
    for sentiment, count in sentiment_counts.items():
        c.drawString(100, y_position, f"{sentiment}: {count}")
        y_position -= 15

    # Tabela de Sentimentos - Cabeçalhos
    c.drawString(100, y_position - 20, "Tabela de Sentimentos:")
    y_position -= 40
    c.setFont("Helvetica-Bold", 10)
    c.drawString(100, y_position, "Comentário")
    c.drawString(350, y_position, "Sentimento")  # Espaçamento maior para a coluna "Sentimento"
    c.drawString(500, y_position, "Confiança")   # Espaçamento maior para a coluna "Confiança"

    # Ajuste de espaçamento e fonte para o conteúdo da tabela
    y_position -= 20
    c.setFont("Helvetica", 8)

    # Função para quebrar o texto em linhas
    def wrap_text(text, max_width):
        wrapped_lines = wrap(text, max_width)
        return wrapped_lines

    # Exibição dos comentários com quebra de linha e alinhamento de colunas
    for index, row in df.iterrows():
        if y_position < 40:  # Salta para nova página se necessário
            c.showPage()
            c.setFont("Helvetica", 8)
            y_position = 750  # Reinicia a posição vertical no topo da nova página

        # Quebrar o texto do comentário em linhas, se for muito longo
        comment_lines = wrap_text(row['text'], 40)  # Ajustado para maior espaçamento
        sentiment = row['sentiment']

        # Converte 'confidence' para float e formata, se possível; caso contrário, exibe como string
        try:
            confidence = f"{float(row['confidence']):.2f}"
        except ValueError:
            confidence = row['confidence']

        # Exibe cada linha do comentário
        for line in comment_lines:
            c.drawString(100, y_position, line)
            y_position -= 10

        # Exibe o sentimento e a confiança na mesma linha
        c.drawString(350, y_position + 10, sentiment)  # Maior espaçamento para a coluna "Sentimento"
        c.drawString(500, y_position + 10, confidence) # Maior espaçamento para a coluna "Confiança"
        y_position -= 15

    # Salvar e retornar o buffer do PDF
    c.save()
    buffer.seek(0)
    return buffer

# import openai
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from textwrap import wrap


# def resumo_sentimentos_ai(comments):
#     openai.api_key = ""

#     # Cria uma string com os comentários
#     comments_text = "\n".join([comment['comment'] for comment in comments])  # Acessando a chave 'comment' correta

#     # Criação do prompt com os comentários
#     prompt = "me de um relatorio geral disto aqui, citando pontos importantes e com base neles de um resumo do que eles dizem sobre o video, e me de a media de cada sentimento positivo, negativo e neutro." + "\n" + comments_text

#     # Enviando o prompt para o OpenAI GPT
#     response = openai.ChatCompletion.create(  # Corrigido aqui
#         model="gpt-3.5-turbo",  # ou outro modelo que você estiver usando
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=200,
#         temperature=0.7
#     )
    
#     # Retorna o resumo gerado pela IA
#     resumo = response['choices'][0]['message']['content'].strip()
#     return resumo


# def gerar_pdf(df, video_url, sentiment_counts, comentarios):
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer, pagesize=letter)
    
#     # Configuração da página
#     page_width, page_height = letter  # Dimensões da página

#     # Título em negrito e centralizado
#     title = "Relatório de Sentimentos dos Comentários do YouTube"
#     c.setFont("Helvetica-Bold", 16)  # Fonte em negrito e tamanho maior para o título

#     # Calcula a posição x para centralizar o título
#     title_width = c.stringWidth(title, "Helvetica-Bold", 16)
#     title_x = (page_width - title_width) / 2
#     c.drawString(title_x, 750, title)  # Centralizado horizontalmente na posição vertical 750

#     # Fonte para o restante do documento
#     c.setFont("Helvetica", 12)
#     c.drawString(100, 730, f"Vídeo Analisado: {video_url}")

#     # Contagem de sentimentos
#     c.drawString(100, 710, "Análise de Sentimentos:")
#     y_position = 690
#     for sentiment, count in sentiment_counts.items():
#         c.drawString(100, y_position, f"{sentiment}: {count}")
#         y_position -= 15

#     # Resumo da análise gerado pela IA
#     c.drawString(100, y_position - 20, "Resumo da Análise de Sentimentos:")
#     y_position -= 40
#     c.setFont("Helvetica", 10)
    
#     # Adiciona o resumo de comentários
#     comentarios_lines = wrap(comentarios, 80)  # Ajuste conforme necessário
#     for line in comentarios_lines:
#         c.drawString(100, y_position, line)
#         y_position -= 12

#     # Tabela de Sentimentos - Cabeçalhos
#     c.drawString(100, y_position - 20, "Tabela de Sentimentos:")
#     y_position -= 40
#     c.setFont("Helvetica-Bold", 10)
#     c.drawString(100, y_position, "Comentário")
#     c.drawString(350, y_position, "Sentimento")
#     c.drawString(500, y_position, "Confiança")

#     # Ajuste de espaçamento e fonte para o conteúdo da tabela
#     y_position -= 20
#     c.setFont("Helvetica", 8)

#     # Função para quebrar o texto em linhas
#     def wrap_text(text, max_width):
#         wrapped_lines = wrap(text, max_width)
#         return wrapped_lines

#     # Exibição dos comentários com quebra de linha e alinhamento de colunas
#     for index, row in df.iterrows():
#         if y_position < 40:  # Salta para nova página se necessário
#             c.showPage()
#             c.setFont("Helvetica", 8)
#             y_position = 750  # Reinicia a posição vertical no topo da nova página

#         # Quebrar o texto do comentário em linhas, se for muito longo
#         comment_lines = wrap_text(row['text'], 40)  # Ajustado para maior espaçamento
#         sentiment = row['sentiment']

#         # Converte 'confidence' para float e formata, se possível; caso contrário, exibe como string
#         try:
#             confidence = f"{float(row['confidence']):.2f}"
#         except ValueError:
#             confidence = row['confidence']

#         # Exibe cada linha do comentário
#         for line in comment_lines:
#             c.drawString(100, y_position, line)
#             y_position -= 10

#         # Exibe o sentimento e a confiança na mesma linha
#         c.drawString(350, y_position + 10, sentiment)
#         c.drawString(500, y_position + 10, confidence)
#         y_position -= 15

#     # Salvar e retornar o buffer do PDF
#     c.save()
#     buffer.seek(0)
#     return buffer



