class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        
        for word in words:
            w_set = set(word.lower())
            if w_set <= row1 or w_set <= row2 or w_set <= row3:
                result.append(word)
                
        return result