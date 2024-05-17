def dfs(graph, visited, path, stack, start, parent):
    global flag
    visited[start] = True
    path[start] = True

    for i in range(len(graph)):
        if i != parent and visited[i] and path[i] and graph[start][i]:
            flag = True
            return
        if not visited[i] and graph[start][i]:
            dfs(graph, visited, path, stack, i, start)
    
    path[start] = False
    stack.append(start)

def main():
    global flag
    n = int(input("Enter the Number of Vertices: "))
    graph = []

    print("Enter the Adjacency Matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    visited = [False] * n
    path = [False] * n
    stack = []
    flag = False

    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, path, stack, i, -1)

    if flag:
        print("Cycle Exists No Solution")
    else:
        print("\nTopological Order:")
        while stack:
            print(chr(stack.pop() + 65), end="---->\t")

if __name__ == "__main__":
    main()
