class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def addnums(self, l1, l2):
        dummy = ListNode(0)
        carry = 0
        curr = dummy
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            
            digit = total % 10
            carry = total // 10
            
            curr.next = ListNode(digit)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next

def ll(values):
    head = ListNode(values[0])
    temp = head
    for val in values[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head

def pll(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next
    
if __name__ == "__main__":
    l1 = ll([2, 4, 3])
    l2 = ll([5, 0, 4])
    
    sol = Solution()
    result = sol.addnums(l1, l2)
    print(result)
    