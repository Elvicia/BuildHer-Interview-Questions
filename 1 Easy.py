class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the given string.

        Parameters:
        - s (str): The input string.

        Returns:
        - int: The length of the last word.
        """
        # Start from the end of the string and skip trailing whitespaces
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the length of the last word
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1

        # Calculate and return the length of the last word
        return i - j

# Create an instance of the Solution class
solution_instance = Solution()

# Take input from the user
input_string = input("Enter a string: ")

# Call the lengthOfLastWord method with the input
result = solution_instance.lengthOfLastWord(input_string)

# Print the result with a clear message
print(f"The length of the last word in the string '{input_string}' is: {result}")
