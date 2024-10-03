import nltk
from nltk.tokenize import word_tokenize


#Sample Text
text = "This is a sample text to tokenize"

#Tokenize the text
tokens = word_tokenize(text)

#Count the number of tokens
token_count = len(tokens)
print(f"Number of tokens : {token_count}")