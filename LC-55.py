class Solution(object):
    def canJump(self, arr):
        jump =0
        boo = False
        if len(arr) == 1 or len(arr) ==2 :
            boo = True
            return boo
        else:
            for i in range(1,len(arr)):
                jump = arr[i]
                if i+jump > len(arr)-1:
                    boo = False
                    break
                elif arr[i+jump] == arr[-1]:
                    boo = True
                    break
                else:
                    pass
            return boo


