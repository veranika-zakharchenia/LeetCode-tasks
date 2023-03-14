def is_contains_characters(base_string, string_to_find):
    unique_char = 0
    for char in string_to_find:
        if char in base_string:
            unique_char += 1
    return unique_char >= len(string_to_find)


def substr(str_arr):
    if len(str_arr) < 2:
        return 0

    initial_str = str_arr[0]
    chrs_to_find = str_arr[1]

    cursor = 0
    final_result = []
    temp_str = initial_str[cursor:]

    while cursor < len(temp_str):
        temp_str = temp_str[cursor:]
        temp_indexes = []
        for char in chrs_to_find:
            try:
                index = temp_str.index(char)
                temp_indexes.append(index)
            except ValueError:
                pass

        min_index = min(temp_indexes)
        result_str = temp_str[min_index]
        temp_index = min_index + 1
        while temp_index < len(temp_str):
            if temp_str[temp_index] in chrs_to_find:
                result_str += temp_str[temp_index]
                temp_index += 1
            else:
                if is_contains_characters(result_str, chrs_to_find):
                    final_result.append(result_str)
                break
        if result_str not in final_result and is_contains_characters(result_str, chrs_to_find):
            final_result.append(result_str)
        cursor = temp_index

    return max(final_result)


if __name__ == '__main__':
    print(substr(["aasdfghhhfdnnnddfffmmmggfd", "fgd"]))