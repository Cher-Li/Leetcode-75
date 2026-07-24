# class Solution(object):
#     def predictPartyVictory(self, senate):
#         """
#         :type senate: str
#         :rtype: str
#         """
        
#         # 1. ban one senator's right - this and all following rounds so could just, remove them from the group entirely
#         # 2. announce victory if alone or all are the same character

#         # queue = deque(senate)
#         # while 'R' in queue and 'D' in queue: 
#         #     for i in range(len(queue)):
#         #         # if senator[i] is R, delete the first D, and vice versa? 
#         #         # shouldn't alter directly tho so need another method

#         # * using two queues one for each party
#         r_queue = deque()
#         d_queue = deque() 
#         for i in range(len(senate)):
#             if senate[i] == 'R':
#                 r_queue.append(i)
#             else:
#                 d_queue.append(i)
#         # queues store the indices

#         # prob don't need a while true, just check whichever's first in between r and d queues
#         while r_queue and d_queue: # breaks if one is empty to take care of case 2? 
#             if r_queue[0] < d_queue[0]: # queue stores the relative position, want the lesser one
#                 # R going first, remove the first from d_queue
#                 d_queue.popleft()

#                 # then need to take care of this first index, so we could just move to the back of the queue? 
#                 # r_queue.append(r_queue.popleft())
#                 # * need to ensure it's also back of the OTHER queue to establish each round
#                 idx = r_queue.popleft()
#                 r_queue.append(idx + len(senate)) # to keep relative position in terms of priority

#             else: 
#                 r_queue.popleft()
#                 # d_queue.append(d_queue.popleft())
#                 idx = d_queue.popleft()
#                 d_queue.append(idx + len(senate))
        
#         if r_queue:
#             return "Radiant" # yea returning the names itself
#         else: 
#             return "Dire" # O(N) 

# * more efficient soln w/ a single pass: 
class Solution(object):
    def predictPartyVictory(self, senate):
        queue = deque(senate)
        ban_balance = 0 # active bans, positive means R have the rights to ban D, negative is vice versa

        # count number of active senators
        r_count = senate.count('R')
        d_count = senate.count('D')

        while r_count > 0 and d_count > 0:
            curr = queue.popleft()

            if curr == "R":
                if ban_balance < 0:
                    # D have rights to ban, so this R is removed
                    r_count -= 1
                else:
                    # R survives, put back on queue for next round
                    queue.append("R")
                ban_balance += 1 # either consume that previous ban or add because there's another R
            else:
                if ban_balance > 0:
                    d_count -= 1
                else:
                    queue.append("D")
                ban_balance -= 1
    
        return "Radiant" if r_count > 0 else "Dire" 