
def applyOperations(nums):
    
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            continue
        
        else:
            nums[i] = 2 * nums[i]
            nums[i + 1] = 0

    zero_count = 0
    non_zero = []

    for i, num in enumerate(nums):
        if num != 0:
            non_zero.append(num)

        else:
            zero_count += 1
    
    zeros = [0] * zero_count

    return non_zero + zeros
    

test = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
applyOperations(test)
print(applyOperations(test))