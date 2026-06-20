def merge_sort(ls: list) -> list:
    if len(ls) <= 1:
        return ls

    middle = len(ls) // 2

    mid_left = merge_sort(ls[:middle])
    mid_right = merge_sort(ls[middle:])

    i, j = 0, 0
    result = []

    while i < len(mid_left) and j < len(mid_right):
        if mid_left[i] <= mid_right[j]:
            result.append(mid_left[i])
            i += 1
        else:
            result.append(mid_right[j])
            j += 1

    while i < len(mid_left):
        result.append(mid_left[i])
        i += 1

    while j < len(mid_right):
        result.append(mid_right[j])
        j += 1

    return result
