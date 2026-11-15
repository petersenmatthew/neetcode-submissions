class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 2):
            k = i + 1
            j = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while k < j:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    k+=1
                    j-=1 
                
                    while k < j and nums[k] == nums[k - 1]:
                        k+=1
                        
                    while k < j and nums[j] == nums[j+1]:
                        j-=1

                elif cur < 0:
                     k +=1
                else:
                    j-=1
        
        return output