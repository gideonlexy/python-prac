'''Find the Roman numeral for any given number.
Constraints
The input variable num must be an integer.
The value of num should be within the range of 1 to 3999, as the Roman numeral system does not have symbols for numbers beyond 3999.'''

def int_to_roman(num):
    """ 
    :type num: int
    :rtype: str
    """
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    result = ""
    
    for val, symbol in values:
        while num >= val:
            result += symbol
            num -= val
    return result

def main():
    # Test cases
    test_numbers = [3, 4, 9, 58, 1994]
    for number in test_numbers:
        roman_numeral = int_to_roman(number)
        print(f"{number} in Roman numeral is: {roman_numeral}")

if __name__ == "__main__":
    main()