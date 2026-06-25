class Solution(object):
    def removeOuterParentheses(self, s):
        ans=[]
        st=[]

        for i in s:
            if i=="(":
                if len(st)>0:
                    ans.append(i)
                st.append(i)
            else:
                st.pop()
                if len(st)>0:
                    ans.append(i)

        return "".join(ans)
