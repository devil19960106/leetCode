# 题目描述
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

# 时间效率较高
class Solution_1:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(x) for x in list(num1)][::-1]
        num2 = [int(x) for x in list(num2)][::-1]
        sum = []
        list_len = len(num1) if len(num1) > len(num2) else len(num2)
        carry = 0
        for i in range(0, list_len):
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0
            value = val1 + val2 + carry
            carry = value // 10
            sum.append(value % 10)
        if carry != 0 :
            sum.append(1)

        return  ''.join([str(x) for x in sum[::-1]])

# 空间较低
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        sum = []
        list_len = len(num1) if len(num1) > len(num2) else len(num2)
        carry = 0
        for i in range(0, list_len):
            val1 = int(num1[i]) if i < len(num1) else 0
            val2 = int(num2[i]) if i < len(num2) else 0
            value = val1 + val2 + carry
            carry = value // 10
            sum.append(value % 10)
        if carry != 0 :
            sum.append(1)

        return  ''.join([str(x) for x in sum[::-1]])

class Solution_2:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1) - 1, len(num2) - 1
        sum = ''
        carry = 0
        while i >= 0 or j >= 0:
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            value = val1 + val2 + carry
            carry = value // 10
            sum = str(value % 10) + sum
            i,j = i - 1, j - 1
        if carry != 0:
            sum = '1' + sum
        return sum

if __name__ == "__main__":
    so = Solution_2()
    an = so.addStrings('129','56')
    print(an)