'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

https://leetcode.com/problems/word-break/
'''

'''
The idea here is, cache array contains the (end index+1) of all prefixes of input string, which can be broken into words from the given dictionary.

For any prefix, it is composable by dictionary words, if and only if, itself takes the format of (a composable prefix) + (a dictionary word)
'''
def word_break(s, d):
  dp = []
  for i in range(len(s)):
    if s[:i+1] in d:
      dp.append(i+1)
    else:
      for j in dp:
        if s[j:i+1] in d:
          dp.append(i+1)
          break
  return dp[-1] == len(s)
