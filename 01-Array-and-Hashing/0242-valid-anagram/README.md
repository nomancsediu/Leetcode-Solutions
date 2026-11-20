# 242. Valid Anagram

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Map frequency count |
| **LeetCode** | [Open problem](https://leetcode.com/problems/valid-anagram/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

 

**Constraints:**

	- `1 <= s.length, t.length <= 5 * 10^4`

	- `s` and `t` consist of lowercase English letters.

 

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## Brute Force

Sort both strings and compare them, which costs O(n log n) time and O(n) space for the sorted copies

## Intuition

If two strings are anagrams, they contain exactly the same characters with the same multiplicities. By counting how many times each character appears in **s** and decrementing with **t**, any mismatch reveals a non‑anagram

## Optimal Approach

Use a **hash map** (or a fixed‑size array for lowercase letters) to store character frequencies, then verify that all counts return to zero

## Step-by-Step Algorithm

1. Initialize an empty dictionary (or a length‑26 list) called **freq**
2. Iterate over each character **c** in **s** and increment **freq[c]**
3. Iterate over each character **c** in **t** and decrement **freq[c]**; if a count becomes negative, return false early
4. After processing both strings, check that all values in **freq** are zero; if so, return true

## Dry Run

- s = "anagram", t = "nagaram"
- freq after s: {a:3, n:1, g:1, r:1, m:1}
- process t: decrement a→2, n→0, g→0, a→1, r→0, a→0, m→0
- All counts are zero → return true

---

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        # Use a fixed-size list for lowercase letters
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            idx = ord(ch) - base
            freq[idx] -= 1
            if freq[idx] < 0:
                return False  # early exit
        # All counts should be zero
        return all(v == 0 for v in freq)
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | We scan each string once |
| **Space** | `O(1)` | The alphabet size is fixed (26 lowercase letters), so the frequency table size is constant |

## Edge Cases

- Different lengths should immediately return false
- One string empty and the other not (though constraints forbid empty)
- All characters identical, e.g., "aaaa" vs "aaaa"
- Strings with characters not in 'a'-'z' for the Unicode follow‑up

---

## Interview Tips

- Clarify constraints (only lowercase letters?) before choosing a fixed array vs a dict
- Mention early‑exit when a count goes negative to improve constant factors
- Discuss trade‑offs between sorting and counting approaches
- If asked, explain how to extend to Unicode by using a hash map instead of a fixed array

## Follow-up Questions

- How would you handle Unicode or arbitrary character sets?
- Can you solve it in place without extra space?
- What if the strings are extremely long and you need to stream them?

## Key Takeaways

- **Frequency counting** with a hash map or array is a common way to compare multisets
- When the domain size is bounded, you can achieve **O(1) space**
- Early termination on mismatch can save work

## Related Problems

- Valid Palindrome
- Longest Anagram Substring
- Group Anagrams
- Find the Difference of Two Arrays

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
