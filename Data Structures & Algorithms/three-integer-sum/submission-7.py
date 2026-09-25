class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
  

        ## nums[i] + nums[j] + nums[k] == 0 
        ## [-4, -1, 0, 1, 2 , 4]

        output = set()
        for k, num in enumerate(nums[:-2]):
            i = k + 1
            j = len(nums) - 1

            target = -nums[k]
            while i < j:
                compare = nums[i]+ nums[j]
                if compare == target:
                    output.add((nums[i], nums[j], nums[k]))
                    i+=1
                elif compare < target:
                    i += 1
                else:
                    j-=1
        
        return list(output)

