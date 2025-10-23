
# Unpack dictionary using while loop

emp_details = {"name":"Jack" , "age": 19 , "salary":"35000"}

emp_keys = list(emp_details.keys())

start = 0

while start < len(emp_keys):
    key = emp_keys[start]
    print(key , ":" , emp_details[key])
    start += 1



lst = ['harsha', 'ranjth', 'kiran'] 

for item in lst:
    for each in item:
        print(each)

#Bubble sort 

lst = [3,0,6,33,55,11,2,4,77,9,10,100]

for idx1 in range(len(lst)):
    for idx2 in range(idx1+1 , len(lst)):
        if lst[idx1]>lst[idx2]:
            lst[idx1], lst[idx2] = lst[idx2],lst[idx1]

print("Sorted List",lst)

                      



"""# how to unpack the dictionary using while loop

sort the list usign bubble sort"""
