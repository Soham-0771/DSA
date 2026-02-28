class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build LPS (longest prefix suffix) array
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j

        # KMP search
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1

        return -1
