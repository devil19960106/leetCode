## 题目描述
# 给你两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
# 将这两数相加会返回一个新的链表。你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶：
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 示例：
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7

# 方法1 沿用上个题的思路，每一位进行相加，不过需要先对两个链表翻转，在进行计算，最后再将和值进行翻转。
# 方法2 使用栈先进后出的特点来进行计算，我们首先将两个链表的数据依次压入栈中，然后再依次读取，就形成
# 了我们日常的计算方式，这里需要注意一点的是由于输出是正序，需要采用头插法进行和值链表的建立。

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution_1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1tail, l2tail = None, None
        while l1:
            val = l1.val
            p = ListNode(val)
            p.next = l1tail
            l1tail = p
            l1 = l1.next
        while l2:
            val = l2.val
            p = ListNode(val)
            p.next = l2tail
            l2tail = p
            l2 = l2.next

        carry = 0
        sum = ListNode(0)
        psum = sum
        while (l1tail or l2tail):
            val1 = l1tail.val if l1tail else 0
            val2 = l2tail.val if l2tail else 0
            value = val1 + val2 + carry
            carry = value // 10
            sum.next = ListNode(value % 10)
            if l1tail:
                l1tail = l1tail.next
            if l2tail:
                l2tail = l2tail.next
            sum = sum.next
        if carry != 0:
            sum.next = ListNode(1)
        psum = psum.next
        answer = None
        while psum:
            val = psum.val
            p = ListNode(val)
            p.next = answer
            answer = p
            psum = psum.next

        return answer


class Solution_2:
    stack1, stack2 = [], []
    def push_stack(self, p, stack):
        while p:
            stack.append(p.val)
            p = p.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        self.push_stack(l1,self.stack1)
        self.push_stack(l2, self.stack2)
        sum = None
        while self.stack1 or self.stack2:
            val1 = self.stack1.pop() if self.stack1 else 0
            val2 = self.stack2.pop() if self.stack2 else 0
            value = val1 + val2 + carry
            carry = value // 10
            node = ListNode(value)
            node.next = sum
            sum = node
        if carry != 0:
            node = ListNode(1)
            node.next = sum
            sum = node
        return sum