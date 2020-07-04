
def binary_search(sequence,item):
    lower = 0
    upper = len(sequence) - 1

    while lower <= upper:
        mid_index = (lower+upper) // 2
        if sequence[mid_index] == item:
            return mid_index
        elif sequence[mid_index] < item:
            lower = mid_index + 1
        else:
            upper = mid_index - 1

    return -1


sample_li = [5,9,6,23,54,68,17,32]
print(f'The sample list: {sample_li}')
sample_li.sort() # sorting is require for performing binary search.
print(f'The list after sorting: {sample_li}')

print(f'The index of "17" in sorted list using binary search: {binary_search(sample_li,17)}')
print(f'The index of "2" in sorted list using binary search: {binary_search(sample_li,2)}')