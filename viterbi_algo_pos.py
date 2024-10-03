## for this problem we need to use the Viterbi algorithm 
## to find the most probable POS tag sequence . Here is the implementation 
## using the nltk library

import nltk
from nltk import word_tokenize
from nltk.tag import hmm

#Training a Hidden Markov Model POS tagger using viterbi
train_data = nltk.corpus.brown.tagged_sents(categories = "news")

#Train an HMM-based POS tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

#Sample Sentence
sentence = "This is a sample sentence for tagging."
tokens = word_tokenize(sentence)

#POS tagging using the viterbi algorithm
tagged_sentence = hmm_tagger.tag(tokens)
print(f"Tagged Sentence: {tagged_sentence}")