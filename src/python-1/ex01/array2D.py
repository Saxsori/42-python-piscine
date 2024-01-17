import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list of lists between start and end indexes"""
    try :
        print("My Shape is : ", np.array(family).shape)
        new_family = np.array(family)[start:end]
        print("My New Shape is : ", new_family.shape)
        return new_family.tolist()
    except :
        return []

    
          
