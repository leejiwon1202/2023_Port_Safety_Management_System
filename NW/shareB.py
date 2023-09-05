import numpy as np
from multiprocessing import shared_memory

shm= shared_memory.SharedMemory(name= 'psm_a6365a64')

x=np.ndarray((6,), dtype=np.int64, buffer=shm)
print(x)
