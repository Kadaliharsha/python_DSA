def numberofprovinces(adj):
    
    n = len(adj)
    visited = [False] * n
    count = 0
    
    def dfs(i):
        for j in range(n):
            if adj[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if not visited[i]:
            count += 1
            visited[i] = True
            dfs(i)
    return count

if __name__ == "__main__":
    adjanceny = eval(input())
    print(numberofprovinces(adjanceny))