#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install spacy


# In[2]:


from spacy.cli import download


# In[3]:


import requests
from bs4 import BeautifulSoup
from collections import Counter
import numpy as np
import re
import json
import networkx as nx
import csv


# In[4]:


download("en_core_web_sm")


# In[10]:


import requests
import json
import re
from bs4 import BeautifulSoup
from collections import defaultdict, Counter
import spacy

nlp = spacy.load("en_core_web_sm")

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    return ""
    
def preprocess_text(text):
    text = re.sub(r'\d+', '', text) 
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().split(".") 

# Pobieranie 20 artykułów z Wikipedii na podstawie zapytania
language_code = 'en'
search_query = 'the'  # Wyszukujemy artykuły z najbardziej ogólnym zapytaniem
number_of_results = 20
headers = {
    'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'  # Ustaw odpowiednie nagłówki
}

base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
url = base_url + language_code + endpoint

parameters = {'q': search_query, 'limit': number_of_results}

response = requests.get(url, headers=headers, params=parameters)

response = json.loads(response.text)

urls = []
for page in response['pages']:
    article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
    urls.append(article_url)

sentences = []
for url in urls:
    text = get_page_content(url)
    if text:  
        words = preprocess_text(text)
        sentences.extend(words)




# In[11]:


import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

transitive_verbs = most_common_verbs

verb_noun_dict = defaultdict(set)

for sentence in sentences:
    doc = nlp(sentence)
    for token in doc:
        if token.lemma_ in transitive_verbs and token.pos_ == "VERB":
            for child in token.children:
                if child.dep_ == "dobj" and child.pos_ == "NOUN":
                    verb_noun_dict[token.lemma_].add(child.lemma_)

for verb, nouns in verb_noun_dict.items():
    print(f"Czasownik: {verb} -> Rzeczowniki: {nouns}")
    print("____________________________________________________")
    
print("____________________________________________________")
print("Przykłady działań na zbiorach")
sum_have_include = verb_noun_dict["have"].union(verb_noun_dict["include"])
print(f"Suma have + include: {sum_have_include}")
print("____________________________________________________")
intersection_make_use = verb_noun_dict["make"].intersection(verb_noun_dict["use"])
print(f"Iloczyn make ∩ use: {intersection_make_use}")
print("____________________________________________________")
difference_follow_have = verb_noun_dict["follow"].difference(verb_noun_dict["have"])
print(f"Różnica follow - have: {difference_follow_have}")
print("____________________________________________________")
sum_eat_drink = verb_noun_dict["eat"].union(verb_noun_dict["drink"])
print(f"Suma eat + drink: {sum_eat_drink}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




