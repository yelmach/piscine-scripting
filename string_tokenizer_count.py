import re
from collections import Counter

def tokenizer_counter(sentence):
    words = re.findall(r'[a-z0-9]+', sentence.lower())
    
    counts = Counter(words)
    
    sorted_items = sorted(counts.items())
    
    return dict(sorted_items)