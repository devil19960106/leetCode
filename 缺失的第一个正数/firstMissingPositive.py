# 题目描述
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
# 提示：
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

# 第一个困难的题目，困难的地方在于时间复杂度为O(n)，空间复杂度为0(1)
# 题目给的提示：Remember that O(2n) = O(n)
# 方法1：
# 所以我们可以先排序，升序排序，然后依次判断是否与没有出现的最小正整数相等，如果相等，则没有出现的最小正整数加1，
# 出现就继续遍历，直到结束，返回 时间复杂度并不满足要求，但过了。。。
# 方法2：
# 在长度为N的数组中，没有出现的最小的正整数为[1, N+1]，如果数组中的元素是从1...N，那么没出现的最小正整数为N+1；
# 反之，则为[1,N]中的一个数。我们考虑将数字大小在[1,N]范围内的数组元素放在它应该在的位置(因为数组下标从0开始，那么正确
# 的位置为nums[i] - 1)。所以我们交换下标为i和nums[i] - 1的元素。下标为nums[i] - 1 的元素是一个新的元素，我们判断它是否在
# [1,N]的范围内或者是否与nums[i]相等。交换的结束条件为下标为i的元素不在[1,N]或者与将要交换的元素相等。
# 最后，我们再次遍历数组，找到第一个不等于i + 1的数组元素，即为答案。
# 方法3：
# 第一步，我们将所有的负数消除，变成其他的正数，但需要大于N + 1(负数在题中无意义)。
# 第二步，我们将所有数值在[1,N]之间的数组元素的正确位置处的元素变成负数，表示该下标 + 1所代表的正数出现。
# 第三步，遍历数组，找到第一个为正数的位置，下标 + 1即为答案，或者都为负数，那么答案为N + 1

class Solution:
    def firstMissingPositive(self, nums):
        positive = 1
        nums = sorted(nums)
        for num in nums:
            if num <= 0:
                continue
            elif num == positive:
                positive += 1
        return positive


class Solution_2:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


class Solution_3:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = - abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

if __name__ == "__main__":
    so = Solution_2()
    an = so.firstMissingPositive([3,4,-1,1])
    print(an)