import re
import sys

# Mapping Roman numerals to their integer equivalents
roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def roman_to_arabic(roman: str) -> int:
    """Convert Roman numeral to integer."""
    result = 0
    for i in range(len(roman)):
        if i > 0 and roman_to_int[roman[i]] > roman_to_int[roman[i - 1]]:
            result += roman_to_int[roman[i]] - 2 * roman_to_int[roman[i - 1]]
        else:
            result += roman_to_int[roman[i]]
    return result

def arabic_to_roman(num: int) -> str:
    """Convert an integer to Roman numeral."""
    if num > 3999:
        return "You're going to need a bigger calculator."
    if num == 0:
        return "0 does not exist in Roman numerals."
    if num < 0:
        return "Negative numbers can’t be represented in Roman numerals."

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def calculate(expression: str) -> str:
    """Evaluate an expression with Roman numerals and return the result."""
    try:
        for roman in re.findall(r'[IVXLCDM]+', expression):
            expression = expression.replace(roman, str(roman_to_arabic(roman)))
        result = eval(expression)
        return arabic_to_roman(int(result))
    except (SyntaxError, NameError, ValueError):
        return "I don’t know how to read this."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression = ' '.join(sys.argv[1:])
        print(calculate(expression))
    else:
        print("No input provided.")
