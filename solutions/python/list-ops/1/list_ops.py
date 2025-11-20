# list_ops.py

def append(list1, list2):
    result = []
    # copy list1
    for item in list1:
        result += [item]
    # add list2
    for item in list2:
        result += [item]
    return result


def concat(lists):
    result = []
    for lst in lists:        # each element in lists
        for item in lst:     # flatten one level
            result += [item]
    return result


def filter(predicate, lst):
    result = []
    for item in lst:
        if predicate(item):
            result += [item]
    return result


def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    result = []
    for item in lst:
        result += [function(item)]
    return result


def foldl(function, lst, acc):
    result = acc
    for item in lst:                 # left fold: f(f(f(acc, x1), x2), x3)...
        result = function(result, item)
    return result


def foldr(function, lst, acc):
    result = acc
    # right fold: f(x1, f(x2, f(x3, acc)))
    # iterate backwards manually
    idx = length(lst) - 1
    while idx >= 0:
        result = function(result, lst[idx])
        idx -= 1
    return result


def reverse(lst):
    result = []
    idx = length(lst) - 1
    while idx >= 0:
        result += [lst[idx]]
        idx -= 1
    return result
