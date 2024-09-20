def minEditDist(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        dp[0][i] = i

    for i in range(m):
        dp[i][0] = i

    for i in range(1, m):
        for j in range(1, n):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 2  # You can adjust this cost as needed
            
            dp[i][j] = min(
                dp[i-1][j] + 1,   # Deletion
                dp[i][j-1] + 1,   # Insertion
                dp[i-1][j-1] + cost  # Substitution
            )

    return dp[m-1][n-1]

# Sample dictionary of correct words
dictionary = ["apple", "banana", "grape", "orange", "mango", "strawberry", "pineapple"]

# Function to find the closest word from the dictionary using minEditDist
def spell_checker(word, dictionary):
    min_distance = float('inf')
    closest_word = ""

    for correct_word in dictionary:
        dist = minEditDist(word, correct_word)
        if dist < min_distance:
            min_distance = dist
            closest_word = correct_word

    return closest_word, min_distance

# Test with a misspelled word
misspelled_word = "aple"  # Misspelled version of "apple"
closest_word, distance = spell_checker(misspelled_word, dictionary)

print(f"The closest word to '{misspelled_word}' is '{closest_word}' with an edit distance of {distance}.")
