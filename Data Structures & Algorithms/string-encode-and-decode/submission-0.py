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

            counter = j + 1
            # loop n times
            new_string = ""
            for k in range(n):
                new_string += s[counter]
                counter += 1
            decoded.append(new_string)
            
        return decoded