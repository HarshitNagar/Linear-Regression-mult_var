import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt

#______________________________________________________________________________#

def create_trainingSetX():

    print('\n\nCREATING TRAINING SET X\n')

    n = int(input('enter number of features\n>'))
    m = int(input('enter number of training examples\n>'))

    f = open('featuresX.txt','w+') #create and open file
    f.truncate() #clear the file contents

    print('enter the training set..ie. values of "x"')

    #write the training set values to the features.txt file

    for i in range(0,m):
        for j in range(0,n):
            f.write('%s\t' % input('>'))
        f.write('\n')

    #print('printing using f.read')
    #return(f.read())

    f.close()



#______________________________________________________________________________#

def load_trainingSetX():

    print('\n\nLOADING TRAINING SET X\n')

    X = np.loadtxt('featuresX.txt',dtype = float)

    print('\nTRAINING SET LOADED\n')
    print(X)
    #return(trainingSet)

    '''
    [[12 23 34 45]
     [56 67 78 89]] values of vector 'X'
    '''
    return(X)
    #create_trainingSetY(len(X))
#______________________________________________________________________________#

def create_trainingSetY(m):
    print('\n\nCREATING TRAINING SET Y\n')

    #n = int(input('enter number of features\n>'))
    #m = int(input('enter number of training examples\n>'))

    g = open('featuresY.txt','w+') #create and open file
    g.truncate() #clear the file contents

    print('enter the training set..ie. values of "Y"')

    #write the training set values to the features.txt file

    for i in range(0,m):

        g.write('%s\n' % input('>'))

    #print('printing using g.read')
    #return(g.read())

    g.close()
#______________________________________________________________________________#

def load_trainingSetY():

    print('\n\nLOADING TRAINING SET Y\n')

    Y = np.loadtxt('featuresY.txt',dtype = float)

    print('\nTRAINING SET LOADED\n')
    print(Y)
    print('\n\n')
    #return(trainingSet)

    '''
    [234 654] values of vector 'Y'
    '''
    return(Y)
#______________________________________________________________________________#

def feature_scaling(mat):
    print('\nscaling matrix\n')
    m,n = mat.shape
    m = int(m) #number of rows
    n = int(n) #number of columns

    for i in range(0,n):
        avg = np.average((mat[:,i]))
        maxnum = np.nanmax((mat[:,i]))
        minnum = np.nanmin((mat[:,i]))
        for j in range(0,m):
            mat[j,i] = ( mat[j,i] - avg)/(maxnum - minnum)


    print('matrix scaled\n')
    return(mat)

#______________________________________________________________________________#


def grad_descent(X, Y, theta):
    '''
    for every X[j]
    X.transpose(Theta)
    '''
    #print(np.dot(X,theta))
    for i in range(0,n):
        print('matrix product')
        print(np.dot(X[i,:],theta))




#______________________________________________________________________________#

def sum():

    '''
    This function will be called from the function grad_descent() to calculate
    sum of derivatives

    temp =  theta(0)*X[0] +
            theta(1)*X[1] +
            theta(2)*X[2] +
            .
            .
            .
            theta(n)*X[n]



            def sumA():
                ansA = 0
                for i in range(0,M):
                    ansA += THETA0 + (THETA1 * x[i]) - y[i]
                return ansA

            def sumB():
                ansB = 0
                for i in range(0,M):
                    ansB += ( THETA0 + (THETA1 * x[i]) - y[i] ) * (x[i])
                return ansB


            temp0 = THETA0 - ( ALPHA/M )*sumA()

            temp1 = THETA1 - ( ALPHA/M )*sumB()

            THETA0 = temp0
            THETA1 = temp1

    '''



#______________________________________________________________________________#





#create_trainingSetX()
'''
remove the above line from comment if new training set is to be created
and the last line from load_trainingSetX() function
'''

X = load_trainingSetX() # to load the created training set for featuresX
Y = load_trainingSetY() # to load the created training set for featuresY
X = np.matrix(X)        # convert to numpy matrix
Y = np.matrix(Y)        # convert to numpy matrix
Y = np.transpose(Y)
m,n = X.shape
m = int(m)
n = int(n)
theta = np.zeros((1,n))
theta = np.transpose(theta)
print(theta)


X = feature_scaling(X)

Y = feature_scaling(Y)
print('\n>X')
print(X)
print('\n>Y')
print(Y)

grad_descent(X,Y,theta)
