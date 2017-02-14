>>> import numpy as np
>>> Arr = lambda txt: np.array([[float(x.strip()) for x in y.split() if x.strip() != ''] for y in txt.split(';') if y.split() != ''])
>>> A = Arr('10 0; 0 0.1')
>>> R = lambda theta: np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
>>> X = Arr('1;2')
>>> 
>>> rotated = np.dot(R(-np.pi/4), X)
>>> 
>>> transformed = np.dot(A**5, rotated)
>>> 
>>> unrotated = np.dot(R(np.pi/4), transformed)
>>> #[(3*10^5-1*10^-5)/2;(3*10^5+1*10^-5)/2]
>>> print(unrotated)
[[ 149999.999995]
 [ 150000.000005]]
