class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

# Example 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]

# Example 2
nums1 = [1]
m = 1
nums2 = []
n = 0
Solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]

# Example 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
Solution.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1]