import nltk
from nltk import trigrams
from collections import Counter
import wikipediaapi
import re
import math
from tkinter import simpledialog, messagebox

wiki_wiki = wikipediaapi.Wikipedia( language="en", user_agent="NLP Class Assignment - Khaled Abdulrahman, MUST University",)

def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

def fetch_wikipedia_content(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        return page.text
    else:
        return ""

def build_corpus(topics, min_words=200000):
    corpus = ""
    for topic in topics:
        content = fetch_wikipedia_content(topic)
        if content:
            corpus += clean_text(content)
        if len(corpus.split()) >= min_words:
            break
    return corpus

def generate_trigrams(corpus):
    tokens = corpus.split()
    trigram_list = list(trigrams(tokens))
    trigram_counts = Counter(trigram_list)
    return trigram_counts

def apply_laplace_smoothing(trigram_counts, vocab_size):
    smoothed_probs = {}
    total_count = sum(trigram_counts.values())
    for trigram, count in trigram_counts.items():
        smoothed_probs[trigram] = (count + 1) / (total_count + vocab_size)
    return smoothed_probs

def calculate_perplexity(smoothed_probs, corpus):
    tokens = corpus.split()
    trigram_list = list(trigrams(tokens))
    N = len(trigram_list)
    log_prob_sum = 0
    for trigram in trigram_list:
        if trigram in smoothed_probs:
            log_prob_sum += math.log(smoothed_probs[trigram])
        else:
            log_prob_sum += math.log(1 / len(smoothed_probs))
    perplexity = math.exp(-log_prob_sum / N)
    return perplexity

def autocomplete(smoothed_probs, prefix):
    prefix_words = prefix.split()
    suggestions = []

    if len(prefix_words) == 1:
        for trigram in smoothed_probs:
            if trigram[0] == prefix_words[0]:
                suggestions.append(trigram[2])
    elif len(prefix_words) >= 2:
        for trigram in smoothed_probs:
            if trigram[0] == prefix_words[-2] and trigram[1] == prefix_words[-1]:
                suggestions.append(trigram[2])

    return suggestions[:10]

def get_autocomplete_suggestions():
    input_text = simpledialog.askstring("Input", "Enter a prefix (1 or 2 words):")

    if not input_text:
        messagebox.showinfo("Error", "Please enter a prefix.")
        return get_autocomplete_suggestions()

    suggestions = autocomplete(smoothed_probs, input_text)

    if suggestions:
        messagebox.showinfo("Autocomplete Suggestions", ", ".join(suggestions))
    else:
        messagebox.showinfo("No Suggestions", "No autocomplete suggestions found.")

topics = ["Economics", "Politics", "Sports", "Finance", "International Relations"]
corpus = build_corpus(topics, min_words=200000)
trigram_counts = generate_trigrams(corpus)
vocab_size = len(set(corpus.split()))
smoothed_probs = apply_laplace_smoothing(trigram_counts, vocab_size)
perplexity = calculate_perplexity(smoothed_probs, corpus)
print(f"Perplexity of the test corpus: {perplexity}")
get_autocomplete_suggestions()