# mergesort

comps = 0
merge_step = 1

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

    global merge_step
    print("MERGE STEP", merge_step, ": ", left_lst + right_lst)
    merge_step += 1

    return merge(left_lst, right_lst)


def merge(left, right):

    new_lst = []
    k, l = 0, 0

    while k < len(left) and l < len(right):
        if left[k] < right[l]:
            new_lst.append(left[k])
            k += 1
        else:
            new_lst.append(right[l])
            l += 1
        global comps
        comps += 1

    new_lst.extend(left[k:])
    new_lst.extend(right[l:])
#    global merge_step
#    print("MERGE STEP", merge_step, ": ", new_lst)
#    merge_step += 1
    return new_lst


#outputs
lst = [5,3,1,2,8,4,7,6,9]

print("INPUT: ", lst, " LENGTH: ", len(lst))
sorted_lst = mergesort(lst)
print("OUTPUT: ", sorted_lst)
print("COMPARISONS: ", comps)
