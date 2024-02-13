# Linear Search
def linear_search_last_occurrence(arr, target):
    stepper = 0
    for index in range(len(arr)-1, 0, -1):
        stepper += 1
        if arr[index] == target: 
            return index, stepper 

# Binary Search
def binary_search_last_occurrence(arr, target):
    steps = 0
    low_end = 0
    high_end = len(arr) -1
    last_index = -1

    while low_end <= high_end:
        steps +=1
        middle = (low_end + high_end) // 2
        if arr[middle] == target:
                last_index = middle
                low_end = middle + 1
        elif arr[middle] < target:
            low_end = middle + 1
        else:
            high_end = middle - 1
    return last_index, steps

# Scenario 3 Test
"""
low, high, mid
0 9 4 index4 != target, 15 is current number 
0 3 1 index == target, 10 is current number, lastindex=1, low=2
2 3 2 
3 3 3
4 3 3
"""
#sorted_occurrence_list = [5,10,10,10,10,10,10,15,20,25,30,35,40]
occurrence_list = [5, 10, 10,10,10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")