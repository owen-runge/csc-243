#######################################################################################
# two_reversal program
# Ajay, Alvaro and I worked together on this program
# this program is based on mergesort with modifications to count the number of swaps
#######################################################################################

#######################################################################################
# mergesort functions
# essentially just a mergesort algorithm but it keeps track of the number of inversions 
# (the number of matches of the two-reversal pattern)
#######################################################################################
def mergesort(arr, n):
	# we create a temporary array to store our values
    temp_arr = [0]*n
    # call the merge_sort function which will do all the work
    return merge_sort(arr, temp_arr, 0, n-1)

def merge_sort(arr, temp_arr, left, right):

	# inversions stores the total matches for each call
    inversions = 0

    # checks for base case
    if left < right:
        # calculate midpoint to divide the array into subarrays
        mid = (left + right)//2

        # recursive call for the first half
        # adds the number of inversions from the call to "inversions"
        inversions += merge_sort(arr, temp_arr, left, mid)

        # recursive call for the second half
        # adds the number of inversions from the call to "inversions"
        inversions += merge_sort(arr, temp_arr, mid + 1, right)

        # calls the merge function to sort the subarrays
        # adds the number of inversions to "inversions"
        inversions += merge(arr, temp_arr, left, mid, right)
    return inversions

#######################################################################################
# merge function
# merges the subarrays into one sorted array
# returns the number of inversions done while sorting
#######################################################################################
def merge(arr, temp_arr, left, mid, right):
    i = left	 # sets i equal to the starting index of the left subarray
    j = mid + 1  # sets j equal to the starting index of the right subarray
    k = left	 # sets k to the starting index of the sorted subarray
    inversions = 0

    # this loop runs as long as i and j are still within the bounds of their respective subarrays
    while i <= mid and j <= right:

        # an inversion will only occur if arr[i] > arr[j]
        # thus we don't want to count inversions here
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
			# inversions only occur here since this condition is for arr[i] > arr[j]
            temp_arr[k] = arr[j]
            inversions += (mid-i + 1)
            k += 1
            j += 1

	# add any remaining elements of the left and right subarrays into the temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

	# copy elements from the temporary array into the regular array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inversions


# Main #
arr = [38, 584, -200, 5, 68, -3000, 1]
n = len(arr)
result = mergesort(arr, n)
print("Number of inversions are", result)

