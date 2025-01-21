class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            word_length = len(word)
            first = 0
            last = word_length - 1
            while first <= last:
                if word[first] != word[last]:
                    break
                else:
                    first+=1
                    last-=1
            if first > last:
                return word
        return ""







        """
        for word in words:
            word_length = len(word)
            first = 0
            last = word_length - 1
            isPalindrome = True
            while first <= last:
                if word[first] != word[last]:
                    isPalindrome = False
                    break
                else:
                    first+=1
                    last-=1
            if isPalindrome:
                return word
        return ""
        """