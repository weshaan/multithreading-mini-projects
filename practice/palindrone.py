def is_palindrome(number):
    # Convert number to string
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    if number_str == number_str[::-1]:
        return True
    else:
        return False

# Example usage
number = 121
if is_palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
