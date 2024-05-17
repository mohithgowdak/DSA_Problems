import random
import time

count = 0

def binary_search(a, low, high, key):
    global count
    if low > high:
        return -1
    mid = (low + high) // 2
    count += 1
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)

def main():
    global count
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        random.seed(time.time())
        m_values = []
        m = 100
        while m <= 30000:
            m_values.append(m)
            if m < 10000:
                m *= 10
            else:
                m += 10000
        
        for m in m_values:
            count = 0
            a = list(range(1, m + 1))
            pos = binary_search(a, 0, m - 1, a[(m - 1) // 2])
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            pos = binary_search(a, 0, m - 1, -1)
            fp2.write(f"{m}\t\t{count}\n")
    
    # Correctness check
    # Uncomment the lines below to test the program interactively
    '''
    n = int(input("Enter the Number of Elements: "))
    a = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    key = int(input("Enter the Element to Search: "))
    pos = binary_search(a, 0, n - 1, key)
    if pos == -1:
        print("Key Not Found")
    else:
        print(f"Key Found at: {pos + 1}")
    print(f"\nThe Count is {count}")
    '''

if __name__ == "__main__":
    main()
