def string_matching(t, p, n, m):
    global count, flag
    for i in range(n - m + 1):
        j = 0
        while j < m and p[j] == t[i + j]:
            count += 1
            j += 1
        if j == m:
            flag = 1
            return

def main():
    global count, flag
    with open("best.txt", "w") as fp1, open("worst.txt", "w") as fp2:
        t = ['a'] * 10000
        for m in range(10, 10001, 10 if m < 1000 else 1000):
            count = 0
            p = ['a'] * m
            string_matching(t, p, 10000, m)
            fp1.write(f"{m}\t\t{count}\n")
            
            count = 0
            p = ['a'] * (m - 1) + ['b']
            string_matching(t, p, 10000, m)
            fp2.write(f"{m}\t\t{count}\n")

    # Correctness check
    # Uncomment the lines below to test the program interactively
    '''
    text = input("Enter the Text: ")
    pattern = input("Enter the Pattern: ")
    string_matching(text, pattern, len(text), len(pattern))
    if flag:
        print("Pattern Found")
    else:
        print("Not matched")
    '''

if __name__ == "__main__":
    count = 0
    flag = 0
    main()
