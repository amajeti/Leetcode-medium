import numpy as np
class Solution(object):
    
    def most_frequent(self,List): 
        counter = 0
        num = List[0] 
        res = []
        for i in List: 
            curr_frequency = List.count(i) 
            if(curr_frequency> counter): 
                counter = curr_frequency 
                num = i 
                #res.append(num)

        return num
    def minDominoRotations(self, A, B):        
        max_count_num = self.most_frequent(A)
        print(max_count_num)
        l = np.array(A)
        r = np.where(l != max_count_num)[0]
        boo = []
        for num in r:
            if B[num] == max_count_num:
                boo.append(True)
            else:
                pass
        if len(boo) == len(r):
            return len(r)
        return -1
