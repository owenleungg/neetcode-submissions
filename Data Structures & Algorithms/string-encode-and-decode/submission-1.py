class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        counter = 0

        while counter < len(s):
            j = counter
            while s[j] != "#":
                j += 1
            
            n = int(s[counter:j])
            decoded.append(s[j + 1: j + 1 + n])
            counter = j + 1 + n 
            
        return decoded