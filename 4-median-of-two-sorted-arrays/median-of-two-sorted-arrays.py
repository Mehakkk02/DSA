class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = nums1 + nums2
        merge.sort()
        n = len(merge)
        mid = n // 2
        if n % 2 != 0:
            return float(merge[mid])
        else:
            return float(merge[mid-1]+ merge[mid]) / 2.0 
        