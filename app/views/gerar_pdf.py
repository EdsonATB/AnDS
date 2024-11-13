from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

def gerar_pdf(df, video_url, sentiment_counts):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Título e URL do vídeo
    c.drawString(100, 750, "Relatório de Sentimentos dos Comentários do YouTube")
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
    c.drawString(350, y_position, "Sentimento")
    c.drawString(500, y_position, "Confiança")

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
        comment_lines = wrap_text(row['text'], 60)  # Ajuste o valor conforme necessário para caber na largura da página
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
        c.drawString(350, y_position + 10, sentiment)
        c.drawString(500, y_position + 10, confidence)
        y_position -= 15

    # Salvar e retornar o buffer do PDF
    c.save()
    buffer.seek(0)
    return buffer
