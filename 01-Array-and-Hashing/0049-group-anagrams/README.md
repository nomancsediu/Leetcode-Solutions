# 49. Group Anagrams

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Map grouping by sorted key |
| **LeetCode** | [Open problem](https://leetcode.com/problems/group-anagrams/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

 

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

 

**Constraints:**

	- `1 <= strs.length <= 10^4`

	- `0 <= strs[i].length <= 100`

	- `strs[i]` consists of lowercase English letters.

---

## Brute Force

Compare each pair of strings and check if they are anagrams by sorting or counting, leading to O(n^2 * m log m) time where n is number of strings and m is average length.

## Intuition

If two strings are anagrams they contain the same multiset of characters, so after sorting the characters they become identical. By using the sorted string as a **canonical representation** we can place all anagrams into the same bucket via a **hash map**.

## Optimal Approach

Use a **hash map** where the key is the sorted version of each word (or a character count tuple) and the value is a list of original strings that share that key.

## Step-by-Step Algorithm

1. Initialize an empty dictionary `groups`.
2. Iterate over each string `s` in `strs`.
3. Compute its key: `key = ''.join(sorted(s))` (or a 26‑length count tuple).
4. Append `s` to `groups[key]` (create the list if the key is new).
5. After processing all strings, return `list(groups.values())` as the grouped anagrams.

## Dry Run

- Input: ["eat","tea","tan","ate","nat","bat"]
- 1. s='eat' → key='aet' → groups{'aet':['eat']}
- 2. s='tea' → key='aet' → groups{'aet':['eat','tea']}
- 3. s='tan' → key='ant' → groups{'aet':['eat','tea'],'ant':['tan']}
- 4. s='ate' → key='aet' → groups{'aet':['eat','tea','ate'],'ant':['tan']}
- 5. s='nat' → key='ant' → groups{'aet':['eat','tea','ate'],'ant':['tan','nat']}
- 6. s='bat' → key='abt' → groups{'aet':['eat','tea','ate'],'ant':['tan','nat'],'abt':['bat']}
- Return values → [["eat","tea","ate"],["tan","nat"],["bat"]]

---

## Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary mapping the canonical key to list of anagrams
        groups = {}
        for s in strs:
            # Canonical key: sorted characters of the string
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        # Return the grouped anagrams as a list of lists
        return list(groups.values())
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n * m log m)` | Sorting each of the n strings of length m dominates the runtime. |
| **Space** | `O(n * m)` | We store each string once in the hash map plus the keys, which together require linear space in total input size. |

## Edge Cases

- Empty string ""
- All strings identical
- All strings already anagrams of each other
- Very long strings (up to 100 characters)

---

## Interview Tips

- Clarify constraints and ask if sorting each string is acceptable or if a linear‑time counting approach is preferred.
- Mention alternative key representation using a 26‑element frequency tuple to achieve O(m) per string.
- Discuss handling of empty strings and why they still produce a valid key (empty string).
- Explain that order of groups and order inside each group does not matter per problem statement.

## Follow-up Questions

- Can you improve the key generation to O(m) without sorting?
- How would you adapt the solution for Unicode characters or case‑insensitive anagrams?
- What if the input size is huge and does not fit in memory?

## Key Takeaways

- Use a **canonical representation** (sorted string or frequency tuple) to identify equivalent items.
- A **hash map** is ideal for grouping items sharing the same key in linear time.
- Choosing between sorting (O(m log m)) and counting (O(m)) depends on constant factors and character set size.

## Related Problems

- Valid Anagram
- Longest Anagram Subsequence
- Group Shifted Strings
- Find All Anagrams in a String

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
