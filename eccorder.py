from sympy import legendre_symbol

# Elliptic curve parameters
a = 13
b = 9
p = 8011

# Function to check if a quadratic residue exists
def is_quadratic_residue(y_squared):
    return legendre_symbol(y_squared, p) == 1

# Counting points on the curve
order = 1  # Include the point at infinity
for x in range(p):
    y_squared = (x**3 + a*x + b) % p
    if is_quadratic_residue(y_squared):
        order += 2  # Two points for each x, one for each y

print("Order of the elliptic curve:", order)