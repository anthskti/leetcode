class Solution:

    def encode(self, strs: List[str]) -> str:
        # from list of strings, create a singular string. 

        res = ""
        for s in strs:
            res += str(len(s))+"#"+s # length+# (as space)+string
        return res

    def decode(self, s: str) -> List[str]:
        # from string to list
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            word = s[j+1 : j + 1 + length]
            res.append(word)

            i = j+1+length


        return res
