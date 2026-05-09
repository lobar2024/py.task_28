def flatten(lst):
    result = []
    for el in lst:
        if isinstance(el, list):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

print(flatten([1, [2, [3, [4]], 5], 6]))
# [1, 2, 3, 4, 5, 6]
