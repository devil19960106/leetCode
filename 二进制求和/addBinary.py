# 题目描述
# 给你两个二进制字符串，返回它们的和（用二进制表示）。输入为空字符串且只包含数字1和0。
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 方法1 将字符串转成数组在翻转，按二进制加法进行计算，将结果保存为数组，最后在翻转就行了。

class Solution_1:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)[::-1]
        b = list(b)[::-1]
        sum = []
        carry = 0
        list_len = len(a) if len(a) >= len(b) else len(b)
        for i in range(0, list_len):
            if i < len(a):
                val1 = int(a[i])
            else:
                val1 = 0
            if i < len(b):
                val2 = int(b[i])
            else:
                val2 = 0
            value = val1 + val2 + carry
            carry = value // 2
            sum.append(str(value % 2))
        if carry != 0:
            sum.append(str(1))
        sum = sum[::-1]
        return ''.join(sum)

class Solution_2:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        sum = ''
        carry = 0
        list_len = len(a) if len(a) >= len(b) else len(b)
        for i in range(0, list_len):
            val1 = int(a[i]) if i < len(a) else 0
            val2 = int(b[i]) if i < len(b) else 0
            value = val1 + val2 + carry
            carry = value // 2
            sum += str(value % 2)
        if carry != 0:
            sum += str(1)

        return ''.join(sum[::-1])

class Solution_3:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a,2) + int(b,2)
        return bin(c).replace('0b', '')


if __name__ == "__main__":
    so = Solution_2()
    a = input("a is :")
    b = input("b is :")
    sum = so.addBinary(a,b)
    print(sum)

