High Level Design

System Overview:
RAG-based assistant using PDF ingestion, embeddings, retrieval and routing.

Architecture:
User -> FastAPI -> Retriever -> Decision Layer -> Response / HITL

Components:
PDF Loader, Chunking, Embedding Model, ChromaDB, Retriever, Routing, HITL

Data Flow:
PDF -> Chunks -> Embeddings -> Store -> Query -> Retrieve -> Respond

Scalability:
Handles multiple documents, scalable DB, async APIs
