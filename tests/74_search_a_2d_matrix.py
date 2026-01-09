# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/
# Topics: Binary Search.
# Difficulty: Medium.


from itertools import chain
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # flattened: Iterator[int] = (item for sublist in matrix for item in sublist)
        flattened: Iterator[int] = chain(*matrix)
        return target in flattened


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    matrix: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 3)


def test_case_2() -> None:
    matrix: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert not Solution().searchMatrix(matrix, 13)
