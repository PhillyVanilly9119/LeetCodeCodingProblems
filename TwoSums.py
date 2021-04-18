
# Problem description: 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int] :
        dic = {}
        count = 0
        for i in range(len(nums)):
            if dic.get(target-nums[i]) is not None:
                return dic[target-nums[i]], i
            dic[nums[i]] = count
            count+=1

def main() :
    s = Solution

if __name__ == '__main__' :
    main()