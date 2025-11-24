class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        none_found = True
        for i in range(len(nums1)):
            none_found = True
            for j in range(nums2.index(nums1[i]), len(nums2)):
                print("Comparing ", nums1[i], "to ", nums2[j])
                if nums1[i] < nums2[j]:
                    print("Found: ", nums1[i], "less than ", nums2[j])
                    ans.append(nums2[j])
                    none_found = False
                    break
            if (none_found):
                print("None found for ", nums1[i])
                ans.append(-1)
        return ans
