import numpy as np
def score(w, x):
    return sum(np.dot(x, w))
def loss(x, y, w):
     print(score(w,x))
     res =sum( np.dot( score(w,x),y))
     print(res)
     if res >= 0:
         return 0
     else:
         return 1
w = [2,-1]
x = [[2,0],[0,2],[2,4]]
y = [1, -1, 0]
print(loss(x,y,w))