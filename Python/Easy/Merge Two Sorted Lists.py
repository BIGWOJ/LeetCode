# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# The number of nodes in both lists is in the range[0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non - decreasing order.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #Creating dummy node to starting iterating with ease and previous pointer
        dummy_node = prev = ListNode(0)
        pointer_1, pointer_2 = list1, list2

        #Iterating till pointers are not NULL
        while pointer_1 and pointer_2:
            #Comapring values and appending smaller one to the merged_list pointer
            if pointer_1.val <= pointer_2.val:
                prev.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                prev.next = pointer_2
                pointer_2 = pointer_2.next
            prev = prev.next

        #Situation when length of lists are not the same => after done iterating one list, just append rest of the list to merged
        #because rest of the list if already sorted as well
        if pointer_1:
            prev.next = pointer_1
        else:
            prev.next = pointer_2

        #Returning head of the merged list
        return dummy_node.next