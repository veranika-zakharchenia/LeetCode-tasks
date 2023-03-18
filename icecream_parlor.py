def icecreamParlor(m, arr):
    index = 0

    while len(arr) > 1:
        item = arr[0]
        intermediate_array = [index + 1]
        arr.remove(item)
        try:
            second_index = arr.index(m - item) + 1 + index
            arr.remove(m - item)
            intermediate_array.append(second_index + 1)
            return intermediate_array
        except ValueError:
            index += 1


if __name__ == '__main__':
    t = 1
    m = 9
    arr = [1, 3, 4, 6, 7, 9]
    for time in range(t):
        result = icecreamParlor(m, arr)
        print(result)
