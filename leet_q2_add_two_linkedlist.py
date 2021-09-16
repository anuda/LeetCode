# Definition for singly-linked list.
'''
Runtime: 203 ms, faster than 5.04% of Python online submissions for Add Two Numbers.
Memory Usage: 25.5 MB, less than 5.83% of Python online submissions for Add Two Numbers.
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_ll(val_list):
    ll = ListNode(val_list[0])
    ll_op=ll
    for i in val_list[1:]:
        temp=ListNode(i)
        ll.next=temp
        ll=temp
    return(ll_op)


import numpy as np

def return_sum(traversal_node,other_node,carry_over):
    # print('return sum')
    try:
        digit_sum = traversal_node.val+other_node.val+carry_over
    except:
        digit_sum = traversal_node.val+carry_over
    carry_over = np.floor(digit_sum/10)
    if carry_over:
        # print('inside carry over')
        digit_sum=digit_sum-10
    # print(digit_sum,carry_over)
    return(digit_sum,carry_over)

def display_ll(ll):
    val_list=[]
    val_list.append(ll.val)
    while ll.next:
        ll=ll.next
        val_list.append(ll.val)
    return(val_list)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l_output = ListNode()
        l3 = l_output
        carry_over=0
        traversal_node = l1
        other_node=l2
        digit_sum,carry_over = return_sum(traversal_node,other_node,carry_over)
        l3.val=digit_sum
        other_flag=True
        if traversal_node.next:
            pass
        else:
            traversal_node=other_node
            other_node=None
            other_flag=False
        while traversal_node.next:
            traversal_node=traversal_node.next
            if other_flag:
                other_node=other_node.next
            if other_node is None:
                other_flag=False
                # break
            # print(traversal_node.val,other_node.val)
            digit_sum,carry_over = return_sum(traversal_node,other_node,carry_over)
            temp=ListNode()
            temp.val = int(digit_sum)
            l3.next=temp
            l3=temp
            if other_flag and traversal_node.next is None:
                traversal_node=other_node
                other_node=None
                other_flag=False
                print('switched')
        
 
        if carry_over:
            print('carry_over')
            temp=ListNode()
            temp.val = int(carry_over)
            l3.next=temp
        return(l_output)

l1 = create_ll([0]) 
l2 = create_ll([7,3])

print(display_ll(l1))
print(display_ll(l2))
sol = Solution()
op = sol.addTwoNumbers(l1,l2)
print(display_ll(op))
# print(sol.addTwoNumbers(l1,l2).val)          
