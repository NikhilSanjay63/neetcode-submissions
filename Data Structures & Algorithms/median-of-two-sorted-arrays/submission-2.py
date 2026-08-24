class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        
        m,n = len(nums1), len(nums2)
        low,high = 0, m

        while low <= high:
            partA = (low+high)//2
            partB = (m+n+1)//2 - partA

            leftX = float('-inf') if partA == 0 else nums1[partA-1]
            rightX = float('inf') if partA == m else nums1[partA]

            leftY = float('-inf') if partB == 0 else nums2[partB-1]
            rightY = float('inf') if partB == n else nums2[partB]

            if leftX <= rightY and leftY <= rightX:
                if (m+n) % 2 == 0:
                    return (max(leftX,leftY) + min(rightX,rightY))/2
                else:
                    return float(max(leftX,leftY))
            elif leftX > rightY:
                high = partA - 1
            else:
                low = partA + 1