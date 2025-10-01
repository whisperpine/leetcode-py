# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
# Topics: Arrays & Hashing.
# Difficulty: Easy.


def test_case_1() -> None:
    assert Solution().containsDuplicate([1, 2, 3, 3])


def test_case_2() -> None:
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     unique_set: set[int] = set()
    #     for n in nums:
    #         if n not in unique_set:
    #             unique_set.add(n)
    #         else:
    #             return True
    #     return False
