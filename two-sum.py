from collections import defaultdict
from typing import List


class Solution:
    def value_to_indices(self, nums: List[int]):
        unique_values = defaultdict(list)
        for index, value in enumerate(nums):  # O(N)
            unique_values[value].append(index)  # O(1)
        return unique_values

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_dict = self.value_to_indices(nums)  # O(N)
        for index, value in enumerate(nums):  # O(N)
            for second_index in indices_dict[target - value]:
              if index != second_index:
                return index, second_index


if __name__ == '__main__':
  solution = Solution()
  assert (solution.twoSum([2,7,11,15], 9) == (0,1))
  assert (solution.twoSum([3,2,4], 6) == (1,2))
  assert (solution.twoSum([3,3], 6) == (0,1))
  assert (solution.twoSum([1,7,11,4,11], 11) == (1,3))
  assert (solution.twoSum([9,0], 9) == (0,1))
  print("Success!")