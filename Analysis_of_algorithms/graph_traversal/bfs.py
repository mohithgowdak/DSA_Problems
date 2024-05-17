def bfs(graph, n, start, d):
    global count, bfscall, isCyclic
    queue = []
    parent = [-1] * n
    visited[start] = 1
    queue.append(start)
    count += 1

    while queue:
        start = queue.pop(0)
        path[start] = 1
        parentnode = parent[start]
        print(chr(start + 65), end="---->")

        for i in range(n):
            if d == 1:
                if i != parentnode and visited[i] and graph[start][i] and path[i]:
                    isCyclic = 1
            else:
                if i != parentnode and visited[i] and graph[start][i]:
                    isCyclic = 1

            if visited[i] == 0 and graph[start][i]:
                queue.append(i)
                parent[i] = start
                visited[i] = 1
                count += 1

        path[start] = 0

def main():
    global count, bfscall, isCyclic, path, visited
    count = 0
    bfscall = 0

    n = int(input("Enter the Number of Vertices: "))
    d = int(input("Enter 1 if Graph is Directed Else 0: "))
    print("Enter the Adjacency Matrix")
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    visited = [0] * n
    path = [0] * n
    isCyclic = 0

    bfs(graph, n, 0, d)
    bfscall += 1

    if isCyclic:
        print("\nGraph is Cyclic")
    else:
        print("\nGraph is Acyclic")

    if count == n:
        print("Graph is Connected")
    else:
        print("Graph is NOT Connected")
        start = 1
        while count != n:
            if visited[start] == 0:
                print("\n")
                bfs(graph, n, start, d)
                bfscall += 1
            start += 1

    print(f"Number Of Connected Components is {bfscall}")

if __name__ == "__main__":
    main()
