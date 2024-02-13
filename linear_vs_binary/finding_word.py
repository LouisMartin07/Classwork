# Linear Search
def linear_search_sorted_words(word_list, target_word):
    steps = 0
    for num in word_list:
        steps += 1
        if num == target_word:
            return(num), steps
    return -1, steps

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    steps = 0
    low_end = 0
    high_end = len(word_list) -1

    while low_end <= high_end:
        steps +=1
        middle = (low_end + high_end) // 2
        if word_list[middle] == target_word:
            return middle, steps
        elif word_list[middle] < target_word:
            low_end = middle + 1
        else:
            high_end = middle - 1
    return steps, -1

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")

