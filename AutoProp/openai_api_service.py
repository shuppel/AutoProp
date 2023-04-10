import openai
import re

openai.api_key = "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"

def ask_question(question, context):
    model = "text-davinci-002"
    prompt = f"{question}\n\n{context}"
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

def process_section(text):
    # This is a simple implementation of section processing using regex
    # You can improve this function to better match your document structure
    sections = re.split(r'\n\n+', text)
    section_dict = {}
    for i, section in enumerate(sections):
        section_dict[f"{i+1}"] = section
    return section_dict
