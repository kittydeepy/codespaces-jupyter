def bubble(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

if __name__ == "__main__":
    nums = [3,2,4,1,0]
    bubble(nums)