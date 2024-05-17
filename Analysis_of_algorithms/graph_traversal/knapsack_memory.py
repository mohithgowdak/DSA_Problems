def Max(a, b):
    return a if a > b else b

def memoryfunction(v, wt, val, i, j):
    if v[i][j] < 0:
        if j < wt[i - 1]:  # Adjust for 0-based index in wt and val
            v[i][j] = memoryfunction(v, wt, val, i - 1, j)
        else:
            v[i][j] = Max(memoryfunction(v, wt, val, i - 1, j), val[i - 1] + memoryfunction(v, wt, val, i - 1, j - wt[i - 1]))
    return v[i][j]

def knapsack(n, capacity, wt, val):
    count = 0
    v = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            count += 1
            if i == 0 or j == 0:
                v[i][j] = 0
    result = memoryfunction(v, wt, val, n, capacity)
    return result, v, count

def main():
    with open("plot.txt", "a+") as fp:
        n = int(input("Enter the Number of Items: "))
        capacity = int(input("Enter the Sack Capacity: "))
        wt = []
        val = []
        print("Enter the Item Weight and their Price\nWeight\tPrice")
        for _ in range(n):
            weight, price = map(int, input().split())
            wt.append(weight)
            val.append(price)

        worth, v, count = knapsack(n, capacity, wt, val)
        print(f"The Worth of Sack is {worth}")

        for i in range(n + 1):
            for j in range(capacity + 1):
                print(f"{v[i][j]}\t", end="")
            print()

        print("Items included are:")
        w = capacity
        for i in range(n, 0, -1):
            if v[i][w] != v[i - 1][w]:
                print(f"Item {i}", end=' ')
                w -= wt[i - 1]
        print("\nThe Count is %d" % count)
        fp.write(f"{n}\t\t{count}\n")

if __name__ == "__main__":
    main()
