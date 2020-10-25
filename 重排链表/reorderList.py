# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 超时
# 采用链表的头插法，将后面部分的节点翻转，依次进行
class Solution:
    # 头插法
    def headInsert(self, head):
        newHead = ListNode()
        while head:
            node = ListNode(head.val)
            node.next = newHead.next
            newHead.next = node
            head = head.next
        return newHead.next
    # 重排列表
    def reorderList(self, head):
        if not head:
            return
        while head.next:
            head.next = self.headInsert(head.next)
            head = head.next
        return head

#头尾交替插入
# 将链表转为数组，通过下标访问
# 重新构建链表， 节点插入的顺序为除去头节点之外的所有节点均分为前后两个部分，每次
# 插入的时候从后面部分往前的方向选一个节点插入，然后再选则前面部分的从前往后的方向
# 选一个节点插入，直到首尾相遇，结束
class Solution_2:
    def reorderList(self, head):
        list = []
        newHead = head
        while head:
            list.append(head.val)
            head = head.next
        mid = int(len(list) / 2)
        p = newHead
        length = len(list)
        for i in range(1, mid + 1):
            if i != length - i:
                first = ListNode(list[i])
                end = ListNode(list[length - i])
                p.next = end
                p = p.next
                p.next = first
                p = p.next
            else:
                node = ListNode(list[i])
                p.next = node


if __name__ == "__main__":
    test = [1,2,3,4,5]
    head = ListNode(test[0])
    list = head
    for i in range(1, len(test)):
        node = ListNode(test[i])
        list.next = node
        list = list.next
    s = Solution_2()
    s.reorderList(head)

    while head:
        print(head.val)
        head = head.next
