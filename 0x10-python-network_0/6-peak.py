#!/usr/bin/python3

""" Test function find_peak """


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
