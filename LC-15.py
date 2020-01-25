class Solution(object):
    def threeSum(self,nums):
        sums = []

        n = len(nums)

        for i in range(0,n-2):
            for j in range(i+1,n-1):
                    for k in range(j+1,n):
                            if nums[k]+nums[j]+nums[i] == 0:
                                li = [nums[k],nums[j],nums[i]]
                                li.sort()
                                if li in sums:
                                    pass
                                else:
                                    sums.append(li)
            li = []

        return sums


