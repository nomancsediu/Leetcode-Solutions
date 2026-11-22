# 205. Isomorphic Strings

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Map mapping |
| **LeetCode** | [Open problem](https://leetcode.com/problems/isomorphic-strings/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

**Explanation:**

The strings `s` and `t` can be made identical by:

	- Mapping `'e'` to `'a'`.

	- Mapping `'g'` to `'d'`.

**Example 2:**

**Input:** s = "f11", t = "b23"

**Output:** false

**Explanation:**

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

**Example 3:**

**Input:** s = "paper", t = "title"

**Output:** true

 

**Constraints:**

	- `1 <= s.length <= 5 * 10^4`

	- `t.length == s.length`

	- `s` and `t` consist of any valid ascii character.

---

## Brute Force

Compare every character of s with every character of t using nested loops to try all possible bijections, which is O(n^2) and impractical.

## Intuition

If two strings are isomorphic, each character in s must consistently map to a single character in t, and no two different characters in s can map to the same character in t. **Maintaining two hash maps**—one for s→t and one for t→s—captures this bidirectional constraint in linear time.

## Optimal Approach

Use **two hash maps** to record the first‑seen index (or direct mapping) of each character in both strings and ensure the patterns of indices match throughout the traversal.

## Step-by-Step Algorithm

1. Initialize two empty dictionaries: map_s_to_t and map_t_to_s.
2. Iterate over the strings simultaneously by index.
3. For each pair (c1, c2), if c1 is already in map_s_to_t, check that map_s_to_t[c1] == c2; otherwise return false.
4. Similarly, if c2 is already in map_t_to_s, verify map_t_to_s[c2] == c1; otherwise return false.
5. If both checks pass, record the mapping: map_s_to_t[c1] = c2 and map_t_to_s[c2] = c1.
6. After the loop finishes, return true.

## Dry Run

- s = "egg", t = "add"
- i=0: c1='e', c2='a' -> not in maps, add e→a and a→e
- i=1: c1='g', c2='d' -> not in maps, add g→d and d→g
- i=2: c1='g', c2='d' -> e maps check passes (g→d matches), a maps check passes (d→g matches)
- End of loop → return true

---

## Code

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Quick length check (optional, constraints guarantee equal length)
        if len(s) != len(t):
            return False
        map_s_to_t = {}
        map_t_to_s = {}
        for c1, c2 in zip(s, t):
            # Check forward mapping
            if c1 in map_s_to_t:
                if map_s_to_t[c1] != c2:
                    return False
            else:
                map_s_to_t[c1] = c2
            # Check reverse mapping
            if c2 in map_t_to_s:
                if map_t_to_s[c2] != c1:
                    return False
            else:
                map_t_to_s[c2] = c1
        return True
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each character is processed once with O(1) dictionary operations. |
| **Space** | `O(min(n, Σ))` | At most one entry per distinct character in each string, bounded by the smaller of string length and character set size. |

## Edge Cases

- Single‑character strings
- Strings with repeated characters mapping to themselves
- Strings containing all possible ASCII characters

---

## Interview Tips

- Clarify that the mapping must be bijective (one‑to‑one) and order matters.
- Mention early exit when lengths differ, even though constraints guarantee equal length.
- Explain why a single dictionary is insufficient and why a second reverse map prevents false positives.

## Follow-up Questions

- Can you solve it using only one hash map and a set?
- How would you adapt the solution if the strings were extremely long and you had memory constraints?

## Key Takeaways

- **Bidirectional hash maps** enforce one‑to‑one character correspondence.
- Mapping based on **first occurrence index** is an alternative to explicit dictionaries.

## Related Problems

- LeetCode 205. Isomorphic Strings
- LeetCode 242. Valid Anagram
- LeetCode 290. Word Pattern
- LeetCode 859. Buddy Strings

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
