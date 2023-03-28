def isthreesumavailable(nums, target):
    nums.sort()
    for index in range(0, (len(nums) - 2)):
        left = index + 1
        right = len(nums) - 1
        while left < right:
            cal_sum = nums[index] + nums[left] + nums[right]
            if cal_sum == target:
                return True
            else:
                if cal_sum > target:
                    right -= 1
                else:
                    left += 1
    return False

def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if isthreesumavailable(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()
