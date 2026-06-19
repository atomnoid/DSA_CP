# 4. Palindrome Checker
# This script checks if a string is a palindrome.
# It handles case insensitivity and ignores non-alphanumeric characters.

def is_palindrome_simple(s):
    """
    Checks for palindrome using string slicing.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    # Clean the string: convert to lowercase and keep only alphanumeric chars
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def is_palindrome_two_pointers(s):
    """
    Checks for palindrome using the Two-Pointer technique without extra string memory.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer forward if not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer backward if not alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare character (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

def main():
    print("--- Palindrome Checker ---")
    user_str = input("Enter a string (or press Enter for default 'A man, a plan, a canal: Panama'): ")
    if user_str.strip() == "":
        user_str = "A man, a plan, a canal: Panama"
        
    print(f"Testing string: \"{user_str}\"")
    
    # Method 1
    res_simple = is_palindrome_simple(user_str)
    print(f"Result (Simple slicing method): {res_simple}")
    
    # Method 2
    res_two_ptr = is_palindrome_two_pointers(user_str)
    print(f"Result (Two Pointers method)  : {res_two_ptr}")

if __name__ == "__main__":
    main()
