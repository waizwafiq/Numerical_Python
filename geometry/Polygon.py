import matplotlib.pyplot as plt
import numpy as np

def plot(*coords):
    lines_x, lines_y = [], []
    A = np.array(coords)

    #Extract x and y coordinates from coords
    x = A[:,0]
    y = A[:,1]

    #copy x and y to the fill arrays and create them
    fill_x, fill_y = [None]*len(x), [None]*len(y)
    for i in range(0,len(x)): fill_x[i] = x[i]
    for i in range(0,len(y)): fill_y[i] = y[i]
    fill_x[len(x):] = [x[0]]
    fill_y[len(y):] = [y[0]]

    #create lines array
    for i in range(0, len(x)-1):
        lines_x.append([x[i], x[i+1]])
        lines_y.append([y[i], y[i+1]])

    lines_x.append([x[len(x)-1], x[0]])
    lines_y.append([y[len(y)-1], y[0]])

    #plotting on graph
    plt.grid()
    plt.axhline(y=0, color='black', linestyle='-') #x axis
    plt.axvline(x=0, color='black', linestyle='-') #y axis

    #plot vertices
    for i,j in zip(x,y):
        plt.plot(i,j, 'r.', markersize=12.5)

    #plot edges
    for i,j in zip(lines_x,lines_y):
        plt.plot(i,j,color='r')

    #fill the area of the polygon bounded by the vertices
    plt.fill_between(fill_x, fill_y)

    plt.show()

def area(*coords):
    '''Calculates the area of polygon based on given vertices/coordinates 
       using Shoelace Theorem'''
    A = np.array(coords)

    # Extract x and y coordinates from coords
    x = A[:, 0]
    y = A[:, 1]

    #Using the shoelace formula
    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    return 0.5*np.absolute(S1-S2)

c1 = [1,3]
c2 = [3,10]
c3 = [-1,5]
c4 = [0,4]
c5 = [-3,-4]
print("Area = ",area(c1,c2,c3,c4,c5))
plot(c1,c2,c3,c4,c5)
