import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("faq_collection")
import json

with open("dataset/final_dataset.json") as f:
    faqs = json.load(f)

for faq in faqs:
    collection.add(
        documents=[faq["answer"]],
        metadatas=[{"question": faq["question"]}],
        ids=[faq["question"]]
    )

print(f" {len(faqs)} FAQs Embedded into ChromaDB")
