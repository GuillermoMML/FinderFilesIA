import unicodedata
import json
from nltk.corpus import wordnet as wn

def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

def expand_query_with_wordnet(query):
    synonyms = set()
    terms = normalizar(query).split()
    for word in terms:
        for syn in wn.synsets(word, lang="spa"):
            for lemma in syn.lemmas(lang="spa"):
                name = lemma.name().replace('_', ' ')
                synonyms.add(name.lower())
    return set(terms).union(synonyms)

def load_keywords(path="metadata/keywords.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}
