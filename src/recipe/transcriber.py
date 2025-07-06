from llama_cpp import Llama
import os

model = Llama(
    model_path="./models/mistral-7b-instruct-v0.2.Q4_0.gguf",
    n_ctx=4096,
    n_threads=8,
)

messages = [
    {
        "role": "system",
        "content": """Sei un assistente specializzato nella scrittura di ricette di cucina. Scrivi sempre in **italiano**. Il tuo compito è trasformare una trascrizione in una **ricetta completa e ben formattata** in **Markdown**.

## Regole da seguire:
- Scrivi solo in **italiano**
- Correggi errori evidenti nel testo (es. "aqua" → "acqua", "olivetta giasche" → "olive taggiasche")
- Se un ingrediente o quantità è incompleto, **stima con buon senso**
- Non aggiungere nulla che non sia nella trascrizione o descrizione
- Scrivi in modo chiaro, semplice e preciso (anche per chi cucina poco)
- Usa sempre **"minuti"**, **"grammi"**, **"ml"**, **"°C"** (niente abbreviazioni)
- Segui sempre e solo lo **schema Markdown** qui sotto
- **Non usare altri formati**

## Schema obbligatorio:

```markdown
# [NOME RICETTA]

## 📝 Descrizione
[Breve descrizione del piatto - 2-3 frasi]

## 👥 Porzioni
[Numero di porzioni]

## ⏱️ Tempi
- **Preparazione:** [X minuti]
- **Cottura:** [X minuti]  
- **Totale:** [X minuti]

## 🥘 Ingredienti
- [quantità precisa] [ingrediente]
- [quantità precisa] [ingrediente]

## 🔧 Strumenti necessari
- [strumento 1]
- [strumento 2]

## 📋 Procedimento

### Fase 1: Preparazione
1. **[Azione specifica]** - [dettagli]

### Fase 2: Cottura
1. **[Azione specifica]** - [Temperatura: X°C, Tempo: X minuti]

### Fase 3: Finalizzazione
1. **[Azione specifica]** - [come servire o completare]

## 💡 Consigli
- [Consiglio utile]
- [Variante o sostituzione]

## 🏷️ Tag
`[categoria]` `[difficoltà]` `[tipo-cottura]` `[tempo-preparazione]`
""",
    }
]


def transcribe_recipe(
    transcription: str, description: str, output_path="files/recipes"
) -> str:
    """
    Transcribes a recipe text using Llama model.

    Args:
        transcription (str): The transcription text to be processed.
        output_path (str): Path where the transcription will be saved.

    Returns:
        str: Path to the saved transcription file.
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    messages.append(
        {
            "role": "user",
            "content": f"""Questa è la descrizione del video:

            {description}

            ---

            E questa è la trascrizione dell'audio del video:

            {transcription}

            ---

            Genera la ricetta completa in italiano, seguendo **esattamente** lo schema Markdown indicato nelle istruzioni di sistema. Non aggiungere nulla che non sia nella trascrizione o nella descrizione. Se mancano quantità o dettagli, stima in modo realistico. Non aggiungere altro che il codice markdown alla risposta, senza commenti o spiegazioni.""",
        }
    )

    response = model.create_chat_completion(
        messages=messages,
        temperature=0.3,
    )

    print(response["choices"][0]["message"]["content"])

    return response["choices"][0]["message"]["content"]
