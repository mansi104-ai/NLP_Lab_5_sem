def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    # Create a DP table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, insert all characters of second string
            if i == 0:
                dp[i][j] = j    

            elif j == 0:
                dp[i][j] = i    

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Remove
                                   dp[i][j - 1],    # Insert
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


def plagiarism_check(text1, text2, threshold=30):
    # Tokenize the input texts for better comparison (optional)
    words1 = text1.split()
    words2 = text2.split()
    
    # Calculate the minimum edit distance between the two texts
    distance = min_edit_distance(words1, words2)
    
    print(f"Minimum Edit Distance: {distance}")
    
    # Check if the edit distance is below the plagiarism threshold
    if distance <= threshold:
        print(f"The text might be plagiarized! (Threshold: {threshold})")
    else:
        print("The text is unlikely to be plagiarized.")
        

text1 = "The process of photosynthesis converts light energy into chemical energy."
text2 = "Photosynthesis is the method by which plants transform light energy into chemical energy."

threshold = 15

plagiarism_check(text1, text2, threshold)

