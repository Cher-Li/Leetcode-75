# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
#         # w/o using division op
#         # prefix product problem
#         # left_products is product of all elmts left of nums[i], right_products is right of nums[i]
#         # then just multiply the two

#         # left_products = []
#         # product = 1
#         # left_products.append(product)

#         left_products = [1] * len(nums)
#         right_products = [1] * len(nums)
#         product = 1

#         # for i in range(1, len(nums) - 1):
#         #     product = product * nums[i]
#         #     left_products.append(product)
#         for i in range(len(nums)):
#             left_products[i] = product
#             product *= nums[i]
        
#         # * reset product
#         product = 1
#         # right_products[len(nums) - 1] = 1
#         # for j in range(len(nums) - 2, -1, -1): 
#         #     product = product * nums[j]
#         #     right_products[j] = product
#         # * more convoluted than needs to be, also not technically wrong because includes current num

#         for i in range(len(nums) - 1, -1, -1):
#             right_products[i] = product
#             product *= nums[i]
        
#         # * can't multiply directly
#         # return left_products * right_products

#         answer = [0] * len(nums)
#         for i in range(len(nums)):
#             answer[i] = left_products[i] * right_products[i]

#         return answer

# * O(1) extra space
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # just directly reusing that same ans arr
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans