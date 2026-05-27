class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0 = nums[i] + nums[j] + nums[k]
        # - nums[i] = nums[j] + nums[k]
        # target = - nums[i]

        output = set()
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l +=1
                elif cur > target:
                    r-=1
                else:
                    output.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1

        return list(output)



















        """
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
        """