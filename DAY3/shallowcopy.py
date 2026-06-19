import copy
l1=[
    [1,2,3],
    [4,5,6]]
l2=copy.copy(l1)
print(l1)
print(l2)
l2[0][0]=6
print(l1)
print(l2)
l3=[7,8,9]
l4=copy.copy(l3)
print(l3)
print(l4)
l4[2]=10
print(l3)
print(l4)