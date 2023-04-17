from collections import defaultdict
from typing import List


class Solution:
    def value_to_indices(self, nums: List[int]):  # O(N)
        unique_values = defaultdict(int)
        for index, value in enumerate(nums):  # O(N)
            unique_values[value] = index  # O(1)
        return unique_values

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        indices_dict = self.value_to_indices(nums)  # O(N)

        for first_index, first_value in enumerate(nums[:-1]):  # O(N)
            for second_index, second_value in enumerate(nums[first_index + 1:], first_index + 1):  # O(N)
                third_value = -(first_value + second_value)

                third_index = indices_dict.get(third_value)  # O(1)
                if not third_index:
                    continue

                if third_value == second_value == first_value and third_index > 2:
                    result.add((nums[first_index], nums[second_index], nums[third_index]))
                    continue

                if third_index > second_index:
                    result.add((nums[first_index], nums[second_index], nums[third_index]))
                    continue

        # sorted(N) -> O(Nlog(N))
        return sorted(list(map(list, result)))


if __name__ == '__main__':
    solution = Solution()
    assert (solution.three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
    assert (solution.three_sum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]) == [[-5, 1, 4], [-4, 0, 4],
                                                                                             [-4, 1, 3], [-2, -2, 4],
                                                                                             [-2, 1, 1], [0, 0, 0]])
    assert (solution.three_sum([-2, 1, 4, -2, 0, 4, 0, -2, 3, 1, 0]) == [[-2, -2, 4], [-2, 1, 1], [0, 0, 0]])
    assert (solution.three_sum([1, 2, -2, -1]) == [])
    assert (solution.three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
    assert (solution.three_sum([0, 0, 0]) == [[0, 0, 0]])
    assert (solution.three_sum([0, 0, 1, 0, 0, 0]) == [[0, 0, 0]])
    assert (solution.three_sum([0, 0, 1]) == [])

    print("Success!")
