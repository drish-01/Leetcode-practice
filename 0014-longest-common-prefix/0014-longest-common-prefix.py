class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        fw1 = strs[0]
        for i in range(len(fw1)):
            char = fw1[i]

            for j in range(len(strs)):
                otherw = strs[j]

                if i >= len(otherw) or otherw[i]!=char:
                    return fw1[:i]
        return fw1
