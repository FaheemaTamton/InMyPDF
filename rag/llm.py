import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(context, question):
    if not os.getenv("OPENAI_API_KEY"):
        return "❌ OpenAI API key not set."

    prompt = f"""
Answer ONLY using the context below.
If the answer is not present, say "Answer not found in the document."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fast + cheap + perfect for RAG
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content
