class Solution(object):
    def missingElement(self, nums, k):
        

        l,r=0,len(nums)-1
        
        while l<r:
            mid=(l+r+1)//2
            if nums[mid]-nums[0]-mid < k: #count the number of missing from the begining to mid point
                l=mid
            else:
                r=mid-1
            
        print(nums[0])
        return nums[0]+k+l

