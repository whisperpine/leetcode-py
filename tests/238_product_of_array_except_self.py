# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/
# Topics: Arrays & Hashing.
# Difficulty: Medium.

# Solution from the NeetCode YouTube channel:
# https://www.youtube.com/watch?v=bNvIQI2wAjk


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr: list[int] = [1] * len(nums)
        left = 1
        for n in range(len(nums)):
            arr[n] = left
            left *= nums[n]
        right = 1
        for n in range(len(nums) - 1, -1, -1):
            arr[n] *= right
            right *= nums[n]
        return arr

    # def productExceptSelf(self, nums: list[int]) -> list[int]:
    #     length = len(nums)
    #     prefix: list[int] = [1] * length
    #     postfix: list[int] = [1] * length
    #     for i in range(1, length):
    #         prefix[i] = prefix[i - 1] * nums[i - 1]
    #     for i in range(length - 2, -1, -1):
    #         postfix[i] = postfix[i + 1] * nums[i + 1]
    #     return [prefix[i] * postfix[i] for i in range(len(nums))]


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_case_2() -> None:
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
