class Solution:
    def countRangeSum(self,nums,lower,upper):
        sums,ans=[0],[0]
        for x in nums:sums.append(sums[-1]+x)
        def merge_sort(l,r):
            if l>=r:return
            mid=(l+r)//2
            merge_sort(l,mid)
            merge_sort(mid+1,r)
            j=k=mid+1
            for i in range(l,mid+1):
                while j<=r and sums[j]-sums[i]<lower:j+=1
                while k<=r and sums[k]-sums[i]<=upper:k+=1
                ans[0]+=k-j
            sums[l:r+1]=sorted(sums[l:r+1])
        merge_sort(0,len(sums)-1)
        return ans[0]

