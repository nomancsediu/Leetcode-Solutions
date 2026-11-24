# 290. Word Pattern

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Map bijection |
| **LeetCode** | [Open problem](https://leetcode.com/problems/word-pattern/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

	- Each letter in `pattern` maps to **exactly** one unique word in `s`.

	- Each unique word in `s` maps to **exactly** one letter in `pattern`.

	- No two letters map to the same word, and no two words map to the same letter.

 

**Example 1:**

**Input:** pattern = "abba", s = "dog cat cat dog"

**Output:** true

**Explanation:**

The bijection can be established as:

	- `'a'` maps to `"dog"`.

	- `'b'` maps to `"cat"`.

**Example 2:**

**Input:** pattern = "abba", s = "dog cat cat fish"

**Output:** false

**Example 3:**

**Input:** pattern = "aaaa", s = "dog cat cat dog"

**Output:** false

 

**Constraints:**

	- `1 <= pattern.length <= 300`

	- `pattern` contains only lower-case English letters.

	- `1 <= s.length <= 3000`

	- `s` contains only lowercase English letters and spaces `' '`.

	- `s` **does not contain** any leading or trailing spaces.

	- All the words in `s` are separated by a **single space**.

---

## Brute Force

Try every possible mapping between pattern letters and words using backtracking, which is exponential O(k^n) where k is number of distinct letters and n number of words.

## Intuition

The problem reduces to checking a **bijection** between two sequences. If we can enforce a one‑to‑one correspondence while scanning both sequences once, the answer is immediate.

## Optimal Approach

Use two **hash maps** (or a map and a set) to maintain the forward mapping pattern→word and the reverse mapping word→pattern, guaranteeing the bijection in O(n) time.

## Step-by-Step Algorithm

1. Split the string s into a list of words.
2. If the number of words differs from the length of pattern, return false.
3. Iterate over the indices, for each (char, word) pair:
4.    • If char is already in the forward map, ensure it maps to the current word; otherwise return false.
5.    • If word is already in the reverse map, ensure it maps to the current char; otherwise return false.
6.    • If both are new, insert the pair into both maps.
7. After the loop finishes, return true.

## Dry Run

- pattern='abba', s='dog cat cat dog'
- words=['dog','cat','cat','dog']
- i=0: char='a', word='dog' → add a→dog, dog→a
- i=1: char='b', word='cat' → add b→cat, cat→b
- i=2: char='b', word='cat' → forward map matches, reverse map matches
- i=3: char='a', word='dog' → forward map matches, reverse map matches
- All checks passed → true

---

## Code

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the sentence into words
        words = s.split()
        # Length mismatch means impossible
        if len(pattern) != len(words):
            return False
        # Forward mapping: char -> word, Reverse mapping: word -> char
        char_to_word = {}
        word_to_char = {}
        for ch, w in zip(pattern, words):
            # Check forward mapping
            if ch in char_to_word:
                if char_to_word[ch] != w:
                    return False
            else:
                char_to_word[ch] = w
            # Check reverse mapping
            if w in word_to_char:
                if word_to_char[w] != ch:
                    return False
            else:
                word_to_char[w] = ch
        return True
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | We scan the words once and each hash operation is O(1) on average. |
| **Space** | `O(m)` | We store at most one entry per distinct pattern character/word, where m ≤ min(|pattern|, number of words). |

## Edge Cases

- Pattern length differs from number of words
- Repeated letters mapping to different words
- Different letters mapping to the same word
- Single character pattern with multiple words

---

## Interview Tips

- Clarify that the mapping must be bijective, not just one‑way.
- Mention handling of mismatched lengths early to avoid unnecessary work.
- Explain why a second hash (or a set) is needed to detect duplicate word mappings.
- State the time and space complexities clearly.

## Follow-up Questions

- Can you solve it without using two hash maps?
- How would you modify the solution if words could be empty strings?
- What if the pattern contains characters beyond lowercase letters?

## Key Takeaways

- Use **two-way hash maps** to enforce a bijection
- Validate input sizes before processing
- Hash‑map lookups give linear‑time verification for correspondence problems

## Related Problems

- LeetCode 205 Isomorphic Strings
- LeetCode 290 Word Pattern II
- LeetCode 242 Valid Anagram
- LeetCode 567 Permutation in String

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
