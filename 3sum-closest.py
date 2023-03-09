from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 3:
            return nums[0]

        the_closest = sum(nums[0:3])
        difference = abs(target - the_closest)
        # difference = max(nums)
        index = 0

        while index <= len(nums) - 3:
            three_sum = sum([nums[index], nums[index+1], nums[index+2]])
            temp_diff = abs(target - three_sum)
            if temp_diff == 0:
                return three_sum
            if temp_diff < difference:
                difference = temp_diff
                the_closest = three_sum

            index += 1

        return the_closest

    def count(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 3:
            return nums[0]

        nums.sort()

        the_closest = sum(nums[0:3])
        difference = abs(target - the_closest)
        # difference = max(nums)
        left = 0
        middle = length // 2
        right = len(nums) - 1

        while left <= length // 2:
            while right > length // 2:
                three_sum = sum([nums[left], nums[middle], nums[right]])
                temp_diff = abs(target - three_sum)
                if temp_diff == 0:
                    return three_sum
                if temp_diff < difference:
                    difference = temp_diff
                    the_closest = three_sum

                right -= 1

            left += 1

        return the_closest


if __name__ == '__main__':
    solution = Solution()
    print(solution.count([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
    print(solution.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
    # print(solution.threeSumClosest([1, 1, 1, 0], -100))
    # print(solution.threeSumClosest([0, 0, 0], 1))
    # print(solution.threeSumClosest([0, 1, 2], 0))
    # print(solution.threeSumClosest([-1, 2, 1, -4], 1))
