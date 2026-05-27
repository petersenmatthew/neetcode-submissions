class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        # 0 = nums[i] + nums[j] + nums[k]
        # - nums[i] = nums[j] + nums[k]

        output = set()
        for i in range(len(nums) - 2):
            print("cur i:", i)
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    print('adding', i, j, k)
                    output.add(tuple([nums[i], nums[j], nums[k]]))
                    j+=1
                    k-=1
                    print(output)
                elif nums[j] + nums[k] < target and j < k:
                    print("too small, increment j")
                    j+=1
                elif nums[j] + nums[k] > target and j < k:
                    print("too small, decerease k")
                    k-=1
        print(output)
        return list(output)