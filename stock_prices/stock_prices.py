#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2])
# need to find the max profit of list of stock prices. Return the maximum profit that can be made from a single buy and sell.
# Find every possible profit
# Every possible profit for a single price
# Find the maximum of every possible profit
profits = [1050, 270, 1540, 3800, 2]
# Buy price is 0 and the price after the buy price will net a profit, buy.
# Need to sell if the buy price is higher than the next index price.
# if buying price is 0 then the buying price is equal to the previous price index



def find_max_profit(prices):
    buyingPrice = 0
    sellingPrice = 0
    maxProfit = 0

    print(prices)
    for i in range(len(prices)-1):
      if buyingPrice == 0 and prices[i] < prices[i+1]:
        buyingPrice = prices[i]
      elif buyingPrice != 0 and prices[i] > prices[i+1]:
        if sellingPrice < prices[i]:
          sellingPrice = prices[i]

    if buyingPrice == 0:
      buyingPrice = prices[-1]

    maxProfit = sellingPrice - buyingPrice

    return maxProfit


if __name__ == '__main__':
                # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
