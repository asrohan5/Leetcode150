class sol:
    def wordPattern(self, pattern: str, str_sequence: str) -> bool:
        # Split the input string on whitespace to get individual words
        words = str_sequence.split()
      
        # If the pattern length and word count are different, they don't match
        if len(pattern) != len(words):
            return False
      
        # Initialize dictionaries to store character-to-word map and word-to-character map
        char_to_word_map = {}
        word_to_char_map = {}
      
        # Iterate over the pattern and the corresponding words together
        for char, word in zip(pattern, words):
            # If the character is already mapped to a different word,
            # or the word is already mapped to a different character, return False
            if (char in char_to_word_map and char_to_word_map[char] != word) or \
               (word in word_to_char_map and word_to_char_map[word] != char):
                return False
          
            # Add the mappings to both dictionaries
            char_to_word_map[char] = word
            word_to_char_map[word] = char
      
        # If no mismatches are found, pattern and words match - return True
        return True
