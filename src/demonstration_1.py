"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
def two_sum(nums, target):
    # Your code here
    # for loop that is generating 2 values, the index and the num
    map = {element: index for index, element in enumerate(nums)}

    for i in range(len(nums)):
        diff = target - nums[i]

        # check id `diff` is a key in our map
        if diff in map:
            return [i, map[diff]]
    
    # at this point, we didn't find two values that up to our target
    return "No 2 elements sum up to our target"

nums = [3,8,12,17]
target = 15
print(two_sum(nums, target))