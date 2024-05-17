import random
import time

count = 0

def merge(b, c, a, n):
    global count
    i = j = k = 0
    p = n // 2
    q = n - p
    while i < p and j < q:
        count += 1
        if b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    while i < p:
        a[k] = b[i]
        i += 1
        k += 1
    while j < q:
        a[k] = c[j]
        j += 1
        k += 1

def merge_sort(a, n):
    if n == 1:
        return
    p = n // 2
    b = a[:p]
    c = a[p:]
    merge_sort(b, len(b))
    merge_sort(c, len(c))
    merge(b, c, a, n)

def worst(arr, beg, end):
    if beg < end:
        mid = (beg + end) // 2
        n1 = mid - beg + 1
        n2 = end - mid
        a = [arr[2 * i] for i in range(n1)]
        b = [arr[2 * j + 1] for j in range(n2)]
        worst(a, beg, mid)
        worst(b, mid + 1, end)
        for i in range(n1):
            arr[i] = a[i]
        for j in range(n2):
            arr[j + n1] = b[j]

def main():
    global count
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        random.seed(time.time())
        m = 10
        while m <= 1000:
            count = 0
            a = list(range(1, m + 1))
            merge_sort(a, m)
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            a = list(range(1, m + 1))
            worst(a, 0, m - 1)
            merge_sort(a, m)
            fp2.write(f"{m}\t\t{count}\n")
            
            if m < 100:
                m += 10
            else:
                m += 100

    # Correctness check
    # Uncomment the lines below to test the program interactively
    '''
    n = int(input("Enter the Number of Elements: "))
    a = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    print("\nThe Elements are: ", end="")
    for i in range(n):
        print(a[i], end="\t")
    merge_sort(a, n)
    print("\nThe Elements are: ", end="")
    for i in range(n):
        print(a[i], end="\t")
    print(f"\nThe Count is: {count}")
    '''

if __name__ == "__main__":
    main()
