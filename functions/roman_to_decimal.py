def decimal_to_roman(int_input):
    """ Convert an decimal number to a Roman numeral. """

    if not isinstance(int_input, type(1)):
        raise TypeError("expected integer, got %s" % type(int_input))
    if not 0 < int_input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(int_input / ints[i])
        result.append(nums[i] * count)
        int_input -= ints[i] * count
    return ''.join(result)


def roman_to_decimal(roman_input):
    """ Convert a Roman numeral to a decimal number. """

    if not isinstance(roman_input, type("")):
        raise TypeError("expected string, got %s" % type(roman_input))
    roman_input = roman_input.upper()
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i in range(len(roman_input)):
        try:
            value = nums[roman_input[i]]
            # If the next place holds a larger number, this value is negative
            if i + 1 < len(roman_input) and nums[roman_input[i + 1]] > value:
                result -= value
            else:
                result += value
        except KeyError:
            raise ValueError('input is not a valid Roman numeral: %s' % roman_input)

    # validity test
    if decimal_to_roman(result) == roman_input:
        return result
    else:
        raise ValueError('input is not a valid Roman numeral: %s' % roman_input)
