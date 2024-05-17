def compute_indegree(graph, n):
    indegree = [0] * n
    visited = [0] * n
    queue = []
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[j][i] == 1:
                indegree[i] += 1

    for i in range(n):
        if indegree[i] == 0:
            count += 1
            queue.append(i)
            visited[i] = 1

    return indegree, visited, queue, count

def topological_sort(graph, n):
    indegree, visited, queue, count = compute_indegree(graph, n)
    temp = []
    cnt = 0

    while count != 0:
        source = queue.pop(0)
        count -= 1
        temp.append(source)
        cnt += 1

        for i in range(n):
            if graph[source][i] == 1:
                indegree[i] -= 1
            if indegree[i] == 0 and not visited[i]:
                count += 1
                queue.append(i)
                visited[i] = 1

    if cnt != n:
        print("Cycle Exists")
    else:
        print("\nThe Topological sorting is:")
        for node in temp:
            print(f"{node + 1}---->\t", end="")

def main():
    global n, graph
    n = int(input("Enter the Number of Vertices: "))
    graph = []

    print("Enter the Adjacency Matrix")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    topological_sort(graph, n)

if __name__ == "__main__":
    main()
