def countDigitOne(n):
    """
    Counts the frequency of digit '1' in numbers less than or equal to the given number.

    Parameters:
    - n (int): The given number.

    Returns:
    - int: The frequency of digit '1'.
    """
    count = 0

    for i in range(1, n + 1):
        str_i = str(i)
        count += str_i.count("1")

    return count

# Take input from the user
n = int(input("Enter a number: "))

# Call the countDigitOne function with the user input
result = countDigitOne(n)

# Print the result with a clear message
print(f"The frequency of digit '1' in numbers up to {n} is: {result}")
