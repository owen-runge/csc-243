# mergesort

# imports
from math import log2, ceil
from random import randint

comps = 0
merge_step = 1
depth = 0
# create a dict that will store all the merge steps
step_dict = {}

# mergesort algorithm
# takes in a list and a depth
# sorts the list and returns it
# branches to a separate function "merge" to merge and sort sublists
def mergesort(lst,depth):

    # list length
    lst_len = len(lst)

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
    
    # append left and right lists to step_dict
    # using a try, except to format step_dict with appropriate merge step numbers
    try:
        step_dict[depth].append(left_lst)
        step_dict[depth].append(right_lst)
    except:
        step_dict[depth] = []
        step_dict[depth].append(left_lst)
        step_dict[depth].append(right_lst)

    return merge(left_lst, right_lst)

# merge function
# this function takes in two lists (left and right) and merges them to create one sorted list
# this merge function uses the iterative method
def merge(left, right):

    new_lst = []                        # new list to return
    k, l = 0, 0                         # pointers for left and right lists (k -> left, l -> right)

    while k < len(left) and l < len(right):
        if left[k] < right[l]:
            new_lst.append(left[k])
            k += 1                      # updates the pointer for the left list if the left list val is smaller than the right list val
        else:
            new_lst.append(right[l])
            l += 1                      # updates the pointer for the right list if the right list val is smaller than the left list val
        global comps                    # global variable comps
        comps += 1                      # keeps track of the number of comparisons throughout the entire sorting algorithm

    new_lst.extend(left[k:])            # extends the new list with all remaining values of the left list 
    new_lst.extend(right[l:])           # extends the new list with all the remaining values of the right list

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


# outputs
lst = []

# test list
# lst = [3,7,1,4,6,2,5]

# list sorted from 50-1
for i in range(50,0,-1):
    lst.append(i)

# list sorted from 1-50
# for i in range(1, 51):
#     lst.append(i)

# list of 50 random ints (bounds 0-100)
# for i in range(1, 51):
#     lst.append(randint(0,100))

print("INPUT: ", lst, " LENGTH: ", len(lst))

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
