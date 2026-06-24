import numpy as np
marks=np.array([
    [95,100,1,55,69],
    [25,45,65,77,69]
])
#print(marks[[0:1,:],marks>45])
marks[(marks>50) & (marks<=70)]=4
marks[(marks>70) & (marks<=80)]=3
print(marks)
arr1 = np.array([[1,2],[3,4]])
#arr1.flags.writeable=False
arr1[0][0]=5
print(arr1)
