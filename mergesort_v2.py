

comparision = 0

def merge_sort(list_):
    
    list_length = len(list_)
   
    if list_length == 1:
        return list_

    mid_point = list_length // 2

    left_partition = merge_sort(list_[:mid_point])
    right_partition = merge_sort(list_[mid_point:])

    return merge(left_partition, right_partition)
    


def merge(left, right):
    output = []
    i = j = 0 

    while i < len(left) and j < len(right):
    
        if left[i] < right[j]:
           
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])

            j += 1
        global comparision
        comparision += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output



in_list = [5,3,1,2,8,4,7,6]

print(merge_sort(in_list))

print(comparision)


