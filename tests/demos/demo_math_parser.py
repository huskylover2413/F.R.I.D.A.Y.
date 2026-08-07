"""
==========================================================
F.R.I.D.A.Y.
Math Parser Validation Demo

Foundation Release:
    13.4
==========================================================
"""

from runtime.skills.system.math_parser import MathParser

parser = MathParser()

TESTS = {
    # Arithmetic
    "2+2": 4,
    "10-3": 7,
    "5*8": 40,
    "100/4": 25,
    "20//3": 6,
    "10%3": 1,

    # Parentheses
    "(2+3)*5": 25,
    "((4+6)*5)/2": 25,

    # Powers
    "2^10": 1024,
    "3^4": 81,
    "pi^2": 9.869604401089358,

    # Decimals
    "3.5*12": 42,
    "-5+8": 3,

    # Constants
    "pi": 3.141592653589793,
    "e": 2.718281828459045,
    "tau": 6.283185307179586,

    # Roots
    "sqrt(81)": 9,
    "sqrt(25)+sqrt(144)": 17,

    # Trig
    "sin(radians(90))": 1,
    "cos(radians(180))": -1,
    "tan(radians(45))": 1,

    # Logs
    "log10(1000)": 3,
    "log2(1024)": 10,

    # Misc
    "factorial(6)": 720,
    "abs(-42)": 42,
    "ceil(3.2)": 4,
    "floor(3.8)": 3,

    # Advanced
    "gcd(84,36)": 12,
    "lcm(12,18)": 36,
    "comb(10,3)": 120,
    "perm(10,3)": 720,
    "hypot(3,4)": 5,

    # Statistics
    "mean([1,2,3,4,5])": 3,
    "median([1,2,3,4,5])": 3,
}

passed = 0
failed = 0

print()
print("========== Math Parser Validation ==========")
print()

for expression, expected in TESTS.items():

    try:

        result = parser.evaluate(expression)

        if isinstance(result, float):
            result = round(result, 10)

        if isinstance(expected, float):
            expected = round(expected, 10)

        if result == expected:
            passed += 1
            print(f"✓ {expression:<35} {result}")
        else:
            failed += 1
            print(f"✗ {expression:<35} got {result} expected {expected}")

    except Exception as error:
        failed += 1
        print(f"✗ {expression:<35} {error}")

print()
print(f"Passed : {passed}")
print(f"Failed : {failed}")
print()