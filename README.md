
# Comment Gauge - Análise de Sentimentos de Comentários do YouTube

## Descrição

Este projeto é uma aplicação para análise de sentimentos em comentários do YouTube, desenvolvida usando FastAPI e Streamlit. Ele extrai comentários de vídeos do YouTube e usa modelos de aprendizado de máquina para identificar o sentimento dos textos (positivo, neutro ou negativo). O projeto também oferece uma interface interativa com Streamlit para visualização dos resultados.

## Funcionalidades

- **Extração de Comentários**: Utiliza o Selenium para coletar comentários de vídeos do YouTube.
- **Análise de Sentimentos**: Aplica um modelo de análise de sentimentos (usando a biblioteca Hugging Face Transformers).
- **Interface Interativa**: Interface desenvolvida em Streamlit para visualização dos dados e interação com o usuário.
- **FastAPI**: Endpoint de API para execução de tarefas de extração e análise.

## Estrutura do Projeto

```plaintext
AnDS-ANDS-Streamlit/
├── app/
│   ├── YouTubeScraper.py         # Módulo para extração de comentários do YouTube
│   ├── sentiment_analysis.py     # Funções para análise de sentimentos
│   ├── streamlit.py              # Script principal para a interface Streamlit
│   ├── api.py                    # Configuração de rotas e FastAPI
│   └── routes.py                 # Rotas específicas para as funcionalidades da API
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do projeto
```

## Requisitos

- Python 3.8 ou superior
- Instalar dependências com:
  ```bash
  pip install -r requirements.txt
  ```

## Como Executar

1. **API com FastAPI**: Para iniciar o servidor FastAPI, execute:
   ```bash
   uvicorn app.api:app --reload
   ```

2. **Interface com Streamlit**: Para iniciar a aplicação Streamlit:
   ```bash
   streamlit run app/streamlit.py
   ```

3. **Configuração**: Certifique-se de definir variáveis de ambiente (ex. `API_KEY`) no arquivo `.env` para acessar a API do YouTube.

## Tecnologias Utilizadas

- **FastAPI** - Para criação de API.
- **Streamlit** - Para visualização interativa de dados.
- **Selenium** - Para automação e coleta de dados.
- **Transformers (Hugging Face)** - Para análise de sentimentos.
- **Torch** - Framework de aprendizado de máquina.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

