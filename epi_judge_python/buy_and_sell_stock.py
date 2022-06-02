from typing import List

from test_framework import generic_test

# 6/2/2022
def buy_and_sell_stock_once(prices: List[float]) -> float:
    # we use two pointer
    max_profit = 0

    buy, sell = 0, 1

    while sell != len(prices):
        profit = prices[sell] - prices[buy]
        if profit > 0:
            if profit > max_profit:
                max_profit = profit
        else:
            buy = sell
        sell += 1

    return max_profit


# T: O(n) since we iterate through array
# S: O(1) because we only use pointers

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
