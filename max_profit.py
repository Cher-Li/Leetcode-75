class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        # I'm guessing dp is just, max profit on that ith day
        # and for each day, you can either buy given you already sold, or sell, or neither? So need to take the max of different options
        # base cases: 0 when starting out
        # dp = [0] * len(prices)

        # * either own stock or don't
        cash = 0 # max profit if don't own a share of stock
        hold = -prices[0] # max profit if do
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee) # cash, or sell stock
            # assume pay fee for stock sale
        
            hold = max(hold, cash - prices[i]) # either held stock, or bought w/ cash
        
        return cash