# 题目描述
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

# 方法1 继续沿用加法，直到循环结束
# 方法2 由于只加一 ，我们只需要找出结束进位的位置，跳出循环。或者循环结束，意味着需要多一位，
# 在数组开始位置增加一位，例如[9,9] ——> [1,0,0]

class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        carry = 1
        for i in range(0, len(digits)):
            value = digits[i] + carry
            carry = value // 10
            print(carry)
            digits[i] = value % 10
        if carry != 0:
            digits.append(1)
        return digits[::-1]

class Solution_2:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    so = Solution_2()
    an = so.plusOne([9,9])
    print(an)