class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S_nodash = S.replace('-', '')

        first_part = len(S_nodash) % K
        combined = []

        if first_part != 0:
            combined.append(S_nodash[:first_part])

        for i in range(first_part, len(S_nodash), K):
            combined.append(S_nodash[i:i+K])

        return '-'.join(combined).upper()