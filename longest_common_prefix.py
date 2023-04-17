def longest_common_prefix(input_array):
    M = min(map(len, input_array))
    common_index = 0
    char_index = 0
    for char in input_array[0][:M]:       # O(M) - length of the shortest string
        for elem in input_array[1:]:      # O(N) - length of the input array
            if elem[char_index] == char:  # O(1)
                common_index += 1
            else:
                return input_array[0][:common_index]
        char_index += 1

    return input_array[0][:common_index]


if __name__ == '__main__':
    assert (longest_common_prefix(["cir", "car"]) == "c")
    assert (longest_common_prefix(["bar", "car"]) == "")
    assert (longest_common_prefix(["", "abc"]) == "")
    assert (longest_common_prefix(["aaab", "aaacd"]) == "aaa")
    print("Success!")
