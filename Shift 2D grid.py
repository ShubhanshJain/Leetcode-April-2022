class Solution(object):
    def shiftGrid(self, grid, k):
        col=len(grid[0])
        nums=sum(grid,[])        
        k = k % len(nums)
        move=len(nums)-k
        ans=grid
        count=0
        nums = nums[move:] + nums[:move]
        for i in range(0,len(nums),col):
            ans[count]=nums[i:i+col]
            count+=1
        return ans