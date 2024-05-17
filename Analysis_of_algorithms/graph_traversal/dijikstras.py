import sys

class Vertex:
    def __init__(self, _id, dist):
        self.id = _id
        self.dist = dist

def heapify(arr, n, i):
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left].dist < arr[largest].dist:
            largest = left
        if right < n and arr[right].dist < arr[largest].dist:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def deleteheap(heap):
    min_vertex = heap[0]
    heap[0] = heap[heapsize - 1]
    heap.pop()
    return min_vertex

def dijkstra():
    for i in range(n):
        heap[i].dist = sys.maxsize
    heap[src].dist = 0
    global heapsize
    heapsize = n
    heapSort(heap)
    while count < n:
        min_vertex = deleteheap(heap)
        u = min_vertex.id
        removed[u] = 1
        count += 1
        for i in range(n):
            if not removed[i] and cost[u][i] != sys.maxsize:
                if d[u] + cost[u][i] < d[i]:
                    d[i] = d[u] + cost[u][i]
                    for vertex in heap:
                        if vertex.id == i:
                            vertex.dist = d[i]
                            break
        heapSort(heap)

n = int(input("Enter the Number of Vertices: "))
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0:
            row[j] = sys.maxsize
    cost.append(row)

src = int(input("Enter the Source Vertex: "))
heap = [Vertex(i, sys.maxsize) for i in range(n)]
removed = [0] * n
d = [sys.maxsize] * n
d[src] = 0
count = 0
heapsize = 0

dijkstra()

print("Shortest Paths Starting from", src, "are:")
for i in range(n):
    if src != i:
        print(src, "---", i, "=", d[i])
