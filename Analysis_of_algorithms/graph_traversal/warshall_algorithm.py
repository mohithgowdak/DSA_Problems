def warshall(graph, n):
    global count
    for k in range(n):
        for i in range(n):
            if graph[i][k]:
                for j in range(n):
                    count += 1
                    if graph[k][j]:
                        graph[i][j] = 1

def main():
    global count, n
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        for n in range(2, 21):
            # Initialize graph for best case (sparse)
            graph = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n-1):
                graph[i][i+1] = 1
            graph[n-1][0] = 1

            count = 0
            warshall(graph, n)
            fp1.write(f"{n}\t\t{count}\n")

            # Initialize graph for worst case (dense)
            graph = [[1 if i != j else 0 for j in range(n)] for i in range(n)]

            count = 0
            warshall(graph, n)
            fp2.write(f"{n}\t\t{count}\n")

    # Uncomment the following block for correctness testing
    """
    n = int(input("Enter the Number of Vertices: "))
    graph = []
    print("Enter the Adjacency Matrix:")
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    count = 0
    warshall(graph, n)

    print("The Transitive Closure of the Matrix by Warshall's Algorithm is:")
    for row in graph:
        print("\t".join(map(str, row)))
    print(f"The Count is: {count}")
    """

if __name__ == "__main__":
    main()
