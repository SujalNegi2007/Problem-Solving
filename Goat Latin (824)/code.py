class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        for i in range(len(words)):
            if words[i][0].lower() in {"a","e","i","o","u"}:
                words[i] = words[i] + "ma"
            else:
                first_letter = words[i][0]
                words[i] = words[i][1:]
                words[i] = words[i] + first_letter + "ma"
            words[i] = words[i] + "a"*(i+1)
        return " ".join(words)
