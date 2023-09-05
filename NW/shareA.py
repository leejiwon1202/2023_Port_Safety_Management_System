import numpy as np
from multiprocessing import shared_memory


a=np.array([0,1,2,3,4])
print(a)

shm=shared_memory.SharedMemory(create=True, size=a.nbytes)
b=np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)

b[:]=a[:]
print(shm.name)
print(b)
while(1):
    print(b)
    print(shm.name)