# mergesort

from random import randint

#global
lst = [5,3,1,2,8,4,7,6]
comps = 0

def mergesort(lst):
    
    # list length
    lst_len = len(lst)

    # base case
    if lst_len == 1:
        return lst
    # finding midpoint
    midpoint = lst_len // 2

    # sublists
    left_lst = mergesort(lst[:midpoint])
    right_lst = mergesort(lst[midpoint:])

    return merge(left_lst, right_lst)


def merge(left, right):
    new_lst = []
    k = l = 0

    while k < len(left) and l < len(right):
        if left[k] < left[l]:
            new_lst.append(left[k])
            k += 1
        else:
            new_lst.append(right[l])
            l += 1
        global comps
        comps += 1

    new_lst.extend(left[k:])
    new_lst.extend(right[l:])
    return new_lst


#outputs
sorted_lst = mergesort(lst)
print("INPUT: ", lst, " LENGTH: ", len(lst))
print("OUTPUT: ", sorted_lst)

