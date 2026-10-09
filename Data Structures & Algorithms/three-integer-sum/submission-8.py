class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for k in range(len(nums) - 2):
            # nums k = - (nums[i] + nums[j])
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.add((nums[k], nums[i], nums[j]))
                    i+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    j-=1
        
        return list(output)

