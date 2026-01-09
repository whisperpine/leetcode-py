# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
# Topics: Stack.
# Difficulty: Easy.


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            match c:
                case left if left in "([{":
                    stack.append(left)
                case ")":
                    if stack and stack[-1] == "(":
                        _ = stack.pop()
                    else:
                        return False
                case "]":
                    if stack and stack[-1] == "[":
                        _ = stack.pop()
                    else:
                        return False
                case "}":
                    if stack and stack[-1] == "{":
                        _ = stack.pop()
                    else:
                        return False
                case _:
                    raise AssertionError("unreachable")
        return not stack


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    assert Solution().isValid("()")


def test_case_2() -> None:
    assert Solution().isValid("()[]{}")


def test_case_3() -> None:
    assert not Solution().isValid("(]")


def test_case_4() -> None:
    assert Solution().isValid("([])")


def test_case_5() -> None:
    assert not Solution().isValid("([)]")


def test_case_6() -> None:
    assert not Solution().isValid("]")


def test_case_7() -> None:
    assert not Solution().isValid("{")
