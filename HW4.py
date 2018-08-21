import math
import random
import numpy as np
import matplotlib.pyplot as plt


def generate_target_func(n):
    res = []
    for i in range(n):
        x1 = random.uniform(-1,1)
        x2 = random.uniform(-1,1)
        y1 = math.sin(math.pi*x1)
        y2 = math.sin(math.pi*x2)
        x = np.array([x1,x2])
        y = np.array([y1,y2])
        x = x[:, np.newaxis]
        a, _, _, _ = np.linalg.lstsq(x, y, rcond=None)
        res.append(a)
    return res


result = generate_target_func(1000)
print(sum(result)/len(result))

