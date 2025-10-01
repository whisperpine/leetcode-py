# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
# Topics: Arrays & Hashing.
# Difficulty: Easy.


def test_case_1() -> None:
    nums: list[int] = [2, 7, 11, 15]
    target: int = 9
    output: list[int] = [0, 1]
    assert output == Solution().twoSum(nums, target)


def test_case_2() -> None:
    nums: list[int] = [3, 2, 4]
    target: int = 6
    output: list[int] = [1, 2]
    assert output == Solution().twoSum(nums, target)


def test_case_3() -> None:
    nums: list[int] = [3, 3]
    target: int = 6
    output: list[int] = [0, 1]
    assert output == Solution().twoSum(nums, target)


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # k: element of nums, v: index
        prev_dict: dict[int, int] = {}

        for i, n in enumerate(nums):
            diff: int = target - n
            if diff in prev_dict.keys():
                return [prev_dict[diff], i]
            else:
                prev_dict[n] = i

        raise AssertionError("This line should be unreachable")
