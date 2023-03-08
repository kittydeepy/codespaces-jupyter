#complexity:
#   Time    :   O(n)
#   Space   :   O(1)
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    test_cases = ["RACECAR", "ABBA", "TART"]
    for s in test_cases:
        print(is_palindrome(s), sep=" ")


if __name__ == "__main__":
    main()