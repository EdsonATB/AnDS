import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


load_dotenv() 
senha_email = os.getenv('SENHA_EMAIL')

def enviar_email(email, pdf_buffer):
    # destinatario = 'commentgauge@gmail.com'
    destinatario = email
    assunto = 'Relatório de Sentimentos dos Comentários do YouTube'
    mensagem = 'Segue em anexo o relatório de sentimentos dos comentários do YouTube'

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = 'commentgauge@gmail.com'
    senha = senha_email

    
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain'))
    
    try:
        anexar_pdf = MIMEApplication(pdf_buffer.read(), _subtype="pdf")
        anexar_pdf.add_header('content-disposition', 'attachment', filename='relatorio.pdf')
        msg.attach(anexar_pdf)
   
    except Exception as e:
            print(e)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, senha)
        
        server.sendmail(remetente, destinatario, msg.as_string())
    finally:
        server.quit()
