class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input: array of nums
        # ouput: [index1, index2] where numbers[index1] + numbers[index2] = target

        l = 0
        r = len(numbers) - 1
        
        while l < r:
            current = numbers[l] + numbers[r]
            if current == target:
                return [l + 1,r + 1] 
            
            if current < target:
                l+=1
            else:
                r-=1
        return False