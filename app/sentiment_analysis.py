from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

def analyze_sentiments(texts):
    # Certifique-se de que 'texts' não é None e é uma lista
    if not texts or not isinstance(texts, list):
        return []

    # Filtra comentários vazios
    texts = [text for text in texts if text.strip()]

    # Define o modelo e o tokenizer
    model_name = 'cardiffnlp/twitter-roberta-base-sentiment'
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Define a função de mapeamento de labels
    label_mapping = {
        'LABEL_0': 'Negative',
        'LABEL_1': 'Neutral',
        'LABEL_2': 'Positive'
    }

    # Cria o pipeline de análise de sentimentos
    sentiment_analyzer = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    # Realiza a análise de sentimentos
    results = sentiment_analyzer(texts)

    # Função para formatar a pontuação
    def format_score(score):
        return f"{round(score * 100)}%"

    # Prepara os resultados
    analysis_results = []
    for text, result in zip(texts, results):
        sentiment_label = label_mapping.get(result['label'], 'Unknown')
        score_percentage = format_score(result['score'])
        analysis_results.append({
            'text': text,
            'sentiment': sentiment_label,
            'confidence': score_percentage
        })

    return analysis_results
