
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
import chromadb

app = FastAPI()

loader = PyPDFLoader("knowledge_base.pdf")
documents = loader.load()

texts = [doc.page_content for doc in documents]

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.create_collection("kb")

embeddings = model.encode(texts).tolist()

for i, t in enumerate(texts):
    collection.add(documents=[t], embeddings=[embeddings[i]], ids=[str(i)])

class Query(BaseModel):
    question: str

def retrieve(q):
    emb = model.encode([q]).tolist()
    res = collection.query(query_embeddings=emb, n_results=1)
    return res['documents'][0][0]

def route(query, context):
    if "complaint" in query.lower() or "not working" in query.lower():
        return "HITL"
    return "AUTO"

def hitl(query):
    return f"Escalated to human agent: {query}"

@app.post("/ask")
def ask(q: Query):
    context = retrieve(q.question)
    decision = route(q.question, context)

    if decision == "HITL":
        return {"answer": hitl(q.question)}

    return {"answer": f"Based on docs: {context}"}
