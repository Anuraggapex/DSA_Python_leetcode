class Solution(object):
    def sequentialDigits(self, low, high):
        ans=[]
        for i in range(1,9):
            num=i
            nxt=i+1

            while nxt <= 9:
                num=num*10+nxt

                if low<=num<=high:
                    ans.append(num)
            
                nxt+=1

        return sorted(ans)