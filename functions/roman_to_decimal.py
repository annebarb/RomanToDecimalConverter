def roman_to_decimal(roman_input):
    # Roman numbers value mapping
    value = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    # Initialize previous character, answer, character counter, subtraction execution
    initial_value = 0
    answer = 0
    count = 1
    sub_num = 0
    sub_index = 0

    # Traverse through all characters backwards
    length = len(roman_input)
    roman_input = roman_input.upper()
    for i in range(length - 1, -1, -1):

        # Rule that doesn't allow invalid roman characters
        if roman_input[i] not in value.keys():
            return "'{}' is an invalid roman numeral".format(str(roman_input[i]))

        # Rule to limit the repetition of a roman character more than 3 times in a row
        if count == 4:
            return "'{}' was used more than 3 times in a row".format(str(roman_input[i - 1]))

        # Rule that forbids a V roman character standing to the left of X
        if initial_value == 10 and roman_input[i] == "V":
            return "V is never written to the left of X"

        # Rule that makes a roman numeral invalid if contains more then one subtraction
        if value[roman_input[i]] < sub_num:
            return "A numeral of lower value, may not stand in front of a group of numerals in subtractive notation, " \
                   "invalid roman numeral "
        else:
            sub_num = 0

        # If greater than or equal to previous value, add to answer
        if value[roman_input[i]] >= initial_value:
            answer += value[roman_input[i]]

        # If smaller than previous value
        else:
            if sub_index - i == 2:
                return "You cannot have two subtraction in a row, invalid roman numeral"
            answer -= value[roman_input[i]]
            sub_num = value[roman_input[i+1]] - value[roman_input[i]]
            sub_index = i

        # Update value
        if initial_value == value[roman_input[i]]:

            # Rule that forbids the repetition of the V, D, L characters
            if roman_input[i] in "VDL":
                return "'{}' numeral cannot be repeated".format(str(roman_input[i - 1]))
            count += 1
        else:
            count = 1
        initial_value = value[roman_input[i]]

    return answer


# Site that works as intended for roman numerals https://roman-numerals.info/
# you can use this to check how any number from 1 to 3999 should be displayed

# Added some tests to help you out
print('All these values should be valid')
print(roman_to_decimal('I'))        # 1
print(roman_to_decimal('II'))       # 2
print(roman_to_decimal('III'))      # 3
print(roman_to_decimal('IV'))       # 4
print(roman_to_decimal('V'))        # 5
print(roman_to_decimal('VI'))       # 6
print(roman_to_decimal('VII'))      # 7
print(roman_to_decimal('VIII'))     # 8
print(roman_to_decimal('IX'))       # 9
print(roman_to_decimal('X'))        # 10
print(roman_to_decimal('XI'))       # 11
print(roman_to_decimal('XII'))      # 12
print(roman_to_decimal('XIII'))     # 13
print(roman_to_decimal('XIV'))      # 14
print(roman_to_decimal('XV'))       # 15
print(roman_to_decimal('XVII'))     # 16
print(roman_to_decimal('XVIII'))    # 18
print(roman_to_decimal('XIX'))      # 19
print(roman_to_decimal('XX'))       # 20
print(roman_to_decimal('XXI'))      # 21
print(roman_to_decimal('XXII'))     # 22
print(roman_to_decimal('XXIII'))    # 23
print(roman_to_decimal('XXIV'))     # 24
print(roman_to_decimal('XXV'))      # 25
print(roman_to_decimal('XXVI'))     # 26
print(roman_to_decimal('XXVII'))    # 27
print(roman_to_decimal('XXVIII'))   # 28
print(roman_to_decimal('XXIX'))     # 29
print(roman_to_decimal('XXX'))      # 30
print(roman_to_decimal('XXXI'))     # 31
print(roman_to_decimal('XXXII'))    # 32
print(roman_to_decimal('XXXIII'))   # 33
print(roman_to_decimal('XXXIV'))    # 34
print(roman_to_decimal('XXXV'))     # 35
print(roman_to_decimal('XXXVI'))    # 36
print(roman_to_decimal('XXXVII'))   # 37
print(roman_to_decimal('XXXVIII'))  # 38
print(roman_to_decimal('XXXIX'))    # 39
print(roman_to_decimal('XL'))       # 40
print(roman_to_decimal('XLI'))      # 41
print(roman_to_decimal('XLII'))     # 42
print(roman_to_decimal('XLIII'))    # 43
print(roman_to_decimal('XLIV'))     # 44
print(roman_to_decimal('XLV'))      # 45
print(roman_to_decimal('XLVI'))     # 46
print(roman_to_decimal('XLVII'))    # 47
print(roman_to_decimal('XLVIII'))   # 48
print(roman_to_decimal('XLIX'))     # 49
print(roman_to_decimal('L'))        # 50
print(roman_to_decimal('MCCXII'))   # 1212
print(roman_to_decimal('MCMXCIX'))  # 1999
print(roman_to_decimal('MMMCMXCIX'))# 3999

print('\nAll these should be invalid')
print(roman_to_decimal('MMMCMXCXI'))# Invalid
print(roman_to_decimal('IXX'))      # Invalid
print(roman_to_decimal('VVV'))      # Invalid
print(roman_to_decimal('IVIV'))     # Invalid
print(roman_to_decimal('MCCIXI'))   # Invalid
print(roman_to_decimal('VIV'))      # Invalid
print(roman_to_decimal('IVI'))      # Invalid
print(roman_to_decimal('IXX'))      # Invalid