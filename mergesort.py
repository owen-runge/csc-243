# mergesort

# imports
from math import log2, ceil

comps = 0
merge_step = 1
depth = 0
# create a dict that will store all the merge steps
step_dict = {}

def mergesort(lst,depth):
    # import pdb
    # pdb.set_trace()
    # list length
    lst_len = len(lst)

    # formatting the dictionary
    # format_dict(lst)

    # base case
    if lst_len == 1:
        return lst
    # finding midpoint
    midpoint = lst_len // 2

    #update depth
    depth += 1

    # sublists
    left_lst = mergesort(lst[:midpoint],depth)
    right_lst = mergesort(lst[midpoint:],depth)
    
    # extend step_dict with the left and right lists
    # step_dict[full_lst_depth - depth + 1].append(left_lst)
    # step_dict[full_lst_depth - depth + 1].append(right_lst)
    try:
        step_dict[depth].append(left_lst)
        step_dict[depth].append(right_lst)
    except:
        step_dict[depth] = []
        step_dict[depth].append(left_lst)
        step_dict[depth].append(right_lst)

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

    return new_lst


# format dict function
# takes an empty dict, calculates height, and makes key value pairs:
# key: all natural numbers from 1 to the depth of the tree
# value: an empty list, for each key
def format_dict(lst):
    
    # list length
    lst_len = len(lst)
    print(lst_len)

    tree_height = ceil(log2(lst_len))

    for i in range(1,tree_height+1):
        step_dict[i] = []

# # function to find the tree height
# def find_height(lst, len):

#     # find tree height using log2 and ceiling
#     tree_height = ceil(log2(len))

#     return tree_height

#outputs
# lst = [5,3,1,2,8,4,7,6,9]
lst = [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

print("INPUT: ", lst, " LENGTH: ", len(lst))
# format_dict(lst)
# print(step_dict)

# find length of the full list
full_lst_len = len(lst)

# find the depth of the tree of the full list
depth = ceil(log2(full_lst_len))

# calls the mergesort function
# final sorted list is stored as sorted_lst
sorted_lst = mergesort(lst,0)

# printing the dictionary
# i: keys && j: values
for i,j in step_dict.items():
    if i == depth:
        continue                                # makes it such that it doesn't print all the singleton arrays
    print("MERGE STEP {0}: {1}".format(i+1,j))  # formatted print; i+1 is so that the steps are numbered correctly
print("MERGE STEP 1: {}".format(sorted_lst))    # prints the final, sorted array as MERGE STEP 1
print("COMPARISONS: ", comps)                   # prints the number of comparisons at the end
