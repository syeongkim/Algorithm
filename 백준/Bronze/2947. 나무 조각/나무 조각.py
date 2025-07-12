nums = list(map(int, input().split()))

def sorting(nums):
    for i in range(len(nums) - 1):
        if (nums[i] > nums[i+1]):
            temp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = temp
            for j in range(len(nums)):
                print(nums[j], end=' ')

while (nums != [1, 2, 3, 4, 5]):
    sorting(nums)