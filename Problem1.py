def gcd(a, b):
    # Recursive function to compute GCD
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(x, y):
    # LCM formula using GCD
    return (x * y) // gcd(x, y)

while True:
    try:
        x = int(input("Enter a value for x: "))
        y = int(input("Enter a value for y: "))
        if x > 0 and y > 0:
            break
        else:
            print("Both numbers must be positive and non-zero.")
    except ValueError:
        print("Please enter valid integers.")

print(f"The LCM of {x} and {y} is = {lcm(x, y)}") 

