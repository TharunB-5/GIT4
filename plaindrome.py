def is_palindrome(s):
    # Convert to string and compare with its reverse
    s = str(s)
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome(121))        # True
