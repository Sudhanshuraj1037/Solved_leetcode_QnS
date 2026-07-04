class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False
        
        characters = {}
        for ch in magazine:
            if ch not in characters:
                characters[ch] = 1
            else:
                characters[ch] += 1

        for ch in ransomNote:
            if ch not in characters or characters[ch] == 0:
                return False
            else:
                characters[ch] = characters[ch]-1
        
        return True