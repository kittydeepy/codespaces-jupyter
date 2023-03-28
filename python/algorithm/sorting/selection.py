"""
Time complexity: O(n^2)
Space complexity: O(1)
"""
def selection_sort(nums):
    for main_index in range(len(nums)):
        min_index = main_index
        for run_index in range(main_index+1, len(nums)):
            if  nums[min_index] > nums[run_index]:
                min_index = run_index
        temp = nums[main_index]
        nums[main_index] = nums[min_index]
        nums[min_index] = temp
    print(nums)


if __name__ == "__main__":
    arr = [1,4,2,5]
    selection_sort(arr)
