from typing import List

def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSub = max(maxSub, currSum)

    return maxSub

result = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)