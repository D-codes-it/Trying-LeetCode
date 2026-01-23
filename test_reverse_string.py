# Test file provided by AI assistance (gemini)
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# --- THE TEST ---
if __name__ == "__main__":
    solution = Solution()
    
    # We create our list here
    my_data = ["p", "y", "t", "h", "o", "n"]
    
    print(f"1. Before function call: {my_data}")
    
    # We call the function. It doesn't return anything.
    solution.reverseString(my_data)
    
    # We check the original 'my_data' variable again
    print(f"2. After function call:  {my_data}")