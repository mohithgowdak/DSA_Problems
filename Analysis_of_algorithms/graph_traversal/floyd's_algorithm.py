def Min(a, b):
    return a if a < b else b

def floyds(graph, n):
    count = 0
    for k in range(n):
        for i in range(n):
            temp = graph[i][k]
            for j in range(n):
                count += 1
                if graph[i][j] > temp:
                    graph[i][j] = Min(graph[i][j], temp + graph[k][j])
    return count

def main():
    global n
    n = int(input("Enter the Number of Vertices: "))
    graph = []

    print("Enter the Adjacency Matrix")
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    count = floyds(graph, n)

    print("The Shortest Path by Floyd's Algorithm is")
    for i in range(n):
        for j in range(n):
            print(f"{graph[i][j]}\t", end="")
        print()

    print(f"The Count is: {count}")

    with open("plot.txt", "a+") as fp:
        fp.write(f"{n}\t\t{count}\n")

if __name__ == "__main__":
    main()
