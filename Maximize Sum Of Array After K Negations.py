def max_arr(nums,k):
    n=len(nums)
    nums.sort()
    for i in range(n):
        if nums[i]<0 and k>0:
            nums[i]-=nums[i]
            k-=1

    if k%2==1:
        nums.sort()
        nums[0]=-nums[0]
    return sum(nums) 


nums=[4,2,3]
k=1
print(max_arr(nums,k))
