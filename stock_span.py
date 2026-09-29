class StockSpanner(object):

    def __init__(self):
        self.stack = [] # * pairs of price, span
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        # span of price = max num consec days going back for which stock was <= price
        # gives monotonic stack vibes, keep track of highest price and pop the ones which <= cur price

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1] # *

        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)