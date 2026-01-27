import re

def tokenize(sentence):
    lower_sentence = sentence.lower()
    tokens = re.findall(r'\w+', lower_sentence)
    
    return tokens
