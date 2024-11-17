
# Comment Gauge - Análise de Sentimentos de Comentários do YouTube

## Descrição

Comment Gauge é uma ferramenta de análise de sentimentos focada em comentários de YouTube. Com ela, é possível extrair comentários, analisar o sentimento por meio de processamento de linguagem natural (NLP) e visualizar dados de forma eficaz. Essa ferramenta é destinada a criadores de conteúdo, pesquisadores e marcas que buscam insights sobre a opinião pública.

## Tecnologias Utilizadas

- **Streamlit** - Para visualização interativa de dados.
- **YouTube Data API v3** - Para coleta de dados.
- **Transformers (Hugging Face)** - Para análise de sentimentos.
- **Torch** - Framework de aprendizado de máquina.
- **Bibliotecas:** - `yagmail`, `matplotlib`, `pandas`, `nltk`, `scikit-learn`

## Funcionalidades

- **Extração de Comentários**: Permite a extração de comentários de vídeos do YouTube usando a API do YouTube.
- **Análise de Sentimentos**: Aplica um modelo de análise de sentimentos (usando a biblioteca Hugging Face Transformers).
- **Interface Interativa**: Interface desenvolvida em Streamlit para visualização dos dados e interação com o usuário.
- **Visualização de Dados**: Gera gráficos e relatórios para facilitar a compreensão das opiniões dos usuários.

## Estrutura do Projeto

```plaintext
AnDS-ANDS-Streamlit/
├── app/
│   ├── logo/
│   │     ├── Ands_logo.png                      # imagem ultilizada no projeto
│   │     └── image_sentiment_analisys.png       # imagem ultilizada no projeto
│   ├── midia/
│   │     └── streamlit_video_txt.mp4            # Video ultilizado no projeto
│   ├── enviar_email.py                          # Função para enviar email com o pdf
│   ├── gerar_pdf.py                             # Função para gerar o pdf a partir dos comentários
│   ├── sentiment_analysis.py                    # Funções para análise de sentimentos
│   ├── streamlit.py                             # Script principal para a interface Streamlit
│   └── YouTubeScraper.py                        # Módulo para extração de comentários do YouTube  
├── requirements.txt                             # Dependências do projeto
└── README.md                                    # Documentação do projeto
```

## Requisitos

- Python 3.8 ou superior
- Instalar dependências com:
  ```bash
  pip install -r requirements.txt
  ```

## Como Executar

1. **Interface com Streamlit**: Para iniciar a aplicação Streamlit:
   ```bash
   streamlit run app/streamlit.py
   ```

3. **Configuração**: Após que as dependências do  `requirements.tx`forem instaladas certifique-se de definir variáveis de ambiente (ex. `API_KEY`) no arquivo `.env` para acessar a API do YouTube.

## Instalação

Para usar o **Comment Gauge**, siga os passos abaixo:

### 1. Clonar o repositório

```bash
git clone https://github.com/NxtTon/AnDS.git
```
### 2. Configuração do YouTube API
Para acessar a API do YouTube, você precisa de uma chave de API. Siga os passos abaixo para obter uma chave:
- Acesse Google Cloud Console.
- Crie um projeto e habilite a **YouTube Data API v3**.
- Gere uma chave de API e adicione-a ao arquivo de configuração do projeto.

### 3. Configurar o env
- Substitua com suas credenciais.

**Template do arquivo .env**
```
#CHAVE DA API DO YOUTUBE
API_KEY=''

#Senha do email
SENHA_EMAIL=''

obs: A senha do email funciona melhor com uma senha de aplicativo que pode ser configurada na conta do google do usuario.

Caso esteja com dificuldades consulte este link: https://atendimento.tecnospeed.com.br/hc/pt-br/articles/4418115119127-Como-criar-senha-de-aplicativo-para-email
```

### 4. Rodar o projeto
Para rodar o projeto, use o seguinte comando:
```bash
python -m streamlit run app\streamlit.py
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

