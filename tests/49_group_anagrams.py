# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/
# Topics: Arrays & Hashing.
# Difficulty: Medium.


from collections import defaultdict

# def get_key(s: str) -> str:
#     bit_mask: list[int] = [0] * 26
#     for c in s:
#         bit_mask[ord(c) - ord("a")] += 1
#     return "".join(str(i) for i in bit_mask)


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


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    strs: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected: list[list[str]] = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    output: list[list[str]] = sorted(Solution().groupAnagrams(strs))
    assert {frozenset(i) for i in output} == {frozenset(i) for i in expected}


def test_case_2() -> None:
    strs: list[str] = [""]
    expected: list[list[str]] = [[""]]
    output: list[list[str]] = sorted(Solution().groupAnagrams(strs))
    assert {frozenset(i) for i in output} == {frozenset(i) for i in expected}


def test_case_3() -> None:
    strs: list[str] = ["a"]
    expected: list[list[str]] = [["a"]]
    output: list[list[str]] = sorted(Solution().groupAnagrams(strs))
    assert {frozenset(i) for i in output} == {frozenset(i) for i in expected}
