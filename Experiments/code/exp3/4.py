def recoverSecret(triplets):
    graph = {}
    for triplet in triplets:
        for letter in triplet:
            if letter not in graph:
                graph[letter] = set()
    
    for triplet in triplets:
        graph[triplet[0]].add(triplet[1])
        graph[triplet[1]].add(triplet[2])
    
    visited = set()
    result = []
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            result.append(node)
    
    for node in graph:
        dfs(node)
    
    return ''.join(reversed(result))

data = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recoverSecret(data))