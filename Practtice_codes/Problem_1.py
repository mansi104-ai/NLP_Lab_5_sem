import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag

#Sample text
Text=  "NLP is a fascinating field that involves a human language."

#Tokenize the word
tokens = word_tokenize(Text)

#Count the number of tokens
token_size = len(tokens)
print(f"The number of the tokens in the sentence is :{token_size}")

## Finding the frequency distribution of each word
word_freq = FreqDist(tokens)
print(f"Word Frequency:{word_freq}")

##Find the pos tagging 
pos_tagging = pos_tag(tokens)
print(f"Pos tags : {pos_tagging}")