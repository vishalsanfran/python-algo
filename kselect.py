def kselect(nums, k):
    pvt = nums[len(nums)/2]
    less = [num for num in nums if num < pvt]
    more = [num for num in nums if num > pvt]
    if k < len(less):
        return kselect(less, k)
    elif k >= len(nums) - len(more):
        return kselect(more, k - (len(nums) - len(more)))
    else:
        return pvt

nums = [4,55,-3,90,-200,33,0,27]
print nums
for i in range(len(nums)):
    print("idx {} num {}".format(i, kselect(nums, i)))
