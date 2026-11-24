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
