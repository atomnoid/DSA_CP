# 1. Reverse an Array / List
# This script demonstrates different methods to reverse an array in Python.

def reverse_slicing(arr):
    """
    Reverses an array using Python's slicing technique.
    Time Complexity: O(N)
    Space Complexity: O(N) (creates a new list)
    """
    return arr[::-1]

def reverse_two_pointers(arr):
    """
    Reverses an array in-place using the two-pointer approach.
    Time Complexity: O(N)
    Space Complexity: O(1) (modifies original list in-place)
    """
    left = 0
    right = len(arr) - 1
    
    # Create a copy so we do not mutate the input if we want to compare
    arr_copy = arr.copy()
    
    while left < right:
        # Swap elements at left and right indices
        arr_copy[left], arr_copy[right] = arr_copy[right], arr_copy[left]
        left += 1
        right -= 1
        
    return arr_copy

def main():
    print("--- Reversing an Array ---")
    # Take user input or use a default list
    input_str = input("Enter numbers separated by spaces (or press Enter for default [1, 2, 3, 4, 5]): ")
    if input_str.strip() == "":
        arr = [1, 2, 3, 4, 5]
    else:
        arr = [int(x) for x in input_str.split()]
        
    print(f"Original Array: {arr}")
    
    # Method 1: Slicing
    sliced = reverse_slicing(arr)
    print(f"Reversed (Slicing): {sliced}")
    
    # Method 2: Two Pointers (In-place swap)
    two_ptr = reverse_two_pointers(arr)
    print(f"Reversed (Two Pointers): {two_ptr}")

if __name__ == "__main__":
    main()
