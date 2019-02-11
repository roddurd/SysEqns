# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 12:16:28 2019

@author: roddu
"""

"""

−7x−10y=45
−3x−5y=25
​	
​	

"""
import numpy as np
numEqns = int(input("Enter the number of eqns: "))
numVars = int(input("Enter the number of variables: "))

equations = np.zeros((numEqns, numVars))
answers = np.zeros(numEqns)
for i in range(numEqns):
    for j in range(numVars):
        equations[i, j] = int(input("Enter coefficient of variable %i in eqn %i: " % (j+1, i+1)))
    answers[i] = int(input("Enter answer to equation %i: " % (i+1)))
    
    
#solvedVariables = np.zeros(numVars)
#inverse = np.linalg.pinv(equations)
#solvedVariables = np.matmul(inverse, answers)
solvedVariables = np.linalg.solve(equations, answers)

for x in range(len(answers)):
    print("Variable %i is: %i" % (x+1,solvedVariables[x]))
        
        

        
      
   
   

