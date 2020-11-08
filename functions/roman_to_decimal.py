def roman_to_decimal(roman_input):
    # Roman numbers value mapping
    value = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    # Initialize previous character and answer
    initial_value = 0
    answer = 0

    # Traverse through all characters backwards
    length = len(roman_input)
    for i in range(length-1, -1, -1):

        # If greater than or equal to previous value, add to answer
        if value[roman_input[i]] >= initial_value:
            answer += value[roman_input[i]]

        # If smaller than previous value
        else:
            answer -= value[roman_input[i]]

        # Update value
        initial_value = value[roman_input[i]]
    return answer
