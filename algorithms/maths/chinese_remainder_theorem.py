"""
Solves system of equations using the chinese remainder theorem if possible.
"""
from typing import List
from algorithms.maths.gcd import gcd

def solve_chinese_remainder(nums : List[int], rems : List[int], flags : List[bool]):

    """
    Computes the smallest x that satisfies the chinese remainder theorem
    for a system of equations.
    The system of equations has the form:
    x % nums[0] = rems[0]
    x % nums[1] = rems[1]
    ...
    x % nums[k - 1] = rems[k - 1]
    Where k is the number of elements in nums and rems, k > 0.
    All numbers in nums needs to be pariwise coprime otherwise an exception is raised
    returns x: the smallest value for x that satisfies the system of equations
    """

    if not len(nums) == len(rems):
        flags[0] = True
        print_flags(flags)
        raise Exception("nums and rems should have equal length")
    else:
        flags[1] = True

    if not len(nums) > 0:
        flags[2] = True
        raise Exception("Lists nums and rems need to contain at least one element")
    else:
        flags[3] = True

    for num in nums:
        flags[4] = True
        if not num > 1:
            flags[6] = True
            raise Exception("All numbers in nums needs to be > 1")
        else:
            flags[7] = True
    flags[5] = True

    if not _check_coprime(nums):
        flags[8] = True
        raise Exception("All pairs of numbers in nums are not coprime")
    else:
        flags[9] = True

    k = len(nums)
    x = 1
    while True:
        flags[10] = True
        i = 0
        while i < k:
            flags[11] = True
            if x % nums[i] != rems[i]:
                flags[13] = True
                break
            else:
                flags[14] = True
            i += 1
            flags[12] = True
        if i == k:
            flags[15] = True
            return x
        else :
            flags[16] = True
        x += 1

def _check_coprime(list_to_check : List[int]):
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            if gcd(num, num2) != 1:
                return False
    return True
