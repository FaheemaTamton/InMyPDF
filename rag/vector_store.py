import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_store(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return {"index": index, "chunks": chunks}

def query_store(store, query):
    q_emb = model.encode([query])
    _, I = store["index"].search(q_emb, 3)
    return "\n".join(store["chunks"][i] for i in I[0])
