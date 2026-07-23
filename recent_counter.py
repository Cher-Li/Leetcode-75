class RecentCounter(object):

    def __init__(self):
        # init w/ zero recent requests
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        # adds new request at time t then return num requests in the past 3000 ms
        # I was thinking just appending the new request at the end of the queue
        # either find the request that barely passes 3000 ms threshold, or entirely dequeue the ones that already passes
        self.queue.append(t) # * also review add vs append
        # for request in self.queue:
        #     if request < t - 3000:
        #         self.queue.popleft() # * default pop right? 
        #     else:
        #         break

        # * while loop probably cleaner here
        while self.queue and self.queue[0] < t - 3000: 
            self.queue.popleft()

        return len(self.queue)    


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)