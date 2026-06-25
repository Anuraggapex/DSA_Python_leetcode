class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)

        ans=[0]*n
        st=[]

        for i in range (2*n-1,-1,-1):
            while len(st)>0 and st[-1]<=nums[i%n]:
                st.pop()
            if len(st)==0:
                ans[i%n]=-1
            else:
                ans[i%n]=st[-1]

            st.append(nums[i%n])

        return ans