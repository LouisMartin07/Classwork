# Linear Search
def linear_search_unsorted(arr, target):
    steps = 0
    for num in arr:
        steps += 1
        if num == target:
            return(num), steps
    return -1, steps

# Binary Search
def binary_search_unsorted(arr, target):
    steps = 0
    low_end = 0
    high_end = len(arr) -1

    while low_end <= high_end:
        steps +=1
        middle = (low_end + high_end) // 2
        if arr[middle] == target:
            return middle, steps
        elif arr[middle] < target:
            low_end = middle + 1
        else:
            high_end = middle - 1
    return steps, -1
            

# Scenario 1 Test
#sorted_arr = [7,10,15,18,22,30,42]
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 18
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")