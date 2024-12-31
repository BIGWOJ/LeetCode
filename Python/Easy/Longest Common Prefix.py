# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string ""
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:
#
#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.
#

class Solution:
    #1st attempt
    def longestCommonPrefix(self, strs):
        longest_prefix = ""
        if not strs:
            longest_prefix
        #The longest prefix maximally can be the shortest word of the list
        shortest_word = min(strs, key=len)
        for char in shortest_word:
            longest_prefix += char
            #Iterating through all words to see if current prefix is valid, if not => shorten the prefix
            for word in strs:
                if word.startswith(longest_prefix):
                    continue
                else:
                    longest_prefix = longest_prefix[:-1]
                    break
        return longest_prefix

    #2nd attempt - faster
    def longestCommonPrefix_2(self, strs):
        if not strs:
            return ""
        shortest_word = min(strs, key=len)
        longest_prefix = shortest_word
        for i in range(len(shortest_word)):
            for word in strs:
                if word[i] != longest_prefix[i]:
                    return longest_prefix[:i]
        return longest_prefix