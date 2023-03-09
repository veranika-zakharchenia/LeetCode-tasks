def process_similarity(expected_string, actual_string):
    actual_index = 0
    expected_index = 0
    transitions = []

    while expected_index < len(expected_string):
        try:
            similar_element_index = expected_string.index(actual_string[actual_index])
            actual_string = expected_string[0:similar_element_index] + actual_string[actual_index:]
            for i in range(0, similar_element_index):
                transitions.append(f"add")
            actual_index = similar_element_index
            expected_index = similar_element_index
            break
        except ValueError:
            expected_index += 1
            if actual_index < len(actual_string) - 1:
                actual_index += 1
            transitions.append("search")

    if expected_index == len(expected_string):
        return "Not similar at all"

    while actual_index < len(actual_string):
        if actual_string[actual_index] != expected_string[expected_index]:
            transitions.append("change")
            temp = list(actual_string)
            temp[actual_index] = expected_string[expected_index]
            actual_string = "".join(temp)

        actual_index += 1
        expected_index += 1

    if len(expected_string) > len(actual_string):
        while expected_index < len(expected_string):
            transitions.append("add")
            actual_string += expected_string[expected_index]
            expected_index += 1
    if expected_index == len(expected_string) and actual_string != expected_string:
        actual_string = actual_string[:len(expected_string)]
        transitions.append("delete")

    return transitions, actual_string


if __name__ == '__main__':
    print(process_similarity("metallica", "metalica"))
