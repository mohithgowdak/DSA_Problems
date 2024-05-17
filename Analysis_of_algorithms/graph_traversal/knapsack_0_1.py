
def Max(a, b):
    return a if a > b else b

def knapsack(n, capacity, wt, val):
    count = 0
    v = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            count += 1
            if i == 0 or j == 0:
                v[i][j] = 0
            elif j < wt[i-1]:
                v[i][j] = v[i-1][j]
            else:
                v[i][j] = Max(v[i-1][j], val[i-1] + v[i-1][j - wt[i-1]])

    print(f"The Worth of Sack is {v[n][capacity]}")
    w = capacity
    print("Items included are:")
    for i in range(n, 0, -1):
        if v[i][w] != v[i-1][w]:
            print(f"Item {i}", end=' ')
            w -= wt[i-1]
    print("\n")
    
    return count

def main():
    with open("plot.txt", "a+") as fp:
        # Correctness
        n = int(input("Enter the Number of Items: "))
        capacity = int(input("Enter the Sack Capacity: "))
        wt = []
        val = []
        print("Enter the Item Weight and their Price\nWeight\tPrice")
        for _ in range(n):
            weight, price = map(int, input().split())
            wt.append(weight)
            val.append(price)

        count = knapsack(n, capacity, wt, val)
        print(f"\nThe Count is {count}")
        fp.write(f"{n}\t\t{count}\n")

if __name__ == "__main__":
    main()
