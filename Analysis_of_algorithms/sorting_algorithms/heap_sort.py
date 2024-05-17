count = 0
count1 = 0

def heap_sort(H, n):
    global count
    for i in range(n // 2, 0, -1):
        pi = i
        pv = H[i]
        Heap = False
        while not Heap and 2 * pi <= n:
            ci = 2 * pi
            count += 1  # for leaf comparisons
            if ci < n:
                if H[ci + 1] > H[ci]:
                    ci += 1
            count += 1  # for leaf and its respective parent comparison
            if pv > H[ci]:
                Heap = True
            else:
                H[pi] = H[ci]
                pi = ci
        H[pi] = pv

def heapify(H, n, i):
    global count1
    while True:
        largest = i
        left = 2 * i
        right = 2 * i + 1
        if left <= n:
            count1 += 1
            if H[left] > H[largest]:
                largest = left
        if right <= n:
            count1 += 1
            if H[right] > H[largest]:
                largest = right
        if largest != i:
            H[i], H[largest] = H[largest], H[i]
            i = largest
        else:
            break

def delete(H, n):
    if n == 0:
        print("Heap is empty.")
        return
    H[1] = H[n]
    n -= 1
    heapify(H, n, 1)

def display(H, n):
    for i in range(1, n + 1):
        print(H[i], end="\t")
    print()

def main():
    global count, count1
    '''
    Uncomment below lines to perform file writing and analysis
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        for m in range(100, 10001, 1000 if m < 1000 else 100):
            count = 0
            count1 = 0
            a = list(range(m, 0, -1))  # Best Case: Decreasing Order
            heap_sort(a, m)
            n = m
            for i in range(m, 0, -1):
                delete(a, n)
                n -= 1
            fp1.write(f"{m}\t\t{count + count1}\n")
            
            count = 0
            count1 = 0
            a = list(range(1, m + 1))  # Worst Case: Increasing Order
            heap_sort(a, m)
            n = m
            for i in range(m, 0, -1):
                delete(a, n)
                n -= 1
            fp2.write(f"{m}\t\t{count + count1}\n")
    '''
    # CORRECTNESS
    n = int(input("Enter the Number of Elements: "))
    a = [0] + [int(input(f"Enter element {i}: ")) for i in range(1, n + 1)]
    heap_sort(a, n)
    print("After Heap Sort:")
    display(a, n)
    print("Deleting elements in decreasing order:")
    for i in range(n, 0, -1):
        delete(a, i)
        display(a, i)

if __name__ == "__main__":
    main()
