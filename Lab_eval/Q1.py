#implement the viterbi algorithm in the given sentence
#import the required libraries
import nltk
from nltk import word_tokenize

# Lexicon, transition, and emission probabilities
lexicon = { 
    'The': ['DET'], 'cat': ['NOUN'], 'sat': ['VERB'], 'on': ['PREP'], 
    'the': ['DET'], 'mat': ['NOUN'] 
}

transition_probs = {
    'START': {'DET': 0.9, 'NOUN': 0.1},
    'DET': {'NOUN': 0.8, 'VERB': 0.1, 'PREP': 0.1},
    'NOUN': {'VERB': 0.7, 'PREP': 0.3},
    'VERB': {'DET': 0.4, 'PREP': 0.6},
    'PREP': {'DET': 0.9, 'NOUN': 0.1}
}

emission_probs = {
    'DET': {'The': 0.6, 'the': 0.4},
    'NOUN': {'cat': 0.5, 'mat': 0.5},
    'VERB': {'sat': 1.0},
    'PREP': {'on': 1.0}
}

# Viterbi Algorithm for POS tagging
def viterbi(sentence, lexicon, transition_probs, emission_probs):
    words = sentence.split()
    n = len(words)
    
    # Initialize Viterbi and backpointer tables
    viterbi = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]
    
    # Initialize start state
    for tag in lexicon[words[0]]:
        viterbi[0][tag] = transition_probs['START'].get(tag, 0) * emission_probs[tag].get(words[0], 0)
        backpointer[0][tag] = None
    
    # Recursive case
    for t in range(1, n):
        for tag in lexicon[words[t]]:
            max_prob, best_prev_tag = max(
                (viterbi[t-1][prev_tag] * transition_probs[prev_tag].get(tag, 0) * emission_probs[tag].get(words[t], 0), prev_tag) 
                for prev_tag in viterbi[t-1]
            )
            viterbi[t][tag] = max_prob
            backpointer[t][tag] = best_prev_tag
    
    # Termination step
    max_prob, best_final_tag = max((viterbi[n-1][tag], tag) for tag in viterbi[n-1])

    # Backtracking to retrieve the best tag sequence
    best_sequence = [best_final_tag]
    for t in range(n-1, 0, -1):
        best_sequence.insert(0, backpointer[t][best_sequence[0]])
    
    return best_sequence

# Test sentence
sentence = "The cat sat on the mat"

# Run Viterbi algorithm
best_tags = viterbi(sentence, lexicon, transition_probs, emission_probs)

# Output the results
print(f"Sentence: {sentence}")
print(f"Predicted POS tags: {best_tags}")

