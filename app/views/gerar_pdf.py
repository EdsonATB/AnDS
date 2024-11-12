from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gerar_pdf(df, video_url, sentiment_counts):

                    buffer = BytesIO()
                    c = canvas.Canvas(buffer, pagesize=letter)
                    c.setFont("Helvetica", 12)


                    c.drawString(100, 750, "Relatório de Sentimentos dos Comentários do YouTube")

                    
                    c.drawString(100, 730, f"Vídeo Analisado: {video_url}")

                    
                    c.drawString(100, 710, "Análise de Sentimentos:")
                    y_position = 690
                    for sentiment, count in sentiment_counts.items():
                        c.drawString(100, y_position, f"{sentiment}: {count}")
                        y_position -= 15

                    
                    c.drawString(100, y_position - 20, "Tabela de Sentimentos:")
                    y_position -= 40
                    c.drawString(100, y_position, "Comentário | Sentimento | Confiança")

                    y_position -= 20
                    for index, row in df.iterrows():
                        c.drawString(100, y_position, f"{row['text']} | {row['sentiment']} | {row['confidence']}")
                        y_position -= 15
                    c.save()
                    buffer.seek(0)

                    return buffer