# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Topics: Arrays & Hashing.
# Difficulty: Medium.


from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c: Counter[int] = Counter(nums)  # num, counts
        return [num[0] for num in c.most_common(k)]


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    nums: list[int] = [1, 1, 1, 2, 2, 3]
    output: list[int] = [1, 2]
    assert set(Solution().topKFrequent(nums, 2)) == set(output)


def test_case_2() -> None:
    nums: list[int] = [1]
    output: list[int] = [1]
    assert set(Solution().topKFrequent(nums, 1)) == set(output)


def test_case_3() -> None:
    nums: list[int] = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    output: list[int] = [1, 2]
    assert set(Solution().topKFrequent(nums, 2)) == set(output)
