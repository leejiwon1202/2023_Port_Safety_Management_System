import numpy as np
from multiprocessing import shared_memory
import time

a=np.array([0,1,2,3,4])
print(a)

shm=shared_memory.SharedMemory(create=True, size=a.nbytes)
print(shm.name)
b=np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)

b[:]=a[:]
print(b)
i=0
while i < 5:
    print(b)
    time.sleep(2)
    b[0]=b[0]+1
    i+=1

    