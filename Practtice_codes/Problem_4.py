import nltk
from nltk import word_tokenize
from nltk.tag import hmm

#Sample text
text = "The cat sat on the mat."

#Tokenize the words 
word_tokens = word_tokenize(text)

#Train a hidden markov model using viterbi algorithm
train_data = nltk.corpus.brown.tagged_sents(categories = "news")

#Make a trainer to train the model
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

#Tag the words from the text
tagged_sentence = hmm_tagger.tag(word_tokens)
print(f"Tagged sentence : {tagged_sentence}")