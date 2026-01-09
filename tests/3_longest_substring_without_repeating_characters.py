# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Topics: Sliding Window.
# Difficulty: Medium.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start: int = 0
        max_length: int = 1
        # key: character, value: index
        last_index: dict[str, int] = {}

        for i, c in enumerate(s):
            start = max(start, last_index.get(c, 0) + 1)
            max_length = max(max_length, i - start + 1)
            last_index[c] = i

        return max_length


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_case_2() -> None:
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test_case_3() -> None:
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3


def test_case_4() -> None:
    assert Solution().lengthOfLongestSubstring("") == 0


def test_case_5() -> None:
    assert Solution().lengthOfLongestSubstring("aabaab!bb") == 3
