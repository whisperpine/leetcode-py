# 15. 3Sum
# https://leetcode.com/problems/3sum/description/
# Topics: Two Pointers.
# Difficulty: Medium.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        length: int = len(nums)
        if length < 3:
            return []

        # Sorting is essential or the following steps.
        nums.sort()

        for i in range(length - 2):
            # When the smallest number is more than 0,
            # it's impossible to find such a triplet.
            if nums[i] > 0:
                break
            # Remove duplicates of the 1rd item of a triplet.
            if i >= 1 and nums[i - 1] == nums[i]:
                continue

            j: int = i + 1  # Index of the 2nd item.
            k: int = length - 1  # Index of the 3rd item.

            while j < k:
                summary: int = nums[i] + nums[j] + nums[k]
                if summary > 0:
                    k -= 1
                    continue
                if summary < 0:
                    j += 1
                    continue
                result.append([nums[i], nums[j], nums[k]])
                # Remove duplicates of the 2nd item of a triplet.
                while j < k and nums[k - 1] == nums[k]:
                    k -= 1
                # remove duplicates of the 3rd item of a triplet.
                while j < k and nums[j + 1] == nums[j]:
                    j += 1
                k -= 1
                j += 1

        return result


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def make_orders_dont_matter(li: list[list[int]]) -> list[tuple[int, ...]]:
    return sorted(tuple(sorted(item)) for item in li)


def test_case_1() -> None:
    expected: list[list[int]] = [[-1, -1, 2], [-1, 0, 1]]
    processed_expected: list[tuple[int, ...]] = make_orders_dont_matter(expected)
    output: list[list[int]] = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    processed_output: list[tuple[int, ...]] = make_orders_dont_matter(output)
    assert processed_output == processed_expected


def test_case_2() -> None:
    expected: list[list[int]] = []
    processed_expected: list[tuple[int, ...]] = make_orders_dont_matter(expected)
    output: list[list[int]] = Solution().threeSum([0, 1, 1])
    processed_output: list[tuple[int, ...]] = make_orders_dont_matter(output)
    assert processed_output == processed_expected


def test_case_3() -> None:
    expected: list[list[int]] = [[0, 0, 0]]
    processed_expected: list[tuple[int, ...]] = make_orders_dont_matter(expected)
    output: list[list[int]] = Solution().threeSum([0, 0, 0])
    processed_output: list[tuple[int, ...]] = make_orders_dont_matter(output)
    assert processed_output == processed_expected


def test_case_4() -> None:
    expected: list[list[int]] = [[0, 0, 0]]
    processed_expected: list[tuple[int, ...]] = make_orders_dont_matter(expected)
    output: list[list[int]] = Solution().threeSum([0, 0, 0, 0])
    processed_output: list[tuple[int, ...]] = make_orders_dont_matter(output)
    assert processed_output == processed_expected
