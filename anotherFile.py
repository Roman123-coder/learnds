class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:

            return head
        
        result_head = head.next
        a = head
        b = head.next
        c = ListNode()
        while a != None and b != None:
            a.next = b.next
            b.next = a
            c.next = b
            if a.next == None:
                break
            c = a
            a = a.next
            b = a.next

        return result_head


x7 = ListNode(7)
x6 = ListNode(6, x7)
x5 = ListNode(5, x6)
x4 = ListNode(4, x5)
x3 = ListNode(3, x4)
x2 = ListNode(2, x3)
x1 = ListNode(1, x2)

obj = Solution()
graf = x1
while graf != None:
    print(graf.val, end=" ")
    graf = graf.next
print()
print("-----")
res = obj.swapPairs(x1)
while res != None:
    print(res.val, end=" ")
    res = res.next
