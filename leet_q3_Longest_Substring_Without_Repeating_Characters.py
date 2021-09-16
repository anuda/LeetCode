class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub=[]
        max_len=0
        temp_len=0
        for i in s:
            if i in sub:
                sub=sub[sub.index(i)+1:]
            sub.append(i)
            temp_len=len(sub)
            if temp_len>max_len:
                max_len = temp_len
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring('dvdf'))
