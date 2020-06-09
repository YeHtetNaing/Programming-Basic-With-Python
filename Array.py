list = [1,5,2,7,8,9,200,155]
print (list[0])
print (list[5])
print (list[7])
# Total Room
print("Total room is array is",len(list))

# Array-Looping
list = [1,5,2,7,8,9,200,155]
t = (1,2,3)
for i in range(len(list)):
    print (list[i])

# Array-Total
list = [1,5,2,7,8,9,200,155]
x = 0
for i in range(len(list)):
    x = x + list[i]
    print("Total:",x)

# Array-WithIndex
list = [1,5,2,7,8,9,200,155]
for (i,item) in enumerate(list):
    print("Index :",i,"And Value :",item)
