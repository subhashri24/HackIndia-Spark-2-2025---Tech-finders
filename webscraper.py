import requests
from bs4 import BeautifulSoup
import json
import time
from tqdm import tqdm

def scrape_url(url):
    faqs = []
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Customize this based on website structure
            questions = soup.select("h2, h3")  # Questions Tags
            answers = soup.select("p")        # Answers Tags
            
            for q, a in zip(questions, answers):
                question = q.text.strip()
                answer = a.text.strip()
                
                if question and answer:
                    faqs.append({
                        "question": question,
                        "answer": answer
                    })

    except Exception as e:
        print(f"python webscraper.py Error Scraping {url}: {e}")

    return faqs


def remove_duplicates(dataset):
    unique_faqs = []
    questions_set = set()

    for faq in dataset:
        if faq["question"] not in questions_set:
            questions_set.add(faq["question"])
            unique_faqs.append(faq)

    return unique_faqs


if __name__ == "__main__":
    all_faqs = []
    
    # Reading URL List
    with open("urls.txt", "r") as f:
        urls = f.read().splitlines()

    print(f" Total URLs Found: {len(urls)}")
    
    # Scraping Each URL
    for url in tqdm(urls, desc="Scraping URLs"):
        faqs = scrape_url(url)
        all_faqs.extend(faqs)
        time.sleep(2)  # Add delay to avoid blocking
    
    print(f" Total FAQs Collected: {len(all_faqs)}")

    # Removing Duplicates
    clean_faqs = remove_duplicates(all_faqs)
    print(f" Unique FAQs: {len(clean_faqs)}")

    # Save Dataset to JSON
    with open("faq_dataset.json", "w") as f:
        json.dump(clean_faqs, f, indent=4)

    print(" Dataset Successfully Created ")
