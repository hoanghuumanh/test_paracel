class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(list(s))
        t = sorted(list(t))
        if t == s :
            return True
        else :
            return False