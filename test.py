import numpy as np

arr = np.array(
    [1,2,4]
)

#print(arr,type(arr))
#print("shape of the array:",arr.shape)

arr2D = np.array([
    [1,2],
    [4,5],
    [5,7]
])


print(arr2D[0,0],arr2D[0,1]
)

print(arr2D[0,1],arr2D[1,1]
)

print(arr2D[2,0],arr2D[2,1]
)
print(arr2D, arr2D.shape)
arr3D = np.array([
    [
        [1,2,3],
        [5,8,7],
        [3,4,5]
    ],
    [
        [1,2,3],
        [5,8,7],
        [3,4,5]
],
    [
        [1,2,3],
        [5,8,7],
        [3,4,5]
]
])
#print(arr3D)
#print(arr3D[0])
#print(arr3D[0,0])
#print(arr3D[0,0,0])

arr2D = np.array([
    [2,4,5],
    [3,5,6],
    [1,2,3]
])

arr2D[0] =[4,5]
print(arr2D)

zeros=np.zeros((4,5))
print (zeros)

ones=np.ones((3,))
print (ones)

consts=np.full((3,3),9)
print(consts)

    
    

