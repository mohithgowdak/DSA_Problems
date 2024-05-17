def dfs(n, start, parent, graph, visited, path, d):
    global is_cyclic, count, graphcount
    visited[start] = True
    path[start] = True
    count += 1
    print(chr(start + 65), end="---->")
    
    for i in range(n):
        if d == 1:
            if i != parent and visited[i] and graph[start][i] and path[i]:
                is_cyclic = True
        else:
            if i != parent and visited[i] and graph[start][i]:
                is_cyclic = True
        graphcount += 1
        if not visited[i] and graph[start][i]:
            dfs(n, i, start, graph, visited, path, d)
    
    path[start] = False

def main():
    global is_cyclic, count, dfscall, graphcount

    # WHILE RUNNING FOR PLOTTING COMMENT OUT THE PRINTF INSIDE THE DFS FUNCTION
    """ 
    with open("plot.txt", "w") as fp:
        for m in range(2, 16):
            graphcount = 0
            graph = [[1 if i != j else 0 for j in range(m)] for i in range(m)]
            visited = [False] * m
            path = [False] * m
            dfs(m, 0, -1, graph, visited, path, 0)
            fp.write(f"{m}\t\t{graphcount}\n")
    """
    
    n = int(input("Enter the Number of vertices: "))
    d = int(input("Enter 1 if the Graph is Directed else 0: "))
    
    print("Enter the Adjacency Matrix")
    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    visited = [False] * n
    path = [False] * n
    
    is_cyclic = False
    count = 0
    dfscall = 0
    graphcount = 0
    
    dfs(n, 0, -1, graph, visited, path, d)
    dfscall += 1
    
    if is_cyclic:
        print("\nGraph is Cyclic")
    else:
        print("\nGraph is Acyclic")
    
    if count == n:
        print("Graph is Connected")
    else:
        print("Graph is NOT Connected")
        start = 1
        while count != n:
            if not visited[start]:
                print()
                dfs(n, start, -1, graph, visited, path, d)
                dfscall += 1
            start += 1
    
    print(f"\nNumber of Connected Components is: {dfscall}")

if __name__ == "__main__":
    main()
