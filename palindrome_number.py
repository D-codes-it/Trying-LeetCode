class Solution(object):
    num = int(input)
    mum1 = map(int, input().split())
    num2 = list(map(int, input.split()))
    def isPalindrome(self, x):
        left = 0
        right = len(x) - 1

        while (left < right):
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1

            if left == right:
                print("true")
            else:
                print("false")

#I don't think this is quite right (attempt one)
        