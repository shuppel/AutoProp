import openai

def analyze_text(text):
    openai.api_key = "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"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n\n{text}\n",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    return summary
