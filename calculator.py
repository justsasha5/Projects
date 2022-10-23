import numpy as np

def calculate(list):
    if len(list)!= 9:
        raise ValueError('List must contain 9 numbers')

    z = np.array(list).reshape(3,3)

    calc = dict()
    calc['mean']=[z.mean(axis=0), z.mean(axis=1), z.mean()]
    calc['standard deviation']=[z.std(axis=0), z.std(axis=1), z.std()]
    calc['sum']=[z.sum(axis=0), z.sum(axis=1), z.sum()]
    return calc


print (calculate([0,1,2,3,4,5,6,7,8]))
