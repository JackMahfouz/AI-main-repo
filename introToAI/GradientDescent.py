import numpy as np
#points = [(2, 4), (4, 2)]
##############################
"""Data Section"""
"""Data Genrator"""
true_w = np.array([1,2,3,4,5])
d = len(true_w)
points = []
for i in range(10000):
    x = np.random.randn(d)
    y = true_w.dot(x) + np.random.randn()
    #print(x, y)
    points.append((x, y))
##############################
def F(w):
    return sum((w.dot(x) - y)**2 for x, y in points)/len(points)
def dF(w):
    return sum(2*(w.dot(x) - y)*x for x, y in points)/len(points)
def sF(w, i):
    x, y = points[i]
    return (w.dot(x) - y)**2
def sdF(w, i):
    x, y = points[i]
    return 2*(w.dot(x) - y)* x

###############################
def gradientDescent(F, dF, Dim = 2):
    w = np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = F(w)
        gradient = dF(w)
        w = w -eta * gradient
        print('itreation {}: w = {}: F(w) = {}'.format(t, w, value))
def SGD(sF, sdF, d, n):
    w= np.zeros(d)
    eta = 1
    numUpdates = 0
    for t in range(1000):
        for i in range(n):
            value = sF(w, i)
            gradient = sdF(w, i)
            numUpdates += 1
            eta = 1.0 / numUpdates
            w = w - eta*gradient
        print('itrations {} : w = {} : F(w) = {}'.format(t, w, value)) 
SGD(sF, sdF, d, len(points))
"""file is Edited by Jack M. Isaac"""
