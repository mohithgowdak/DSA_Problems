import math

x = 10
y = 100

def euclid(m, n):
    count = 0
    while n:
        count += 1
        temp = m % n
        m = n
        n = temp
    return count

def consec(m, n):
    count = 0
    min_val = min(m, n)
    while True:
        count += 1
        if m % min_val == 0:
            count += 1
            if n % min_val == 0:
                break
            min_val -= 1
        else:
            min_val -= 1
    return count

def modified(m, n):
    count = 0
    while n > 0:
        if n > m:
            m, n = n, m
        m = m - n
        count += 1
    return count

def analysis(ch):
    if ch == 1:
        best_file = "e_b.txt"
        worst_file = "e_w.txt"
    elif ch == 2:
        best_file = "c_b.txt"
        worst_file = "c_w.txt"
    elif ch == 3:
        best_file = "m_b.txt"
        worst_file = "m_w.txt"

    with open(best_file, "w") as fp2, open(worst_file, "w") as fp1:
        for i in range(x, y + 1, 10):
            maxcount = 0
            mincount = float('inf')
            for j in range(2, i + 1):
                for k in range(2, i + 1):
                    count = 0
                    m = j
                    n = k

                    if ch == 1:
                        count = euclid(m, n)
                    elif ch == 2:
                        count = consec(m, n)
                    elif ch == 3:
                        count = modified(m, n)

                    if count > maxcount:
                        maxcount = count
                    if count < mincount:
                        mincount = count

            fp2.write(f"{i} {mincount:.2f}\n")
            fp1.write(f"{i} {maxcount:.2f}\n")

def main():
    for ch in range(1, 4):
        analysis(ch)

if __name__ == "__main__":
    main()
