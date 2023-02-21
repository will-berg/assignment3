"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""


def summarize_ranges(array):
    flags = [False for i in range(5)]
    """
    :type array: List[int]
    :rtype: List[]
    """
    res = []
    if len(array) == 1:
        flags[0] = True
        print(flags)
        return [str(array[0])]
    i = 0
    while i < len(array):
        flags[1] = True
        num = array[i]
        while i + 1 < len(array) and array[i + 1] - array[i] == 1:
            flags[2] = True
            i += 1
        if array[i] != num:
            flags[3] = True
            res.append((num, array[i]))
        else:
            flags[4] = True
            res.append((num, num))
        i += 1
    print(flags)    
    return res


if __name__ == "__main__":
    ex1 = [0, 1, 2, 4, 5, 7]
    summarize_ranges(ex1)
    ex2 =[1]
    summarize_ranges(ex2)
    
