# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    # 1st solution, brute force approach
    def twoSum(self, nums, target):
        for index_i, i in enumerate(nums):
            indexes = []
            indexes.append(index_i)
            current_sum = i
            for index_j, j in enumerate(nums):
                current_sum += j
                if index_j == index_i:
                    current_sum = i
                    continue
                if current_sum == target:
                    indexes.append(index_j)
                    return indexes
                current_sum = i

    #2nd solution, using hash map
    def twoSum_2(self, nums, target):
        numbers_hash_map = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in numbers_hash_map:
                return [numbers_hash_map[difference], index]
            numbers_hash_map[number] = index