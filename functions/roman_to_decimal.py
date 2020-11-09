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


