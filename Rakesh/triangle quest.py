# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:43:18 2018
5

Sample Output

1
22
333
4444

Can you do it using only arithmetic operations, a single for loop and print statement?

@author: Rakesh
"""

for x in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (int(10**(x-1)*x+10**(x-2)*x + 10**(x-3)*x + 10**(x-4)*x + 10**(x-5)*x + 10**(x-6)*x + 10**(x-7)*x + 10**(x-8)*x + 10**(x-9)*x))
