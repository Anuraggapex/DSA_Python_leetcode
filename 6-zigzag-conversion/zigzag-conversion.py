class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows>=len(s): 
            return s
        
        rows=[""]*numRows
        curr, direction=0,1
        
        for char in s:
            rows[curr] += char
            if curr==0:direction=1
            elif curr==numRows- 1:direction= -1
            curr += direction
            
        return "".join(rows)