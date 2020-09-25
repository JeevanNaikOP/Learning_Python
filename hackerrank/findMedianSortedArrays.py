class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        x=len(nums1)
        mid=x//2
        if x%2==0:
            return float(nums1[mid-1]+nums1[mid])/2
        return nums1[mid]
