class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output=[]
        for i in nums:
            if i in output:
                return True
            else:
                output.append(i)
        return False
        