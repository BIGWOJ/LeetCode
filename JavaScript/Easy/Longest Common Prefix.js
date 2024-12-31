// Write a function to find the longest common prefix string amongst an array of strings.
//
// If there is no common prefix, return an empty string ""
// Example 1:
//
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
//
// Example 2:
//
// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
// Constraints:
//
//     1 <= strs.length <= 200
//     0 <= strs[i].length <= 200
//     strs[i] consists of only lowercase English letters.
//
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) {
        return ""
    }

    //Finding the shortest word in the list because the longest prefix maximally can be the shortest word of the list
    let shortest_word = strs.reduce((a, b) =>{
        return a.length <= b.length ? a : b;
    })

    let longest_prefix = shortest_word;
    for (let i = 0; i < shortest_word.length; i++) {
        //Iterating through all words to see if current prefix is valid, if not => shorten the prefix
        for (let word of strs) {
            if (word[i] !== longest_prefix[i]) {
                return longest_prefix.slice(0, i);
            }
        }
    }
    return longest_prefix;
}