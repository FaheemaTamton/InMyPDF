

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fast + cheap + perfect for RAG
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content
