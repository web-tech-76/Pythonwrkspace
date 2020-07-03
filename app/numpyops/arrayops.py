import numpy as np


def array_shape():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a.shape)
    pass


def change_array_shape():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = a.reshape(3, 2)
    print(b)
    pass


def num_array_range():
    a = np.arange(24)
    a.ndim
    a = a.reshape(2, 4, 3)
    print(a)
    pass


def check_slice():
    a = np.arange(10)
    b = slice(2, 7, 2)
    print(a[b])
    pass


def check_array_shape():
    a = np.arange(10)
    # [start:stop:step]
    b = a[2:7:2]
    print(b)
    pass
