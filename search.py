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


# fibonacci series
x = 0
y = 1
arr = [x, y]
while ((x + y) < 1000):
    z = x + y
    arr.append(z)
    x = y
    y = z
print(arr)
# time complexity -> 0(n)

# binary search
#arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
arr = [1,2,3,4,5,6,7,8,9]
element_to_find = 4
left = 0
right = len(arr) - 1
while (left <= right):
    mid = (left + right) // 2
    if arr[mid] == element_to_find:
        print(mid)
        break
    elif arr[mid] < element_to_find:
        left = mid + 1
    elif arr[mid] > element_to_find:
        right = mid - 1

if arr[mid] != element_to_find:
    print(-1)
# time complexity -> 0(logn)


# reverse of number:
number = 34456
rev_number = 0
while(number > 0):
    # remainder(last_digit) + rev_number * 10
    rev_number = (number % 10) + (rev_number * 10)
    print(rev_number)
    number = number // 10

print("".join(rev_number))


# stack problems:
# check if parantheses are valid or not:
str = "{[]}{}{})"
bracket_dict = {
    "]": "[",
    "}": "{",
    ")": "("
}
arr = []
counter = 0
for lt in str:
    if not bracket_dict.get(lt):
        arr.append(lt)
        print(arr)
    else:
        if arr:
            if arr[-1] == bracket_dict[lt]:
                arr.pop()


# remove adjacent letters:

arr = []
str = "aabbccffefffss"
for lt in str:
    if not arr or (arr and arr[-1] != lt):
        arr.append(lt)

print("".join(arr))

# sort two sorted arrays: merge sort half:

arr1 = [1,2,3,4,5,5,6,8,8,8,499]
arr2 = [1,2,2,2,2,3,34,50]

i = 0
j = 0
k = []
counter = 0

while i < len(arr1) and j < len(arr2):
    if (arr1[i] < arr2[j]):
        k.append(arr1[i])
        i = i + 1
    else:
        k.append(arr2[j])
        j = j + 1

while i < len(arr1):
    k.append(arr1[i])
    i = i + 1

while j < len(arr2):
    k.append(arr2[j])
    j = j + 1

print(k)
