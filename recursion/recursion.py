case_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def sum(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum(nums[1:])
    

print(f"List: {case_list}")
print(f"Sum: {sum(case_list)}")

def count_elem_in_list(list):
    if len(list) == 1:
        return 1
    else:
        return 1 + count_elem_in_list(list[1:])

print(f"The list contains {count_elem_in_list(case_list)} elements")

def higher_value(list):
    current = list[0]

    if len(list) == 1:
        return current
    
    if current > list[1]:
         list[1] = current
    return higher_value(list[1:])

print(f"The higher value is {higher_value(case_list)}")

def binary_search(list, num):
    size = len(list)
    
    guess_index = size // 2

    if size == 1 and num != list[guess_index]:
        return 
    
    if num == list[guess_index]:
        return guess_index
    elif num < list[guess_index]:
        return binary_search(list[:guess_index], num)
    else:
        result = binary_search(list[guess_index+1:], num)
        return result + len(list[:guess_index+1]) if result != None else None

print(f"Index of 5: {binary_search(case_list, 9)}")
print(f"Index of 5: {binary_search(case_list, 15)}")
print(f"Index of 5: {binary_search(case_list, 16)}")
print(f"Index of 5: {binary_search(case_list, 1)}")
    