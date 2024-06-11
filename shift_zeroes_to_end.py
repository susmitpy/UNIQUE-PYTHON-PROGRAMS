"""
Apple Interview Coding Question
Given a list of integers, without using any extra space

Task 1) Shift all zeroes to end
Task 2) Shift all zeroes to end while maintaining the order of other elements

Task 2:
# Input -
l = [1, 2, 0, 4, -1, 5, 6, 0, 0, 7, 0]
# Output -
l = [1, 2, 4, -1, 5, 6, 7, 0, 0, 0, 0]
"""

from typing import Union
l = [1, 2, 0, 4, -1, 5, 6, 0, 0, 7, 0]

def shift_by_swap(l: list[int]) -> list[int]:
    s, e = 0, len(l) - 1

    while s < e:
        if l[s] != 0:
            s += 1
            continue

        if l[e] == 0:
            e -= 1
            continue

        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1

    return l

print(shift_by_swap(l.copy()))

def get_elem_safely(l: list[int], idx: int) -> Union[int, StopIteration]:
    if idx >= len(l):
        raise StopIteration

    return l[idx]

def shift_while_maintaining_order(l: list[int], non_zero_ptr: int=0, zero_ptr: int=0) -> list[int]:
    try:
        # find the next 0
        while get_elem_safely(l, zero_ptr) != 0:
            zero_ptr += 1
            non_zero_ptr += 1

        # find the non zero elem after finding 0
        while get_elem_safely(l, non_zero_ptr) == 0:
            non_zero_ptr += 1
        
        # Swap the elements at zero and non zero pointers
        l[zero_ptr], l[non_zero_ptr] = l[non_zero_ptr], l[zero_ptr]

        return shift_while_maintaining_order(l, non_zero_ptr, zero_ptr)

    except StopIteration:
        return l
    
print(shift_while_maintaining_order(l.copy(), 0, 0))