'''
Time complexity:
    best case, worst case, average case: O(nlogn)
Space complexity: O(logn)

'''
def merge(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge(left)
        merge(right)

        left_index = 0
        right_index = 0
        temp_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                nums[temp_index] = left[left_index]
                left_index += 1
            else:
                nums[temp_index] = right[right_index]
                right_index += 1
            temp_index += 1

        while left_index < len(left):
            nums[temp_index] = left[left_index]
            left_index += 1
            temp_index += 1
        while right_index < len(right):
            nums[temp_index] = right[right_index]
            right_index += 1
            temp_index += 1

if __name__ == "__main__":
    nums = [4,1,3,2,7,6,5]
    merge(nums)
    print(nums)

