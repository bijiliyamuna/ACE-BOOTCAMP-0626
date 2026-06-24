import numpy as np
#print(np.version)
arr1 = np.array([[[1,2,3,4],[5,6,7,8],[5,6,7,8]],
                [[1,2,3,4],[5,6,7,8],[5,6,7,8]],
                [[1,2,3,4],[5,6,7,8],[5,6,7,8]]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1[2,0,1])
