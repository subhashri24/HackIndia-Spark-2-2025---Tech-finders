import requests
import json

API_URL = "https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&tagged=python&site=stackoverflow"

def fetch_stackoverflow():
    response = requests.get(API_URL)
    questions = response.json()["items"]
    faqs = []

    for q in questions[:20]:
        question = q["title"]
        faqs.append({"question": question, "answer": "Answer not available"})

    return faqs

faq_list = fetch_stackoverflow()

with open("dataset/stackoverflow_faq.json", "w") as file:
    json.dump(faq_list, file, indent=4)

print(f" {len(faq_list)} FAQs Collected from StackOverflow")
