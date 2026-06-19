# 2. Binary Search
# This script demonstrates Binary Search (both Iterative and Recursive).
# Note: Binary search requires the input array to be sorted first.

def binary_search_iterative(arr, target):
    """
    Performs binary search iteratively.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    # Element was not present in the array
    return -1

def binary_search_recursive(arr, target, low, high):
    """
    Performs binary search recursively.
    Time Complexity: O(log N)
    Space Complexity: O(log N) (due to call stack recursion limit)
    """
    # Base case
    if low > high:
        return -1
        
    mid = (low + high) // 2
    
    # If element is found at mid
    if arr[mid] == target:
        return mid
    # If element is smaller than mid, it can only be in left subarray
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    # Else the element can only be in right subarray
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

def main():
    print("--- Binary Search ---")
    print("Note: The array must be sorted.")
    
    # Setup test data
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Sorted Array: {arr}")
    
    try:
        target = int(input("Enter target number to search for: "))
    except ValueError:
        print("Invalid input, using default target 23")
        target = 23
        
    # Iterative approach
    iter_result = binary_search_iterative(arr, target)
    if iter_result != -1:
        print(f"Iterative: Element {target} found at index {iter_result}")
    else:
        print(f"Iterative: Element {target} not found in the array")
        
    # Recursive approach
    recur_result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if recur_result != -1:
        print(f"Recursive: Element {target} found at index {recur_result}")
    else:
        print(f"Recursive: Element {target} not found in the array")

if __name__ == "__main__":
    main()
