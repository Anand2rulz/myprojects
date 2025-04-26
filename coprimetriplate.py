import math

def is_coprime_triplet(a, b, c):
    # Check if GCD of all three is 1
    gcd_ab = math.gcd(a, b)
    gcd_abc = math.gcd(gcd_ab, c)
    return gcd_abc == 1

# Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if is_coprime_triplet(a, b, c):
    print(f"{a}, {b}, {c} form a coprime triplet.")
else:
    print(f"{a}, {b}, {c} do not form a coprime triplet.")
