# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
# Topics: Arrays & Hashing.
# Difficulty: Medium.


def test_case_1() -> None:
    strs: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert Solution().groupAnagrams(strs) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]


def test_case_2() -> None:
    assert Solution().groupAnagrams([""]) == [[""]]


def test_case_3() -> None:
    assert Solution().groupAnagrams(["a"]) == [["a"]]


# ---------------------------------
# copy to leetcode starts from here
# ---------------------------------


# def get_key(s: str) -> str:
#     bit_mask: list[int] = [0] * 26
#     for c in s:
#         bit_mask[ord(c) - ord("a")] += 1
#     return "".join(str(i) for i in bit_mask)

from collections import defaultdict


def get_key(s: str) -> str:
    return str(sorted(s))


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # k: unique identifier, v: list of anagrams
        result: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            key: str = get_key(s)
            result[key].append(s)
        return list(result.values())
