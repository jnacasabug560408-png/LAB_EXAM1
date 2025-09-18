def isPalindrome(valStr):
    # Check if the string is the same forwards and backwards
    return valStr == valStr[::-1]

def toBinaryIfNumber(value):
    # Convert to binary only if the input is numeric
    if value.isdigit():
        return bin(int(value))[2:]  # Remove '0b' prefix
    return None

# Main program
user_input = input("Enter a value: ")

# Check if input is a palindrome
input_palindrome = isPalindrome(user_input)
print("Input is a palindrome:", input_palindrome)

# Convert to binary if numeric
binary_value = toBinaryIfNumber(user_input)
if binary_value:
    print("Binary equivalent:", binary_value)
    binary_palindrome = isPalindrome(binary_value)
    print("Binary is a palindrome:", binary_palindrome)
else:
    print("(No binary conversion since input is text)")
