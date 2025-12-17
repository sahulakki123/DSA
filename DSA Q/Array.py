def remove_duplicate(nums):
    nums = set(nums)
    nums = list(nums)
    nums = nums.sort()
    
li =[1,2,3,4,5,6,7,8,9,10]
ans = remove_duplicate(li)
print(ans)
