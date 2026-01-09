# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Topics: Sliding Window.
# Difficulty: Easy.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        result: int = 0
        buy_price: int = prices[0]
        sell_price: int = prices[0]

        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
                sell_price = p
            elif p > sell_price:
                sell_price = p
            result = max(sell_price - buy_price, result)

        return result


# ---------------------- #
# copy above to leetcode
# ---------------------- #


def test_case_1() -> None:
    result: int = 5
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == result


def test_case_2() -> None:
    result: int = 0
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == result


def test_case_3() -> None:
    result: int = 0
    assert Solution().maxProfit([]) == result
