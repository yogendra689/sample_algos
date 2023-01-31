# example: binary_search([1,2,3,4,5,6,7,8,9,10,11], 9)
# complexity : log n, logarithmic 
def binary_search(arr, element_to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        print("-------------")
        mid = (left + right)//2
        if arr[mid] == element_to_find:
            print(f"left: {left}")
            print(f"right: {right}")
            print(f"mid: {mid}")
            return mid
        elif arr[mid] < element_to_find:
            print(f"left: {left}")
            print(f"right: {right}")
            print(f"mid: {mid}")
            left = mid + 1
        else:
            print(f"left: {left}")
            print(f"right: {right}")
            print(f"mid: {mid}")
            right = mid - 1
    if arr[mid] != element_to_find:
        return -1
    

# example: ternary_seach([1,2,3,4,5,6,7,8,9,10,11], 9)
# complexity : logn/3, logarithmic 
def ternary_seach(arr, element_to_find):
    l = 0
    array_size = len(arr)
    while (array_size >= l):
        mid1 = l + (array_size - l)//3
        mid2 = array_size - (array_size - l)//3
        print("-------------")
        print(mid1)
        print(mid2)
        if arr[mid1] == element_to_find:
            return mid1
        elif arr[mid2] == element_to_find:
            return mid2
        elif element_to_find < arr[mid1]:
            array_size = mid1 - 1
        elif element_to_find > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1 
            array_size = mid2 - 1
    return -1
