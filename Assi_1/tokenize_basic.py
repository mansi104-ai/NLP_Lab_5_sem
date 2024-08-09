import re

# Function to tokenize text
def tokenize(text):
    # Splitting based on non-word characters and ignoring empty strings
    tokens = re.split(r'\W+', text)
    tokens = [token.lower() for token in tokens if token]  # Convert to lowercase and remove empty strings
    return tokens

# Function to count word frequency
def word_frequency(tokens):
    frequency = {}
    for token in tokens:
        if token in frequency:
            frequency[token] += 1
        else:
            frequency[token] = 1
    return frequency

# Function to identify POS tags (Basic approach)
def identify_pos(tokens):
    pos_tags = {}
    for token in tokens:
        if re.match(r'^[A-Z]', token):
            pos_tags[token] = 'Proper Noun'
        elif re.match(r'(.*)ing$', token):
            pos_tags[token] = 'Verb (Present Participle)'
        elif re.match(r'(.*)ed$', token):
            pos_tags[token] = 'Verb (Past Tense)'
        elif re.match(r'(.*)ly$', token):
            pos_tags[token] = 'Adverb'
        elif re.match(r'(.*)ous$', token):
            pos_tags[token] = 'Adjective'
        elif re.match(r'(.*)s$', token) and len(token) > 1:
            pos_tags[token] = 'Noun (Plural)'
        else:
            pos_tags[token] = 'Noun/Verb/Other'
    return pos_tags

# Main function
def main():
    # Sample input text
    text = """
    The quick brown fox jumps over the lazy dog. The fox was very quick and it jumped over another lazy dog.
    """

    # Tokenize the text
    tokens = tokenize(text)
    
    # 1) Count the number of tokens
    token_count = len(tokens)
    print(f'Number of tokens: {token_count}')

    # 2) Word Analysis: Frequency of words
    frequency = word_frequency(tokens)
    print(f'\nWord Frequency:')
    for word, count in frequency.items():
        print(f'{word}: {count}')

    # Word Analysis: POS tagging
    pos_tags = identify_pos(tokens)
    print(f'\nPOS Tags:')
    for word, pos in pos_tags.items():
        print(f'{word}: {pos}')

# Run the main function
if __name__ == "__main__":
    main()
