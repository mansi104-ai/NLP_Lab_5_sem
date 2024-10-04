def min_edit_distance(word1,word2):

    #Get the length of both words
    m = len(word1)
    n= len(word2)

    #Create a matrix to store the edit distance
    dp = [[0]*(n+1) for _ in range(m+1)]

    #Initialize the matrix with the base cases
    #If one word is empty,we need to insert all characters of the other word
    for i in range(m+1):
        dp[i][0] = i #Deletion steps

    for j in range(n+1):
        dp[0][j] = j #Insertion steps

    #Fill the dp matrix using recursice relation
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] #No operations needed if the characters match

            else:
                dp[i][j] = min(
                    dp[i-1][j],  #Deletion
                    dp[i][j-1], #Insertion
                    dp[i-1][j-1] #Substitution
                )+1

    #The final result is the minimum edit distance
    return dp[m][n]


word1 =  "intention"
word2 =  "execution"
result = min_edit_distance(word1,word2)

print(f"The minimum edit distnace between the 2 words is :{result}")