//Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
//
//An input string is valid if:
//
//    Open brackets must be brackets by the same type of brackets.
//    Open brackets must be brackets in the correct order.
//    Every close bracket has a corresponding open bracket of the same type.
//
//Example 1:
//Input: s = "()"
//Output: true
//
//Example 2:
//Input: s = "()[]{}"
//Output: true
//
//Example 3:
//Input: s = "(]"
//Output: false
//
//Example 4:
//Input: s = "([])"
//Output: true
//
//Constraints:
//1 <= s.length <= 104
//s consists of parentheses only '()[]{}'.

var isValid = function(s) {
    let stack = [];
    let brackets = {')': '(', ']': '[', '}': '{'};
    for (let bracket of s) {
        //Adding to stack if bracket is opened
        if (Object.values(brackets).includes(bracket)) {
            stack.push(bracket);
        }
        //If bracket it closed...
        else if (Object.keys(brackets).includes(bracket)) {
            //check if lastly added bracket is the correct closing one
            if (stack.length === 0 || stack.pop() !== brackets[bracket]) {
                return false;
            }
        }
    }
    //Return true only if whole stack is popped
    return stack.length === 0;
}