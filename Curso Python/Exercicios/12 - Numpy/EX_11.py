import numpy as np

def concate_array(arr1, arr2, arr3):
    if arr1.shape != arr2.shape or arr1.shape != arr3.shape:
        raise Exception("Formatos Diferentes")
    
    return np.concatenate((arr1, arr2, arr3))

arrr = np.array([1, 2, 3])
arrr2= np.array([1, 2, 3])
arrr3 = np.array([1, 2, 3])
print(concate_array(arrr, arrr2, arrr3))
      