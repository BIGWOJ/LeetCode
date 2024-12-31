# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        stack = []
        closed = {')': '(', ']': '[', '}': '{'}
        for bracket in s:
            #Adding to stack if bracket is opened
            if bracket in closed.values():
                stack.append(bracket)
            #If bracket is closed...
            elif bracket in closed.keys():
                #check if lastly added bracket is the correct closing one
                if stack == [] or closed[bracket] != stack.pop():
                    return False
        #Return true only if whole stack is popped
        return stack == []