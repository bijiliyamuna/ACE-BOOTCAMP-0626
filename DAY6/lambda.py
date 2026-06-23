from functools import reduce
slist=[1,2,3,4,5,6]
def sum_ele(a):
    m=0
    for i in range(len(a)):
        m=m+a[i]
    return m
print(sum_ele(slist))
print(list(map(lambda x:x*x,slist)))
print(list(filter(lambda val: val%2==0,slist)))
print(list(filter(lambda val: val%2!=0,slist)))
print(reduce(lambda x,y:x+y,slist))
print(reduce(lambda x,y:x*y,slist))
xlist=[["abc,1"],["def",2],["mghi",5],["jkl",4]]
print(list(sorted(xlist, key =lambda x: x[1])))