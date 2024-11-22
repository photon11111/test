import numpy as np

def isEven(value):
    abs = np.abs(value)
    castedToInt = int(abs)

    if castedToInt < abs:
        return False
    
    return castedToInt & 1 == 0