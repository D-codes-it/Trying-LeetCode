class Solution(object):
    def reverseString(self, s):
        # REMOVED: s = ["h", "e", "l", "l", "o"] (Now it works for any input!)
        left = 0
        right = len(s) - 1

        while (left < right):
            # THE SWAP (The 3-step dance) - but in Python, we can do it in one line!
            s[left], s[right] = s[right], s[left]
            # We must move the pointers!
            left += 1
            right -= 1
        