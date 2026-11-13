# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

Original
Python
 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 31 ms (beats 5.97%)  
**Memory:** 12.2 MB (beats 79.16%)  
**Submitted:** 2026-11-13T03:20:32.098Z  

```py
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        rev = 0

        if a < 0:
            return False

        while a > 0:
             d = a % 10
             rev = rev * 10 + d
             a = a//10
             
        if x == rev:
            return True
            
        else:
            return False
    

        
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)