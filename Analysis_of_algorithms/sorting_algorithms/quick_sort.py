import random
import time

count = 0

def swap(a, b):
    a, b = b, a

def partition(a, l, r):
    p = a[l]
    i = l + 1
    j = r
    while i <= j:
        while i <= r:
            global count
            count += 1
            if a[i] < p:
                i += 1
            else:
                break
        while j >= l:
            count += 1
            if a[j] > p:
                j -= 1
            else:
                break
        if i <= j:
            swap(a[i], a[j])
            i += 1
            j -= 1
    swap(a[l], a[j])
    return j

def quick_sort(a, l, r):
    if l == r:
        return
    elif l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s - 1)
        quick_sort(a, s + 1, r)

def main():
    global count
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        random.seed(time.time())
        m = 10
        while m <= 1000:
            count = 0
            a = [10] * m
            quick_sort(a, 0, m - 1)
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            a = list(range(1, m + 1))
            quick_sort(a, 0, m - 1)
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
    quick_sort(a, 0, n - 1)
    print("\nThe Elements are: ", end="")
    for i in range(n):
        print(a[i], end="\t")
    print(f"\nThe Count is: {count}")
    '''

if __name__ == "__main__":
    main()
