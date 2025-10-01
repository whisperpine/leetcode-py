# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Topics: Arrays & Hashing.
# Difficulty: Medium.


def test_case_1() -> None:
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4


def test_case_2() -> None:
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_case_3() -> None:
    assert Solution().longestConsecutive([1, 0, 1, 2]) == 3


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------


def get_left_length(n: int, s: set[int]) -> int:
    result: int = 0
    if n in s:
        s.remove(n)
        result += 1 + get_left_length(n - 1, s)
    return result


def get_right_length(n: int, s: set[int]) -> int:
    result: int = 0
    if n in s:
        s.remove(n)
        result += 1 + get_right_length(n + 1, s)
    return result


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        result: int = 0
        s: set[int] = set(nums)

        for n in nums:
            if n in s:
                s.remove(n)
                left_len: int = get_left_length(n - 1, s)
                right_len: int = get_right_length(n + 1, s)
                result = max(result, 1 + left_len + right_len)

        return result
