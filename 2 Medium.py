from collections import Counter

class Solution:
    def majorityElement(self, nums):
        """
        Finds the majority element(s) in the given list.

        Parameters:
        - nums (List[int]): The input list of integers.

        Returns:
        - List[int]: A list containing the majority element(s) (appearing more than n/3 times).
        """
        # Calculate the threshold count for a majority element
        count_threshold = len(nums) // 3

        # Count the occurrences of each element in the list
        element_counter = Counter(nums)

        # Initialize a result list to store majority elements
        result = []

        # Check each element and add it to the result if it is a majority element
        for num, freq in element_counter.items():
            if freq > count_threshold:
                result.append(num)

        # Return the list of majority elements
        return result

# Create an instance of the Solution class
solution_instance = Solution()

# Take input from the user
nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Call the majorityElement method with the input
result = solution_instance.majorityElement(nums)

# Print the result with a clear message
print(f"The majority element(s) in the list {nums} is/are: {result}")
