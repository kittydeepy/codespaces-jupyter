def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: right-index of sub-list
    """

    # Pick 3 random numbers within the range of the list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    # Return their median
    return max(min(i1, i2), min(max(i1, i2), i3))

def parition(lst, left, right):
    pivot_index = choose_pivot(left, right)
    temp = lst[right]
    lst[right] = lst[pivot_index]
    lst[pivot_index] = temp

    pivot = lst[right]
    i = left - 1

    for j in range(left, right):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j],lst[i]
    lst[i + 1], lst[right] = lst[right], lst[i + 1]  # Putting the pivot back in place
    return i + 1


def quicksort(lst, left, right):

    if left < right:
        pivot = partition(lst, left, right)

        quicksort(lst, left, pivot-1)
        quicksort(lst, pivot+1, right)
