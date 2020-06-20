## 升序数组的两数之和
## 题目描述
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
## 双指针法 从数组的开始和结尾向中间靠拢
## 方法1 逐步靠拢，通过判断两数之和与目标值的大小来决定是left移动还是right移动，每次移动一个单位
## 方法2 采用二分法靠拢 如果和值比目标值小，则left移动，移动的距离在[left+1,right]的范围寻找一个值，
# 这里的目标值为target - numbers[right]（和值小了，需要变大，需要更新left值）
# 如果大，则right移动，移动的距离[left,right-1]寻找一个值,这里的目标值为target - numbers[left]。
class Solution_1:
    def twoSum(self, numbers, target):
        left = 0
        rigth = len(numbers) - 1
        while left <= rigth:
            if numbers[left] + numbers[rigth] == target:
                return [left+1, rigth+1]
            elif numbers[left] + numbers[rigth] < target:
                left += 1
            else:
                rigth -= 1

class Solution_2:
    def binary_search(self, nums, left, right, target, flag):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left if flag == True else right

    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left = self.binary_search(numbers, left+1, right, target - numbers[right], True)
            else:
                right = self.binary_search(numbers, left, right-1, target - numbers[left], False)
