def three_sum(nums):                           # Define a function named 'three_sum' that takes a list of numbers as input
    nums.sort()                                # Sort the list in ascending order to make two-pointer logic work properly
    res = []                                   # Create an empty list to store the resulting triplets
    n = len(nums)                              # Store the length of the list for easy reference

    for i in range(n - 2):                     # Loop through the list until the third last element
        if i > 0 and nums[i] == nums[i - 1]:   # Skip this number if it's the same as the previous one (to avoid duplicates)
            continue                           # Move to the next iteration

        l = i + 1                              # Set the left pointer to the element just after 'i'
        r = n - 1                              # Set the right pointer to the last element of the list

        while l < r:                           # Continue looping while left pointer is before the right pointer
            s = nums[i] + nums[l] + nums[r]    # Calculate the sum of the three numbers at indices i, l, and r

            if s == 0:                         # If the sum is zero, we found a valid triplet
                res.append([nums[i], nums[l], nums[r]])  # Add the triplet to the result list
                l += 1                         # Move the left pointer one step forward
                r -= 1                         # Move the right pointer one step backward

                while l < r and nums[l] == nums[l - 1]:  # Skip duplicate numbers for the left pointer
                    l += 1                     # Keep moving left pointer forward

                while l < r and nums[r] == nums[r + 1]:  # Skip duplicate numbers for the right pointer
                    r -= 1                     # Keep moving right pointer backward

            elif s < 0:                        # If the sum is less than zero,
                l += 1                         # Move the left pointer to the right to increase the sum
            else:                              # If the sum is greater than zero,
                r -= 1                         # Move the right pointer to the left to decrease the sum

    return res                                 # After all loops, return the list of all unique triplets found


# Example usage:
print(three_sum([-1, 0, 1, 2, -1, -4]))        # Print the result for the given list
                                                # Expected output: [[-1, -1, 2], [-1, 0, 1]]
