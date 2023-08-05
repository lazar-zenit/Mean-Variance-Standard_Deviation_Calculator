import numpy as np


   
#we can do all calculations separately and then make it into a list and then into a matrix

#it is more streamlines to do it all within new array in function calculate()

def calculate():
    list=[0,1,2,3,4,5,6,7,8] #just delete this before putting it on Replit since it runs main.py script ehich gives list in it
    print(list)
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.') #elegant way to display errors, not using basig print function
    array=np.array(list).reshape((3,3)) #convert list into numpy array and reshape it in 3x3 matrix
    print(array)
    calculations={'mean':
                          [np.mean(array, axis=0).tolist(), #mean on axis 1 and put it in list
                           np.mean(array, axis=1).tolist(), #mean on axis 2 and put it in list
                           np.mean(array).tolist() #mean on whole array/matrix and put it in list
                           ],
                      'variance':
                          [np.var(array, axis=1).tolist(),
                           np.var(array, axis=1).tolist(),
                           np.var(array).tolist()
                           ],
                      'standard deviation':
                          [np.std(array, axis=0).tolist(),
                           np.std(array, axis=1).tolist(),
                           np.std(array).tolist()
                           ],
                      'maximum':
                          [np.max(array, axis=0).tolist(),
                           np.max(array, axis=1).tolist(),
                           np.max(array).tolist()
                           ],
                      'minimum':
                          [np.min(array, axis=0).tolist(),
                           np.min(array, axis=1).tolist(),
                           np.min(array).tolist()
                           ],
                      'sum':
                          [np.sum(array, axis=0).tolist(),
                           np.sum(array, axis=1).tolist(),
                           np.sum(array).tolist()
                           ],
                          }
    return calculations
     
output=calculate()
print(output)

