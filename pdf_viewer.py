"""
There is a list of  character heights aligned by index to their letters. For example, 'a' is at index  and 'z'
is at index. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight
in assuming all letters are  wide.

Example
h = [1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5]
word = 'abc'

The heights are 1 and 3 and 1. The tallest letter 'b' is 3mm high and there are 3 letters. The hightlighted area will be
3 * 3 mm = 9 mm so the answer is 9.
"""


def pdf_viewer(h, word):
    # dict = {ord('a'): h[0], ... ord('z'): h[len(h)-1]}
    char_map = dict(zip(range(97, 123), [h[index] for index, value in enumerate(h)]))  # 'a' - 97 ... 'z' - 122
    max_value = 0
    for char in word:
        if char_map[ord(char)] >= max_value:
            max_value = char_map[ord(char)]

    return max_value * len(word)


if __name__ == '__main__':
    input_string = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7"
    str_arr = [int(e) if e.isdigit() else e for e in input_string.split(" ")]
    print(pdf_viewer(str_arr, "zaba"))
