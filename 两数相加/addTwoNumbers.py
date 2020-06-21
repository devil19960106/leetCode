## 题目描述:
# 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，
# 并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 思路:
# 最开始的思路有点复杂,发现考虑不周全,还是简单说一下吧,首先是对两个链表长度相同的部分进行遍历相加,
# 直到一个结束或者全部结束.如果是全部结束,就判断一下是否有进位,有就增加一个节点,没有就结束.如果是
# 一个结束,则将没有结束的剩余部分链接到和值的后面,在对和值进行处理.思路还是比较清楚的,就是没能实现
# ,可能能力还是不足.需要多多加强啊!
# 嫖的思路:
# 这个就非常简单了,不管两个链表长度怎样,我们就认为是一样长的,不足的补0,进行每一位的相加,直到两个链表
# 遍历结束,在判断是否有进位.

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = ListNode(0)
        psum = sum
        while (l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            sum.next = ListNode(value % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            sum = sum.next
        if carry != 0:
            sum.next = ListNode(1)
        return psum.next
