import random
import time

count = 0

def insertion_sort(a):
    global count
    for i in range(1, len(a)):
        j = i - 1
        temp = a[i]
        while j >= 0:
            count += 1
            if a[j] > temp:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = temp

def main():
    global count
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        random.seed(time.time())
        m = 10
        while m <= 1000:
            count = 0
            a = list(range(1, m + 1))
            insertion_sort(a)
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            a = list(range(m, 0, -1))
            insertion_sort(a)
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
    insertion_sort(a)
    print("\nThe Elements are: ", end="")
    for i in range(n):
        print(a[i], end="\t")
    print(f"\nThe Count is: {count}")
    '''

if __name__ == "__main__":
    main()
