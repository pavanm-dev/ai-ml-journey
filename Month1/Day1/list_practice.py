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
