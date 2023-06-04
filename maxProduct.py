from typing import List

def maxProduct(nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = max(nums)

        for n in nums:
            vals = (n * currMax, n * currMin, n)
            currMax = max(vals)
            currMin = min(vals)

            res = max(res, currMax)
        return res

result = maxProduct([2,3,-2,4])