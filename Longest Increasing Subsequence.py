nums=list(map(int,input().strip().split()))
m=len(nums)
dp=[1]*m
maxwell=1
for i in range(1,m):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+1)
    maxwell=max(maxwell,dp[i])
print(maxwell)
