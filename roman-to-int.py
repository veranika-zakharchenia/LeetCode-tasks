import re


class Solution:
    def translate(self, s: str) -> int:
        if s == "I":
            return 1
        if s == "IV":
            return 4
        if s == "V":
            return 5
        if s == "IX":
            return 9
        if s == "X":
            return 10
        if s == "XL":
            return 40
        if s == "L":
            return 50
        if s == "XC":
            return 90
        if s == "C":
            return 100
        if s == "CD":
            return 400
        if s == "D":
            return 500
        if s == "CM":
            return 900
        if s == "M":
            return 1000

    def convert_string_to_list(self, s):
        return re.findall('[a-zA-Z]', s)

    def process_double_numbers(self, s_list: list):
        i = 0
        while i < len(s_list) - 1:
            if (s_list[i] == "I" and (s_list[i+1] == "V" or s_list[i+1] == "X")) or \
                    (s_list[i] == "X" and (s_list[i+1] == "L" or s_list[i+1] == "C")) or \
                    (s_list[i] == "C" and (s_list[i+1] == "D" or s_list[i+1] == "M")):
                s_list[i] = s_list[i] + s_list[i+1]
                s_list.pop(i + 1)
            i += 1
        return s_list

    def romanToInt(self, s: str) -> int:
        s_list = self.convert_string_to_list(s)
        s_list_processed = self.process_double_numbers(s_list)
        list_result = list(map(lambda x: self.translate(x), s_list_processed))
        result = sum(list_result)
        print(result)
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    solution.romanToInt("MCMXCIV")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
