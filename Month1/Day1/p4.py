#PROBLEM 4 - Remove duplicates from a list
list3 = [10,20,30,33,33,40,45,45,60,90,50,99,95]
length_of_list3 = len(list3)
print(length_of_list3)
for i in range(0,length_of_list3-1):
    for j in range(0,length_of_list3-1):
        if list3[i] == list3[j]:
            list3.remove(j)
            print(list3)

print("list without duplicates:", list3)