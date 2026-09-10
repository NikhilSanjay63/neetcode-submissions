class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for index,height in enumerate(heights):
            start = index
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                width = index - j
                area = h * width
                max_area = max(max_area,area)
                start = j
            stack.append((height,start))
        
        while stack:
            h,j = stack.pop()
            width = n - j
            max_area = max(max_area,(h*width))
        
        return max_area
