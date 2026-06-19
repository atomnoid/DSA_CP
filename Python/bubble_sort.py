# 3. Bubble Sort
# This script demonstrates the Bubble Sort algorithm with an optimization.

def bubble_sort(arr):
    """
    Sorts an array in ascending order using Bubble Sort.
    Includes an optimization to stop early if the array is already sorted.
    Time Complexity: O(N^2) in worst/average case, O(N) in best case (already sorted)
    Space Complexity: O(1)
    """
    n = len(arr)
    arr_copy = arr.copy() # copy to avoid modifying in-place for comparison
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
            
    return arr_copy

def main():
    print("--- Bubble Sort ---")
    input_str = input("Enter unsorted numbers separated by spaces (or press Enter for default [64, 34, 25, 12, 22, 11, 90]): ")
    if input_str.strip() == "":
        arr = [64, 34, 25, 12, 22, 11, 90]
    else:
        arr = [int(x) for x in input_str.split()]
        
    print(f"Original Array: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"Sorted Array  : {sorted_arr}")

if __name__ == "__main__":
    main()
