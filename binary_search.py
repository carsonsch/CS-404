def binary_search(lst, target, left=0, right=None):
    if right is None:
        right = len(lst) - 1

    if left > right:
        return -1

    mid = (right + left) // 2
    mid_elem = lst[mid]

    if mid_elem == target:
        return mid
    elif mid_elem < target:
        return binary_search(lst, target, left=mid + 1, right=right)
    elif mid_elem > target:
        return binary_search(lst, target, left=left, right=mid - 1)
