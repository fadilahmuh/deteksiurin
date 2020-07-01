import numpy as np

sample = np.zeros((20, 20), dtype=np.uint8)

for i in range(20):
    for n in range(20):
        sample[i,n] = (i,n)
print(sample)