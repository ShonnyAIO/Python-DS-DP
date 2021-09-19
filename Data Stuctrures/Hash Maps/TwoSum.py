def twoSum(self, nums: List[int], target: int) -> List[int]:
    sumMap={}
    for i in range(len(nums)):
        if nums[i] not in sumMap:
            sumMap[target-nums[i]]=i
        else:
            return [sumMap[nums[i]],i]
    return -1,-1
