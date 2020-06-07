# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:47:33 2020

@author: maryf
"""
#
# A strange calculator.. only does strange functions. 
#

from functools import reduce
import random


li = [1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]

class Calculator():
    
    # 1. Sum of all items in a list using reduce.
    def sum_list(self, li):
        sum = reduce((lambda x, y: x + y), li) 
        print(sum)
        return sum
    # 2 Subtract each subsequent number from prior number in the list.
    def sub_list(self, li):
        sub = reduce((lambda x, y: x - y), li) 
        print(sub)
        return sub
    
    # 3. Square of all items in a list using map.
    def square_list(self, li):
        sq=list(map(lambda x: 2*x, li))
        print(sq)
        return sq
    
    # 4. Filter() list to only odd using lambda() 
    def odd_list(self, li):
        odd_list = list(filter(lambda x: (x%2 != 0) , li)) 
        print(odd_list)
        return(odd_list) 
        
    # 5. Filter() list to only even using lambda() 
    def even_list(self, li):
        even_list = list(filter(lambda x: (x%2 == 0) , li)) 
        print(even_list)
        return(even_list) 
    # 5. Raise a number to the power of a second number

    # 6. Return only positive values.    
    def pos(self, li):
        pos_list= list( filter((lambda x: x > 0),li ))
        print(pos_list)
        return(pos_list)

    #7. Return only negative values
    def neg(self, max=0):
        neg_list= list( filter((lambda x: x < 0),li ))
        print(neg_list)
        return(neg_list)

    #8. Random number between 1 and 100
    def rand(self, n=1):
        for i in range(n):
            yield random.randint(1, 100)
            print
        
    #9. Multiply each item in the list by N and return a list.
    def multiply_list(self,li,n):
        mul_list=list(map(lambda x: x*n, li))
        print(mul_list)
        return mul_list
    
    #10. Raise list to the power of N
    def power(self, li, n):
        power = list(map(lambda x: x**n, li))
        print(power)
        return power
    
    
    def menu(self, li, n):
        
        print("Please select operation -\n"  
        "1. sum_list\n" 
        "2. sum_list\n" 
        "3. square_list\n" 
        "4. odd_list\n"
        "5. even_list\n"
        "6. positive values \n"
        "7. negative values\n"
        "8. random number\n"
        "9. multiply_list by a a fixed number "+str(n)+"\n"
        "10. Raise number to the power of a fixed number "+str(n)+" \n") 
        
        # Take input from the user  
        select = int(input("Select operations form the list above:")) 
        
        
        if select == 1: 
            Calculator.sum_list(self,li)
        
            print("Summing the list li:- " +str(li))
        elif select == 2: 
            Calculator.sub_list(self,li)
            print("Subtracting the list li:- " +str(li)) 
        elif select == 3: 
            Calculator.square_list(self,li)
            print("Squaring the list li:- " +str(li))     
        elif select == 4: 
            Calculator.odd_list(self,li)
            print("Filtering out the even values out of the list li:- " +str(li))     
        elif select == 5: 
            Calculator.even_list(self,li)
            print("Filtering out the odd values out of the list li:- " +str(li))     
        elif select == 6: 
            Calculator.pos(self,li)
            print("Getting the only positive values of the list, removing all negative values:- " +str(li))     
        elif select == 7: 
            Calculator.neg(self,li)
            print("etting the only negative values of the list, removing all positive values:- " +str(li))     
        elif select == 8:
            Calculator.rand(self,li)
            print("Generating a random number between 1 and 100. " )  
            print(list(Calculator.rand(n)))
        elif select == 9:
            Calculator.multiply_list(self,li,n )
            print("Multiplying the list by a fixed number n :- " +str(n))  
        elif select == 10: 
            Calculator.power(self,li,n )
            print("Raise number to the power of a fixed number n :- " +str(li))
        else: 
            print("Invalid input") 
        
          
        
          

            
    
    
       


        
    
if __name__ == '__main__':

    '''
    Calculator().sum_list(li)           #1
    Calculator().sub_list(li)           #2
    Calculator().square_list(li)        #3
    Calculator().odd_list(li)           #4
    Calculator().even_list(li)          #5
    Calculator().pos(li)                #6
    Calculator().powtogen(5)           #7
    Calculator().rand(li)               #8
    Calculator().multipy_list(li,8)     #9
    Calculator().power(li,8)            #10
    '''

    Calculator().menu(li, 7)
    
    