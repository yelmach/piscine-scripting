import re

def tokenize(sentence):
    lower_sentence = sentence.lower()
    tokens = re.findall(r'[a-z0-9]+', lower_sentence)
    
    return tokens
