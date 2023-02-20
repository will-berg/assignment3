"""
Solves system of equations using the chinese remainder theorem if possible.
"""
from typing import List
from algorithms.maths.gcd import gcd

def solve_chinese_remainder(nums : List[int], rems : List[int]):

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

    """
    Manual branch coverage flags
    """
    flags = [False for i in range(9)]

    if not len(nums) == len(rems):
        flags[0] = True
        print_flags(flags)
        raise Exception("nums and rems should have equal length")
    if not len(nums) > 0:
        flags[1] = True
        print_flags(flags)
        raise Exception("Lists nums and rems need to contain at least one element")
    for num in nums:
        flags[2] = True
        if not num > 1:
            flags[3] = True
            print_flags(flags)
            raise Exception("All numbers in nums needs to be > 1")
    if not _check_coprime(nums):
        flags[4] = True
        print_flags(flags)
        raise Exception("All pairs of numbers in nums are not coprime")
    k = len(nums)
    x = 1
    while True:
        flags[5] = True
        i = 0
        while i < k:
            flags[6] = True
            if x % nums[i] != rems[i]:
                flags[7] = True
                break
            i += 1
        if i == k:
            flags[8] = True
            print_flags(flags)
            return x
        x += 1

def print_flags(flags):
    coverage = 0
    for i in range(len(flags)):
        if flags[i]:
            coverage += 1
    cov_ratio = coverage / len(flags)
    print("Branch cov: ", cov_ratio)

def _check_coprime(list_to_check : List[int]):
    for ind, num in enumerate(list_to_check):
        for num2 in list_to_check[ind + 1:]:
            if gcd(num, num2) != 1:
                return False
    return True
