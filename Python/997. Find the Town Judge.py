class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        if not trust:
            return 1 if n == 1 else -1

        trusted = [0]*(n+1)

        for a,b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        return trusted.index(n-1) if (n-1) in trusted else -1

print(Solution().findJudge(1, []))
