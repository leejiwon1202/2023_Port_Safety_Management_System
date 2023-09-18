import numpy as np
from multiprocessing import shared_memory
a=np.array([0,1,2,3,4])
shm= shared_memory.SharedMemory(name= 'wnsm_b3352210')

x=np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)

print(x)