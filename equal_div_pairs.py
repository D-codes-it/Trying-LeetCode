def countPairs(nums, k):
    pairs = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                if (i * j) % k == 0:
                    pairs += 1
        
    return pairs

test = [3,2,2,1,7,8,8, 3]
k = 2
countPairs(test, k)
print(countPairs(test, k))