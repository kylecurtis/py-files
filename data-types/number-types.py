# =============================================================================
# IMPORTS
# =============================================================================
import decimal
import math
import sys
from decimal import Decimal

# =============================================================================
# INTEGERS
# =============================================================================
# Integers in Python are whole numbers without a fractional component
# They can be positive, negative, or zero

# Basic integer declaration
a = 10
b = -5
c = 0

# Python supports arbitrary-precision integers (no size limit besides memory)
very_large_number = 9999999999999999999999999999
print(f"Very large integer: {very_large_number}")

# Integer literals in different bases
decimal_number = 42  # Base 10 (default)
binary_number = 0b101010  # Base 2 (prefix: 0b)
octal_number = 0o52  # Base 8 (prefix: 0o)
hex_number = 0x2A  # Base 16 (prefix: 0x)

print(
    f"Integer literals: {decimal_number}, {binary_number}, {octal_number}, {hex_number}"
)

# Underscores can be used for readability in large numbers
readable_large_number = 1_000_000  # Same as 1000000
print(f"One million with underscores: {readable_large_number}")


# =============================================================================
# FLOATING-POINT NUMBERS:
# Floating-point numbers are numbers with a decimal point or in scientific
# notation
# =============================================================================

# Basic float declaration
x = 3.14
y = -0.001
z = 0.0

# Scientific notation
avogadro_number = 6.022e23  # 6.022 * 10^23
planck_constant = 6.626e-34  # 6.626 * 10^-34
print(f"Avogadro's number: {avogadro_number}")
print(f"Planck's constant: {planck_constant}")

# Floating-point division always returns a float
float_division = 10 / 3
print(f"10 / 3 = {float_division}")

# =============================================================================
# COMPLEX NUMBERS:
# Complex numbers have a real and an imaginary part (j represents the imaginary
# unit)
# =============================================================================

# Basic complex number declaration
c1 = 2 + 3j
c2 = complex(4, -1)  # Alternative constructor: complex(real, imag)

# Complex number properties and operations
print(f"Complex number: {c1}")
print(f"Real part: {c1.real}")
print(f"Imaginary part: {c1.imag}")
print(f"Complex conjugate: {c1.conjugate()}")

# Complex arithmetic
c3 = c1 + c2
print(f"Addition: {c1} + {c2} = {c3}")

c4 = c1 * c2
print(f"Multiplication: {c1} * {c2} = {c4}")

# =============================================================================
# NUMBER TYPE CONVERSION:
# Python provides functions to convert between number types
# =============================================================================

# Integer to float conversion
float_from_int = float(42)
print(f"Integer 42 to float: {float_from_int}")

# Float to integer conversion (truncates, does not round)
int_from_float = int(3.14)
print(f"Float 3.14 to integer: {int_from_float}")

# String to number conversion
int_from_string = int("123")
float_from_string = float("3.14159")
print(f"String '123' to integer: {int_from_string}")
print(f"String '3.14159' to float: {float_from_string}")

# Base conversion with strings
hex_string = "1A"
decimal_from_hex = int(hex_string, 16)  # Convert hex string to decimal
print(f"Hex '1A' to decimal: {decimal_from_hex}")

# Number to different base string representation
decimal_number = 26
binary_string = bin(decimal_number)
octal_string = oct(decimal_number)
hex_string = hex(decimal_number)
print(f"Decimal {decimal_number} to binary: {binary_string}")
print(f"Decimal {decimal_number} to octal: {octal_string}")
print(f"Decimal {decimal_number} to hex: {hex_string}")

# Complex conversion
complex_from_parts = complex(1, 2)  # 1 + 2j
print(f"Complex from parts (1, 2): {complex_from_parts}")

# Round to nearest integer (returns an integer)
rounded_number = round(3.7)
print(f"3.7 rounded to nearest integer: {rounded_number}")

# Round to specific decimal places
rounded_to_places = round(3.14159, 2)  # Round to 2 decimal places
print(f"3.14159 rounded to 2 decimal places: {rounded_to_places}")


# =============================================================================
# ARITHMETIC OPERATIONS:
# Python supports all standard arithmetic operations
# =============================================================================

a, b = 10, 3

# Basic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b  # Always returns float

print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")

# Integer division (floor division)
floor_division = a // b  # Discards the decimal part
print(f"Floor division: {a} // {b} = {floor_division}")

# Modulo (remainder)
remainder = a % b
print(f"Modulo (remainder): {a} % {b} = {remainder}")

# Power operation
power = a**b  # a raised to the power of b
print(f"Power: {a} ** {b} = {power}")

# Negation
negation = -a
print(f"Negation of {a} = {negation}")

# Absolute value
abs_value = abs(-15)
print(f"Absolute value of -15: {abs_value}")

# Divmod (returns quotient and remainder as a tuple)
quotient, remainder = divmod(a, b)
print(f"divmod({a}, {b}) = ({quotient}, {remainder})")

# =============================================================================
# MATH MODULE FUNCTIONS:
# The math module provides additional mathematical functions
# =============================================================================

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number (e): {math.e}")
print(f"Tau (2*pi): {math.tau}")
print(f"Infinity: {math.inf}")
print(f"NaN (Not a Number): {math.nan}")

# Basic functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"16 raised to power 0.5 (equivalent to sqrt): {math.pow(16, 0.5)}")
print(f"Ceiling of 3.1 (round up): {math.ceil(3.1)}")
print(f"Floor of 3.9 (round down): {math.floor(3.9)}")
print(f"Truncate 3.9 (remove decimal): {math.trunc(3.9)}")
print(f"Absolute value of -7.5: {math.fabs(-7.5)}")

# Trigonometric functions (arguments in radians)
print(f"Sine of π/2: {math.sin(math.pi / 2)}")
print(f"Cosine of π: {math.cos(math.pi)}")
print(f"Tangent of π/4: {math.tan(math.pi / 4)}")

# Inverse trigonometric functions (return radians)
print(f"Arc sine of 1: {math.asin(1)}")
print(f"Arc cosine of 0: {math.acos(0)}")
print(f"Arc tangent of 1: {math.atan(1)}")

# Conversion between degrees and radians
degrees_45 = 45
radians_45 = math.radians(degrees_45)
print(f"45 degrees in radians: {radians_45}")
print(f"{radians_45} radians in degrees: {math.degrees(radians_45)}")

# Hyperbolic functions
print(f"Hyperbolic sine of 1: {math.sinh(1)}")
print(f"Hyperbolic cosine of 1: {math.cosh(1)}")
print(f"Hyperbolic tangent of 1: {math.tanh(1)}")

# Exponential and logarithmic functions
print(f"e raised to power 2: {math.exp(2)}")
print(f"Natural logarithm (base e) of 10: {math.log(10)}")
print(f"Base-10 logarithm of 100: {math.log10(100)}")
print(f"Base-2 logarithm of 8: {math.log2(8)}")
print(f"Logarithm of 8 with base 2: {math.log(8, 2)}")

# Special functions
print(f"Error function at 1: {math.erf(1)}")
print(f"Gamma function at 5: {math.gamma(5)}")
print(f"Factorial of 5: {math.factorial(5)}")

# Greatest common divisor and least common multiple
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
print(f"LCM of 4 and 6: {math.lcm(4, 6)}")  # Available in Python 3.9+

# Statistical functions
data = [1, 2, 3, 4, 5]
print(f"Sum of data: {sum(data)}")  # Built-in function
print(f"Product of data: {math.prod(data)}")  # Available in Python 3.8+

# =============================================================================
# NUMERIC PRECISION AND LIMITATIONS:
# Understanding precision issues and limitations of number representations
# =============================================================================

# Integer precision
# Python integers have unlimited precision (limited only by available memory)
large_factorial = math.factorial(100)  # 100! is a very large number
print(f"100! has {len(str(large_factorial))} digits")

# Float precision issues
# Floating-point numbers have limited precision and may lead to unexpected
# results
a = 0.1 + 0.2
b = 0.3
print(f"0.1 + 0.2 = {a}")
print(f"0.3 = {b}")
print(f"0.1 + 0.2 == 0.3: {a == b}")  # Will likely be False due to precision
print(f"Difference: {abs(a - b)}")

# Using decimal for higher precision
decimal.getcontext().prec = 28  # Set precision to 28 digits
d1 = Decimal("0.1")
d2 = Decimal("0.2")

d3 = d1 + d2
print(f"Using Decimal: 0.1 + 0.2 = {d3}")
print(f"Using Decimal: 0.1 + 0.2 == 0.3: {d3 == Decimal('0.3')}")

# Float limitations
print(f"Maximum representable float: {sys.float_info.max}")
print(f"Minimum positive representable float: {sys.float_info.min}")
print(f"Float epsilon (smallest representable difference): {sys.float_info.epsilon}")

# Infinity
positive_infinity = float("inf")
negative_infinity = float("-inf")
print(f"Positive infinity: {positive_infinity}")
print(f"Negative infinity: {negative_infinity}")
print(f"Is infinity: {math.isinf(positive_infinity)}")

# NaN (Not a Number)
not_a_number = float("nan")
print(f"NaN: {not_a_number}")
print(f"Is NaN: {math.isnan(not_a_number)}")
print(f"NaN equality check: {not_a_number == not_a_number}")  # Always False

# Integer overflow in other languages vs Python
# In many languages this would overflow, but Python handles it automatically
very_big = 2**1000
print(f"2^1000 has {len(str(very_big))} digits")
