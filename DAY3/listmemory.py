import sys
mylist=[None]*10
for i in range(10):
    mylist[i]=i
    print(list.__sizeof__(mylist))
    print(sys.getsizeof(mylist))
print(mylist)
