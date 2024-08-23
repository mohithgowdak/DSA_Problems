def quicksort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choosing the middle element as pivot
    pivot_index = 0 # use the desired index
    pivot = arr[pivot_index]
    
    # Dividing the array into three parts:
    # 1. Elements less than the pivot
    # 2. Elements equal to the pivot
    # 3. Elements greater than the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    # Recursively applying quicksort to the less and greater parts
    return quicksort(less) + equal + quicksort(greater)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)
