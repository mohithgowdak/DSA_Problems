import sys

class Edge:
    def __init__(self, u, v, dist):
        self.u = u
        self.v = v
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
    min_edge = heap[0]
    heap[0] = heap[heapsize - 1]
    heap.pop()
    return min_edge

def prim():
    visited[0] = True
    heap.append(Edge(-1, 0, 0))
    while cnt != n:
        min_edge = deleteheap(heap)
        VT.append(min_edge)
        cnt += 1
        v = min_edge.u
        removed[v] = True
        for i in range(1, n):
            if not visited[i] and cost[v][i] != sys.maxsize and not removed[i]:
                visited[i] = True
                heap.append(Edge(v, i, cost[v][i]))
            if visited[i] and cost[v][i] != sys.maxsize and not removed[i]:
                for edge in heap:
                    if edge.u == i and cost[v][i] < edge.dist:
                        edge.dist = cost[v][i]
                        edge.v = v
                        break
        heapSort(heap)

n = int(input("Enter the total number of vertices: "))
cost = []
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 0:
            row[j] = sys.maxsize
    cost.append(row)

cnt = 0
visited = [False] * n
removed = [False] * n
heapsize = 0
heap = []
VT = []

prim()

sum = 0
for i in range(1, cnt):
    print(f"{chr(VT[i].v + 65)} --> {chr(VT[i].u + 65)} == {VT[i].dist}")
    sum += VT[i].dist

print("Minimum Distance is:", sum)
