# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # go through every node and add them up
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tens = (l1.val + l2.val) // 10
        digit = (l1.val + l2.val) % 10
        
        result = ListNode(val=digit)
        start = result
        while l1.next!=None or l2.next!=None:
            # in case that one linknode is longer than the other 
            if (l1.next == None): 
                l1val = 0
                l2val = l2.next.val
                l2 = l2.next
            elif (l2.next == None): 
                l2val = 0
                l1val = l1.next.val
                l1=l1.next
            else:
                l1val = l1.next.val
                l2val = l2.next.val
                l1 = l1.next
                l2 = l2.next
            # calculate the tens, digit
            add = (l1val + l2val) + tens
            tens = add // 10
            digit = add % 10
            nextNode = ListNode(val=digit)
            # move to next
            result.next = nextNode
            result = result.next
        # if there is still number left in the tens
        if tens > 0:
            nextNode = ListNode(val=tens)
            result.next = nextNode
            result = result.next
        return start

# recursion may also works nicely