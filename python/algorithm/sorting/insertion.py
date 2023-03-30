'''
Time complexity:
    Worst case: O(n^2)
    Best case / Sorted array and inserting: O(n)
    Average Case: O(n^2)
Space complexity:
    O(n^2)

'''
def insertion(nums):
    for main_index in range(1, len(nums)):
        key = nums[main_index]
        run_index = main_index - 1
        while nums[run_index] > key and run_index >= 0:
            nums[run_index + 1] = nums[run_index]
            run_index -= 1
        nums[run_index+1] = key
    print(nums)

if __name__ == "__main__":
    nums = [3,2,1,0,5,4]
    insertion(nums)
