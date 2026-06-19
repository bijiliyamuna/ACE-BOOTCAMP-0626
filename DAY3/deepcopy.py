import copy
l1=[
    [1,2,3],
    [4,5,6]]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l2[0][0]=6
print(l1)
print(l2)
