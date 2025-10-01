# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# Topics: Arrays & Hashing.
# Difficulty: Easy.


def test_case_1() -> None:
    assert Solution().isAnagram("anagram", "nagaram")


def test_case_2() -> None:
    assert Solution().isAnagram("rat", "car") == False


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars: Counter[str] = Counter(s)
        t_chars: Counter[str] = Counter(t)
        return s_chars == t_chars
