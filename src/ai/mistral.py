from llama_cpp import Llama

model = Llama(
    model_path="./models/mistral-7b-instruct-v0.2.Q4_0.gguf",
    n_ctx=4096,
    n_threads=8,
)


def improve_transcription(transcription: str) -> str:
    """
    Migliora la trascrizione di un testo utilizzando il modello Mistral.

    Args:
        transcription (str): La trascrizione da migliorare.

    Returns:
        str: La trascrizione migliorata.
    """
    messages = [
        {
            "role": "system",
            "content": """Scrivi sempre e solo in italiano. Sei un assistente che corregge trascrizioni audio di video di cucina. Il tuo compito è sistemare gli errori di riconoscimento vocale, mantenendo sempre il significato originale.

    ## Regole:
    - Correggi parole sbagliate o fuse (es. "olivetta giasche" → "olive taggiasche")
    - Aggiungi punteggiatura se manca, ma senza esagerare
    - Non cambiare lo stile, resta semplice e parlato
    - Non aggiungere nulla che non sia già presente
    - Mantieni l’ordine e la struttura della trascrizione originale
    - Mantieni il testo in italiano
    - Non usare formattazioni speciali come grassetto o corsivo
    - Non aggiungere titoli o sezioni, rispondi solo con il testo corretto
    - Non usare emoji o simboli speciali
    - Non usare markdown o altri formati, rispondi solo con il testo corretto
    - Non usare abbreviazioni, scrivi sempre le parole per esteso


    Restituisci solo il testo corretto, senza commenti o spiegazioni.""",
        },
        {
            "role": "user",
            "content": transcription,
        },
    ]

    response = model.create_chat_completion(messages, temperature=0.1)
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]
