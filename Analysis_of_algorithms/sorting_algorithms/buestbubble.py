def count_swaps(arr, ascending=True):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swap_count += 1
    return swap_count

def minimum_swaps_to_make_beautiful(arr):
    # Count swaps for both ascending and descending
    ascending_swaps = count_swaps(arr[:], ascending=True)  # Copy of array for ascending
    descending_swaps = count_swaps(arr[:], ascending=False)  # Copy of array for descending
    
    # Return the minimum swaps required
    return min(ascending_swaps, descending_swaps)

# Input reading
N = int(input())  # Reading number of elements
arr = list(map(int, input().split()))  # Reading the array of elements

# Output the result
print(minimum_swaps_to_make_beautiful(arr))
