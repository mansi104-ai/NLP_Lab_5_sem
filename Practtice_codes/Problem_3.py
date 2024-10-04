from collections import defaultdict, deque

def find_morph(words):
    #Step 1 :  Create a graph and calculate the in-degree (number of incoming steps)
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    #Initialize the in-degree for all characters
    for word in words:
        for char in word:
            in_degree[char] = 0

    #Step 2 : Build the graph by comparing the adjacent words
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        #Find the first differing character and create a directed edge

        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                #If the characters are different , add an edge word1[j]-> word2[j]
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]]+= 1
                break
            else:
                #Handle the edge case : if word2 is a prefix of word1,it's an invalid dictionary
                if len(word2) < len(word1):
                    return "Invalid dictionary order"
                

    #Step 3 : Perform topological sort using kahn's algorithm
    #Queue of all characters with in-degree 0 (no incoming edges)
    queue = deque([char for char in in_degree if in_degree[char] == 0])

    topo_order= []

    while queue :
        current = queue.popleft()
        topo_order.append(current)

        #Reduce the in_degree of neighbors and add to queue if it becomes 0
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

        # If topological sort is possible, the number of characters in topo_order should match the in-degree map
    if len(topo_order) == len(in_degree):
        return "".join(topo_order)
    else:
        return "Invalid dictionary order"


