from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_char_counter_map = defaultdict(int)
    magazine_char_counter_map = defaultdict(int)

    for char in magazine:
        magazine_char_counter_map[char] += 1

    for char in ransomNote:
        if magazine_char_counter_map[char] == 0:
            return False
        magazine_char_counter_map[char] -= 1

    return True

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))