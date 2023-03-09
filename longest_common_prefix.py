from typing import List


class Solution:
    def isCommonPrefix(self, strs: List[str], length: int):
        str1 = strs[0][0: length]
        i = 1
        while i < len(strs):
            if strs[i].startswith(str1) is False:
                return False
            i += 1
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_len = 1000
        for str in strs:
            min_len = min(min_len, len(str))

        low = 1
        high = min_len

        while low <= high and low <= min_len:
            middle = int((low + high) / 2)
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1

        return strs[0][0:int((low + high) / 2)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["cir","car"]))
