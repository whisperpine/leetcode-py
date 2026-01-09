# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
# Topics: Two Pointers.
# Difficulty: Easy.

from string import ascii_letters, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_s: list[str] = [
            char.lower() for char in s if char in ascii_letters + digits
        ]
        return sanitized_s == sanitized_s[::-1]


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


def test_case_2() -> None:
    assert not Solution().isPalindrome("race a car")


def test_case_3() -> None:
    assert Solution().isPalindrome(" ")
