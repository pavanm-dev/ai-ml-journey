#arr=[] #Creating a list
#for i in range(5):
#    arr.append(i) # Using 5 iterations to fill the list
#print(arr)
#print ("First Element - ", arr[0])
##length_of_list = len(arr) - This is Unnecesary
##print ("Last Element - ", arr[length_of_list - 1])
#print ("last Element - ", arr[-1])
#arr.pop(1)
#print(arr)
#arr.insert(1,27)
#print(arr)
#index_of_an_element = arr.index(27)
#print ("index of the element 27 is - ", index_of_an_element)

# Day 1 - List Practice

arr = []

#append 5 number
for i in range(5):
    arr.append(i)

print("Initial List:", arr)

# Access elements
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Pop last element
remove_last = arr.pop()
print("After pop():", arr)
print("Removed element:", remove_last)

# Insert at index 1
arr.insert(1,27)
print("After insert(1,27):", arr)

# Find index
index_of_27 = arr.index(27)
print("Index of 27:", index_of_27)

print("Final List:", arr)
print("-----------------------------------")

#PROBLEM 1 - Reverse a list without using [::-1]
list1 = [10,20,30,33,33,40,45,45,60,90,50,99,95]
#length_of_list = len(list1)
#for i in range(length_of_list):
#    print("Before pop:", list1)
#    remove_last = list1.pop()
#    print("Last removed element: ", remove_last)
#    list1.insert(i,remove_last)
#    print("After insert:", list1)

#print("Final List", list1)

reversed_list = []
#for item in list1:
#    reversed_list.insert(0, item)

#print ("Reversed: ", reversed_list)

#OR
# Because range() excludes the stop value, we must use -1 to ensure index 0 is included.
for f in range(len(list1) -1, -1, -1):
    reversed_list.append(list1[f])
print ("Reversed: ", reversed_list)

print('------------------------------------')

#PROBLEM 2 - Find maximum number manually (no max())
list2 = [10,20,30,33,33,40,45,45,60,90,50,99,95]
def find_max(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest
print("Maximum number in the list:", find_max(list2))

print('------------------------------------')

#PROBLEM 3 - Count occurrences of a number
list3 = [10,20,30,33,33,40,33,45,45,60,90,50,99,95]
count = 0
target = 33

for item in list3:
    if item == target:
        count += 1

print("Occurences: " , count)
print('------------------------------------')

#PROBLEM 4 - Remove duplicates from a list
list4 = [10,20,30,33,33,40,45,45,60,90,50,99,95]
unique_list = []

for item in list4:
    if item not in unique_list:
        unique_list.append(item)

print("Without Duplicates: ", unique_list)

print('------------------------------------')

#PROBLEM 5 - Sum all elements without sum()
list5 = [10,20,30,33,33,40,45,45,60,90,50,99,95]
total = 0
for k in list5:    
    total = total + k
print("Sum of numbers in the list: ", total)

# PROBLEM 6 - Second Largest Element (Without Sorting)
list6 = [5,5,5,5]

def second_largest(nums):
    second = largest = nums[0]
    for item in nums:
        if item > largest:
            second = largest
            largest = item
        elif item > second and item != largest:
            second = item
    return second

print("Second largest number in the list: ", second_largest(list6))