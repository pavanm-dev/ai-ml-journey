# Day 1 - Python Lists internals

## What is a python list?
- A python list is a Dynamic Data Structure, which can be increased in the run time.
- A python list will no actually store the actual data but stores the referance to the data.
- We do not need to specify the size while creating a list.
- Python lists are dynamic, the size and length of the list can be entended.

## Memory Model
- Understanding the memory model of a list in python, When an empty python list is created/initialised a memory size of 4 slots will be assigned, when the list is almost full with 4 elements then python will start adding another 4 slots or double the size of existing list which are ready to append.

- *CORRECTED* 
    - Python does not always allocate exactly 4 slots.
    - CPython uses an OverAllocation strategy.
        new_capacity = old_capacity + (old_capacity // 8) + constant
        so it grows by Approx 1.125x (not stric doubling, not fixed +4)

- *ADDED*
    - List is a contiguous block of memory (dynamic array)
    - To access index i, Python calculates:
    memory_address = base_address + (i x size_of_pointer)
    - That calculation is constant time.
    - No traversal. no loop.
    - Thats why arr[50000] is instant.

- Tried with a program (Not written from scratch, but understood the logic very well)

- CODE:
import sys # Importing the system library to get the size of the list
arr=[] # Initialising an list

for i in range(20):
    num_items=len(arr) # This will give the length of the list
    list_size=sys.getsizeof(arr) # This will give the size of the list
    print(f"Items: {num_items}, Size: {list_size} bytes")
    arr.append(i)

print(arr)

- OUTPUT:
    Items: 0, Size: 56 bytes
    Items: 1, Size: 88 bytes  
    Items: 2, Size: 88 bytes  
    Items: 3, Size: 88 bytes  
    Items: 4, Size: 88 bytes  
    Items: 5, Size: 120 bytes 
    Items: 6, Size: 120 bytes 
    Items: 7, Size: 120 bytes 
    Items: 8, Size: 120 bytes 
    Items: 10, Size: 184 bytes
    Items: 11, Size: 184 bytes
    Items: 12, Size: 184 bytes
    Items: 13, Size: 184 bytes
    Items: 14, Size: 184 bytes
    Items: 15, Size: 184 bytes
    Items: 16, Size: 184 bytes
    Items: 17, Size: 248 bytes
    Items: 18, Size: 248 bytes
    Items: 19, Size: 248 bytes
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

## Time Complexity
- So we understood the how much time taken to append a new element to the list which is on an average - O(1) which is called AMORTISED
- Append takes O(1) - Time Complexity

*ADDED*
- Most appends -> just palce value at next free slot -> O(1)
- Sometimes -> resize happens -> O(n) copy (insert(), remove(), pop(0), slicing)
- But resizing is rare
- Spread accross many operations -> average becomes O(1)
- That spreading is called AMORTIZED analysis.

## Kay Takeaways
- Python lists are Dynamic, Can store elements of different data types.
- We don't need to specify the size of the list, as it can be extended in the runtime.
- Time Complexity of appending an element to the list is O(1) - AMORTISED.
- Python will not store the element directly to the list but stores the referances of the elements.
