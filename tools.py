import numpy as np

def v2t(vector):
    transform = np.zeros((3,3))
    transform[0,0] = np.cos(vector[2])
    transform[0,1] = -np.sin(vector[2])
    transform[0,2] = vector[0]
    transform[1,0] = np.sin(vector[2])
    transform[1,1] = np.cos(vector[2])
    transform[1,2] = vector[1]
    transform[2,0] = 0
    transform[2,1] = 0
    transform[2,2] = 1

    return transform

def t2v(transform):
    vector = np.zeros((3,1))
    vector[0] = transform[0,2]
    vector[1] = transform[1,2]
    vector[2] = np.arctan2(transform[1,0], transform[0,0])

    return vector