class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # What does this question want: wants a boolean if two strings contain a permutation of another, specifically s1 contains in s1.
        # permutation can be every positional values in the string
        # ex. abc -> cab -> bac

        # we can use a sliding window approach to build the a permutated string.
        # we'd make a hashmap and continuously add and remove values if they don't exist? maybe a hashset is better. 

        # we can look at a fixed window and slide to then end using the size of s1, however s2 is bigger, it bricks, base case.

        # we can use that 26 array to keep track of total letters. 

        ls1 = len(s1)
        ls2 = len(s2) 

        # Base case
        if ls1 > ls2:
            return False

        # initalize 
        count1 = [0] * 26 # letters
        count2 = [0] * 26 # letters
        for i in range(ls1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # inital comparison
        if count1 == count2: 
            return True
        
        # adjust array (remove first, add last), then check 
        for i in range(ls1, ls2):
            count2[ord(s2[i-ls1]) - ord('a')] -= 1
            count2[ord(s2[i]) - ord('a')] += 1

            if count1 == count2:
                return True
    
        return False
            
            


            
