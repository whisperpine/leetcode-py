# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/
# Topics: Binary Search.
# Difficulty: Easy.


def test_case_1() -> None:
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_case_2() -> None:
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------

import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target not in nums:
            return -1
        index: int = bisect.bisect_left(nums, target)
        return index
