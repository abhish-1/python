import numpy as np
import time
size = 10_000_000
pyarr=list(range(size))
start = time.time()
sqarr=[x**2 for x in pyarr]
end = time.time()
print(end-start) #2.9173667430877686

nparr=np.array(pyarr)
start =time.time()
newnparr=nparr**2
end=time.time()
print(end-start) #0.08203530311584473
2.9173667430877686
0.08203530311584473
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr,type(arr)) #[1 2 3 4 5] <class 'numpy.ndarray'>

arr2=np.array([1,2,34,5,"apple"])
print(arr2,type(arr), arr2.dtype) #['1' '2' '34' '5' 'apple'] <class 'numpy.ndarray'> <U21 [cast entire to one type]

arr3 = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr3,type(arr),arr3.dtype,arr3.shape,arr.size)
#[[1 2 3] in case isme 4 add krte to homgonous error a jata.
#[1 2 3]
#[1 2 3]] <class 'numpy.ndarray'> int64 (3, 3)
#9 

arr4 = arr3.astype(np.float64)
print(arr4)
#[[1. 2. 3.]
#[1. 2. 3.]
#[1. 2. 3.]]

arr5 = arr3.reshape((1,9))
print(arr5) #[[1 2 3 1 2 3 1 2 3]]
[1 2 3 4 5] <class 'numpy.ndarray'>
['1' '2' '34' '5' 'apple'] <class 'numpy.ndarray'> <U21
[[1 2 3]
 [1 2 3]
 [1 2 3]] <class 'numpy.ndarray'> int64 (3, 3) 5
[[1. 2. 3.]
 [1. 2. 3.]
 [1. 2. 3.]]
[[1 2 3 1 2 3 1 2 3]]
import numpy as np
arr3 = np.array([[1,2,3],[1,2,3],[1,2,3]])
num = arr3[1][1]
print(num) #2 

arrnew = np.array([12,3,4,56,6,6])
newarr=[1,2,3]
print(arrnew[newarr]) #[ 3  4 56]
print(arrnew[arrnew>3]) #[12  4 56  6  6]
print(arrnew[1:4:2]) #[ 3 56]

# Note -> IN python lists when you slice it creates a new array and it thus occupies some memory but in numpy it is mostly called as view that is you
# actually have a copy its just a view of the same data, also if you want to copy use the .copy() funtion in numpy.

print(np.sum(arr3,axis=1)) # axis -> 0 me sum column wise print, 1 me sum row wise.

arr3D = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,4,3]]])
print(arr3D[1,1,1]) # 4 , slicing same as earlier
2
[ 3  4 56]
[12  4 56  6  6]
[ 3 56]
[6 6 6]
2
#Vectorization & Broadcasting.
arr3 = np.array([[1,2,3],[1,2,3],[1,2,3]])
arr4 = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr3+arr4)
#Both aim to make operation simple in numpy, broadcasting has 2 rules the two array must be of same dimension or one of them must be of 1, like (1*k)
# basically use your brains and think if they could be operated together someway without removing adding new.

#Mathematical operation.
#np.sum(), np.mean(), np.std(), np.min(), np.max()
# Trig: np.sin, np.cos, np.tan
# np.exp(), np.log(), np.sqrt()
# np.abs(), np.round()
[[2 4 6]
 [2 4 6]
 [2 4 6]]
 