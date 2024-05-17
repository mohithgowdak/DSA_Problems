import random
import time

count = 0

def linear_search(a, key):
    global count
    for i in range(len(a)):
        count += 1
        if a[i] == key:
            return i
    return -1

def main():
    global count
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        random.seed(time.time())
        m = 10
        while m <= 1000:
            count = 0
            a = list(range(1, m + 1))
            pos = linear_search(a, 1)
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            pos = linear_search(a, -1)
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
    key = int(input("Enter the Element to Search: "))
    pos = linear_search(a, key)
    if pos == -1:
        print("Key Not Found")
    else:
        print(f"Key Found at: {pos+1}")
    '''

if __name__ == "__main__":
    main()
