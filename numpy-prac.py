import numpy as np 

a = np.zeros(3)

print(a)
# array([0., 0., 0.])


print(type(a))
# numpy.ndarray

print(type(a[0]))
# numpy.float64

print(a.shape)
# (10,)

a.shape = (3, 1)
print(a)
# array([[0.], [0.], [0.]])

b = np.ones(3)
# array([1., 1., 1.])

c = np.empty(3)
# array([0., 0., 0.])

d = np.linspace(2, 10, 5) # From 2 to 10, with 5 elements
print(d)
# array([2., 4., 6., 8., 10.])
print(type(d[0]))
# np.float64

a_list = [1, 2, 3]
e = np.array([a_list])
print(e)
# array([[1, 2, 3]])
print(type(e))
# numpy.ndarray

b_list = [[1, 2, 3], [4, 5, 6]]
f = np.array([b_list])
print(f)
# array([[[1, 2, 3], [4, 5, 6]]])
print(f.shape)
# (1, 2, 3)

np.random.seed(0)
g = np.random.randint(10, size = 6)
print(g)
# array([5, 0, 3, 3, 7, 9])

print(g[0:2])
# array([5, 0])
print(g[-1])
# 9

from skimage import io

photo = io.imread('p.jpg')
type(photo)
# numpy.ndarray

print(photo.shape)
# (324, 574, 3) # (rows, cols, rgb_color_channel)

import matplotlib.pyplot as plt 
plt.imshow(photo)

import matplotlib
print(matplotlib.matplotlib_fname())

import matplotlib.rcsetup as rcsetup
print(rcsetup.all_backends)

# show image flipped
plt.imshow(photo[::-1]) # going backwards 

# columns reversed, side mirror image
plt.imshow(photo[:,::-1])

# every other row, every other col
plt.imshow(photo[::2, ::2])

photo_sin = np.sin(photo) # in-positing sin of every element of photo


print(np.sum(photo))
print(np.prod(photo))
print(np.mean(photo))
print(np.std(photo))
print(np.var(photo))
print(np.min(photo))
print(np.max(photo))
print(np.argmin(photo)) # index value
print(np.argmax(photo)) # index value

h = np.array([1, 2, 3, 4, 5])
print(h < 3)
# array([ True, True, False, False])
print( h[ h > 3 ])
# array([ 4, 5])

photo_masked = np.where(photo > 100, 255, 0) 
# if an element > 100, replace it with 255, else 0
plt.imshow(photo_masked)


c_arr = np.array([1, 2, 3, 4, 5])
d_arr = np.array([6, 7, 8, 9, 10])
print(c_arr + d_arr)
# array([ 7, 9, 11, 13, 15])
print(c_arr + 10)
# array([ 11, 12, 13, 14, 15])
print(c_arr * d_arr)
# array([ 6, 14, 24, 36, 50])
print(c_arr @ d_arr) # dot product
# 130

plt.imshow(photo[:,:,0].T) # transpose, interchanges rows & cols

np.sort(c_arr)