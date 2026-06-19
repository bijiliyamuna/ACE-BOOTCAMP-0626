m1=[
    [1,1,1],
    [2,2,2],
    [3,3,3]
]
for i in m1:
    print(i)
m2=[
    [4,4,4],
    [5,5,5],
    [6,6,6]
]
for i in m2:
    print(i)

m3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=m1[i][j]+m2[i][j]
for r in m3:
    print(r)
