import random
import time

count = 0

def swap(a, b, i, j):
    a[i], a[j] = a[j], a[i]

def selection_sort(a):
    global count
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            count += 1
            if a[j] < a[min_index]:
                min_index = j
        swap(a, a, i, min_index)

def main():
    global count
    with open("plot.txt", "w") as fp:
        random.seed(time.time())
        m = 10
        while m <= 1000:
            count = 0
            a = list(range(1, m + 1))
            selection_sort(a)
            fp.write(f"{m}\t\t{count}\n")
            
            if m < 100:
                m += 10
            else:
                m += 100

    # Correctness check
    # Uncomment the lines below to test the program interactively
    '''
    n = int(input("Enter the Number of Elements: "))
    a = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    selection_sort(a)
    print("The Elements are: ", end="")
    for i in range(n):
        print(a[i], end="\t")
    print(f"\nThe Count is: {count}")
    '''

if __name__ == "__main__":
    main()
