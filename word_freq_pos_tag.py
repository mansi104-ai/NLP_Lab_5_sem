import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.probability import FreqDist

# Sample text
text = "This is a sample text to tokenize."

# Tokenize the text
tokens = word_tokenize(text)

#Count word frequency
word_freq = FreqDist(tokens)
print(f"Word frequency : {word_freq}")

#Identify the POS tags
pos_tags = pos_tag(tokens)
print(f"POS tags :{pos_tags}")