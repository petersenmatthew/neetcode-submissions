class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make a prefix products array
        prefix_products = []
        running_prefix_product = 1

        for num in nums:
            running_prefix_product *= num
            prefix_products.append(running_prefix_product)

        # make a suffix products array
        suffix_products = []
        running_suffix_product = 1

        for num in reversed(nums):
            running_suffix_product *= num
            suffix_products.append(running_suffix_product)
        suffix_products.reverse()
        print(prefix_products)
        print(suffix_products)

        output = [0] * len(nums)

        for i in range(len(nums)):
            # start:
            if i == 0:
                output[i] = suffix_products[i + 1]

            # end 
            elif i == len(nums) - 1:
                output[i] = prefix_products[i-1]  

            # middle
            else:
                output[i] = prefix_products[i-1] * suffix_products[i+1]

        return output