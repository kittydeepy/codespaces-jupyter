'''
Worst Case: O(n^2)
Best Case: O(n)
Average Case: O(n^2)
Space complexity worst case: O(1) auxilary
'''
def bubble(nums):
    for step in range(len(nums)):
        for j in range(0, len(nums)-step-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

if __name__ == "__main__":
    nums = [3,2,4,1,0]
    bubble(nums)
