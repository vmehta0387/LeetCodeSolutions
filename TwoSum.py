def twoSum_nSquareComplexity(nums, target):
    
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            sum = nums[i] + nums[j]
            if target == sum:
                return [i , j]
    return []
            
def twoSum_nComplexity(nums, target):
    # Step 1: Again, create a dictionary to store numbers and their indices.
    numMap = {}
    # Step 2: During iteration over the numbers, the complement is calculated for each number.
    for i, num in enumerate(nums):
        complement = target - num
        # Step 3: It checks if the complement exists in the dictionary. If so, the indices are returned.
        if complement in numMap:
            return [numMap[complement], i]
        # Step 4: Otherwise, the current number and its index are added to the dictionary.
        numMap[num] = i
        print(numMap)
    # Step 5: If no pair sums up to the target, return an empty list.
    return []
        

nums = [2, 7 , 11 ,15]
target = 9
result = []
result = twoSum_nSquareComplexity(nums, target)
print(result)
result = twoSum_nComplexity(nums, target)
print(result)              