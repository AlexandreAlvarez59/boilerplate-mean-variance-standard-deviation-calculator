import numpy as np

def calculate(list):
  if(len(list)<9):
    raise ValueError("List must contain nine numbers.")
  matrix = np.array(list).reshape(3,3) 

  calculations = {

###€ This one works

    'mean': [np.mean(matrix, 0).tolist(), np.mean(matrix, 1).tolist(), np.mean(matrix)],
    'variance': [np.var(matrix, 0).tolist(), np.var(matrix, 1).tolist(), np.var(matrix)],
    'standard deviation': [np.std(matrix, 0).tolist(), np.std(matrix, 1).tolist(), np.std(matrix)],
    'max': [np.max(matrix, 0).tolist(), np.max(matrix, 1).tolist(), np.max(matrix)],
    'min': [np.min(matrix, 0).tolist(), np.min(matrix, 1).tolist(), np.min(matrix)],
    'sum': [np.sum(matrix, 0).tolist(), np.sum(matrix, 1).tolist(), np.sum(matrix)]

#### This doesn't work even if it's the same output

#    'mean': [matrix.mean(0).tolist(), matrix.mean(1).tolist(), matrix.mean()],
#    'variance': [matrix.var(0).tolist(), matrix.var(1).tolist(), matrix.var()],
#    'standard_deviation': [matrix.std(0).tolist(), matrix.std(1).tolist(), matrix.std()],
#    'max': [matrix.max(0).tolist(), matrix.max(1).tolist(), matrix.max()],
#    'min': [matrix.min(0).tolist(), matrix.min(1).tolist(), matrix.min()],
#    'sum': [matrix.sum(0).tolist(), matrix.sum(1).tolist(), matrix.sum()],
 
  }
    
  return calculations


