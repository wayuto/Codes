from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea: int = 0
        left: int = 0
        right: int = len(height) - 1
        
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            
            if currentArea > maxArea:
                maxArea = currentArea
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea


def main():
    arr = [1,8,6,2,5,3,7]
    sol = Solution()
    print(sol.maxArea(arr))

if __name__ == '__main__':
    main()