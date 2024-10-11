#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import re
import json
import networkx as nx
import csv


# In[2]:


# Funkcja do pobrania i przetworzenia treści z URL (pojedyncze)
def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    return ""


# In[3]:


# Funkcja do przetwarzania tekstu: usuwanie liczb i znaków specjalnych
def preprocess_text(text):
    text = re.sub(r'\d+', '', text)  # Usunięcie liczb
    text = re.sub(r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]', ' ', text)  # Usunięcie znaków specjalnych
    return text.lower().split()


# In[4]:


# Pobranie 100 artykułów w wybranym języku przy uzyciu The Wikimedia API
language_code = 'pl'
search_query = 'the'  
number_of_results = 100
headers = {
    'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)' 
}

base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
url = base_url + language_code + endpoint

parameters = {'q': search_query, 'limit': number_of_results}

response = requests.get(url, headers=headers, params=parameters)

response = json.loads(response.text)

urls=[]
for page in response['pages']:
    article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
    urls.append(article_url)

print(urls)


# In[5]:


#POJEDYNCZY ARTYKUL


# In[6]:


# URL artykułu
url = urls[0]

# Pobranie tekstu
text = get_page_content(url)

if text:  # Jeśli tekst został pobrany
    words = preprocess_text(text)

# Zliczenie częstotliwości wyrazów
word_count = Counter(words)

# Sortowanie słów według częstotliwości
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Rangi i częstotliwości do prawa Zipfa
ranks = np.arange(1, len(sorted_words) + 1)
freq = np.array([count for _, count in sorted_words])
zipf = np.array([ranks[i] / freq[i] for i in range(len(sorted_words))])

# Zapisanie do csv 
csv_data = [['Rank', 'Word', 'Frequency', 'Zipf']] + [[r, word, f, z] for r, (word, f), z in zip(ranks, sorted_words, zipf)]
file_path_zipf = 'zipf_data.csv'

with open(file_path_zipf, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Wykres log-log (prawo Zipfa)
plt.figure(figsize=(8, 6))
plt.loglog(ranks, freq, marker="o")
plt.title("Prawo Zipfa - zależność rangi a częstotliwości")
plt.xlabel("Ranga")
plt.ylabel("Częstotliwość")
plt.grid(True)
plt.savefig("zipf_plot.png")
plt.show()

# Tworzenie grafu współwystępowania słów
G = nx.Graph()
G.add_nodes_from(words)

# Dodanie krawędzi między słowami występującymi obok siebie
for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    G.add_edge(word1, word2)

# Wyodrębnienie 10% wierzchołków o największej liczbie sąsiadów
num_nodes_to_extract = int(0.1 * len(G.nodes())) 
sorted_nodes_by_degree = sorted(G.degree, key=lambda x: x[1], reverse=True)

top_nodes = [node for node, degree in sorted_nodes_by_degree[:num_nodes_to_extract]]

# Wyświetlenie wybranych węzłów
H = G.subgraph(top_nodes)

# Wizualizacja grafu
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(H, k=0.5)
nx.draw(H, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Graf 10% węzłów z największą liczbą sąsiadów")
plt.savefig("graph_top_10_percent.png")
plt.show()


# In[7]:


#100 artykułów


# In[8]:


all_words = []  # Lista na słowa ze wszystkich artykułów

# Przetwarzanie każdego artykułu
for url in urls:
    text = get_page_content(url)
    if text:  # Jeśli tekst został pobrany
        words = preprocess_text(text)
        all_words.extend(words)  # Dodajemy słowa do ogólnej listy

# Zliczenie częstotliwości słów dla wszystkich artykułów
word_count = Counter(all_words)

# Sortowanie słów według częstotliwości
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Prawo Zipfa - przygotowanie danych
ranks = np.arange(1, len(sorted_words) + 1)
freq = np.array([count for _, count in sorted_words])

# Zapisanie do csv 
csv_data = [['Rank', 'Word', 'Frequency', 'Zipf']] + [[r, word, f, z] for r, (word, f), z in zip(ranks, sorted_words, zipf)]
file_path_zipf = 'all_zipf_data.csv'

with open(file_path_zipf, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Wykres log-log (prawo Zipfa)
plt.figure(figsize=(8, 6))
plt.loglog(ranks, freq, marker="o")
plt.title("Prawo Zipfa - zależność rangi a częstotliwości")
plt.xlabel("Ranga")
plt.ylabel("Częstotliwość")
plt.grid(True)
plt.savefig("all_zipf_plot.png")
plt.show()

# Tworzenie grafu współwystępowania słów
G = nx.Graph()
G.add_nodes_from(words)

# Dodanie krawędzi między słowami występującymi obok siebie
for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    G.add_edge(word1, word2)

# Wyodrębnienie 10% wierzchołków o największej liczbie sąsiadów
num_nodes_to_extract = int(0.1 * len(G.nodes())) 
sorted_nodes_by_degree = sorted(G.degree, key=lambda x: x[1], reverse=True)

top_nodes = [node for node, degree in sorted_nodes_by_degree[:num_nodes_to_extract]]

# Wyświetlenie wybranych węzłów
H = G.subgraph(top_nodes)

# Wizualizacja grafu
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(H, k=0.5)
nx.draw(H, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Graf 10% węzłów z największą liczbą sąsiadów")
plt.savefig("all_graph_top_10_percent.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:





# In[ ]:




