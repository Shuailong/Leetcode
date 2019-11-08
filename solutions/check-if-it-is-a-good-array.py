from typing import List
from math import gcd
from functools import reduce


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        if gcd of nums are 1, return true. else return false.
        """
        return reduce(gcd, nums) == 1


if __name__ == "__main__":
    solution = Solution()
    nums = [12, 5, 7, 23]
    print(solution.isGoodArray(nums))
    nums = [29, 6, 10]
    print(solution.isGoodArray(nums))
    nums = [3, 6]
    print(solution.isGoodArray(nums))
