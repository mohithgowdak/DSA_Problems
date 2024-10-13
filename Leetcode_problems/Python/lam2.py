def main():
    # Read the size and elements of the first list
    n = int(input())
    A = list(map(int, input().split()))
    
    # Read the size and elements of the second list
    m = int(input())
    x = list(map(int, input().split()))
    
    # Sort the second list
    x.sort()
    
    # Find common elements using binary search
    ans = []
    for element in A:
        if binary_search(x, element):
            ans.append(element)
    
    # Print the result
    for it in ans:
        print(it, end=" ")
    print()

def binary_search(arr, target):
    """Helper function to perform binary search on a sorted list."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    main()
