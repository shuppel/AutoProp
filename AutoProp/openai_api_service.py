import openai
import re

openai.api_key = "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"

def ask_question(question, context):
    model = "text-davinci-003"
    prompt = f"Answer the following question based on the given context:\n\nQuestion: {question}\n\nContext: {context}\n\nAnswer:"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer


