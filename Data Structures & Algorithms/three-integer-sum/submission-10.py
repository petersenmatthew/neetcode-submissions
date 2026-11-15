class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i in range(len(nums) - 2):
            k = i + 1
            j = len(nums) - 1

            while k < j:
                cur = nums[i] + nums[j] + nums[k]
                if cur == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    k+=1
                elif cur < 0:
                    k +=1
                else:
                    j-=1
        
        return [[i, j, k] for i, j, k in output]