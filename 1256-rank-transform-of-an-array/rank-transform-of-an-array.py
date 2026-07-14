class Solution(object):
    def arrayRankTransform(self, arr):
        uni=sorted(list(set(arr)))
        map={}
        rank=1

        for i in uni:
            map[i]=rank
            rank+=1
        
        res=[]
        for i in arr:
            res.append(map[i])

        return res


        