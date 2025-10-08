class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def LLtraversal(head):
    temp = head
    result = []
    while temp is not None:
        result.append(temp.val)
        temp = temp.next
    return result

def countNodes(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count

def search(head, target):
    temp = head
    while temp is not None:
        if temp.val == target:
            return True
        temp = temp.next
    return False

def delete(head, target):
    if head is None:
        return head
    if head.val == target:
        return head.next
    temp = head
    while temp.next is not None:
        if temp.next.val == target:
            temp.next = temp.next.next
            break
        temp = temp.next
    return head

def update(head, old, new):
    temp = head
    while temp is not None:
        if temp.val == old:
            temp.val = new
            break
        temp = temp.next
    return head        
            
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    n1 = ListNode(nums[0])
    n2 = ListNode(nums[1])
    n3 = ListNode(nums[2])
    n1.next = n2
    n2.next = n3
    print(LLtraversal(n1))
    print(countNodes(n1))
    print(search(n1, 4))
    n1 = delete(n1, 2)
    print(LLtraversal(n1))
    n1 = update(n1, 3, 5)
    print(LLtraversal(n1))