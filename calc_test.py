import unittest

from calc import Calculator



class TestCalculator(unittest.TestCase):
    
    

    def setUp(self):
        pass
    
         # 1. Sum of all items in a list using reduce.
    def test_sum_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):
        
        self.assertEqual(182, Calculator.sum_list(self, li))
        
    def test_sub_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):
        self.assertEqual(-180, Calculator.sub_list(self, li))
        
    def test_square_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):
        self.assertEqual([2, 4, 6, 8, -10, 12, 14, 16, -18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40], Calculator.square_list(self, li))
        
    def test_odd_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):
        self.assertEqual([1, 3, -5, 7, -9, 11, 13, 15, 17, 19], Calculator.odd_list(self, li))
        
    def test_even_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):     
        self.assertEqual([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], Calculator.even_list(self, li))
        
    def test_neg(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):  
        #self.assertEqual([1, 2, 3, 4, -5, 6, 7, 8, -9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], Calculator.neg(self, li))
        self.assertEqual([-5,-9], Calculator.neg(self, li))
    
    def test_pos(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):    
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], Calculator.pos(self, li))

    def test_multiply_list(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]):  
        self.assertEqual([5,10,15,20,-25,30,35,40,-45,50,55,60,65,70,75,80,85,90,95,100], Calculator.multiply_list(self, li, 5))
        
    def test_power(self, li=[1, 2, 3, 4, -5,6,7,8,-9,10,11,12,13,14,15,16,17,18,19,20]): 
        self.assertEqual([1, 32, 243, 1024, -3125, 7776, 16807, 32768, -59049, 100000, 161051, 248832, 371293, 537824, 759375, 1048576, 1419857, 1889568, 2476099, 3200000], 
                         Calculator.power(self, li, 5))


        
        
'''
from calc import add, divide, exponent, multiply, subtract

class CalculatorTest(unittest.TestCase):
    
     # 1. Sum of all items in a list using reduce.
    def test_sum_list(self, li):
        self.assertEqual(208, sum_list(li2))

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
        pos_list= list( filter((lambda x: x < 0),li ))
        print(pos_list)
        return(pos_list)

    #7. Return only negative values
    def neg(self, max=0):
        neg_list= list( filter((lambda x: x > 0),li ))
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
        return list(map(lambda x: x**n, li))

    def testAdd(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(5, add(2, 3))
        self.assertEqual(5, add(5, 0))
        self.assertEqual(1, add(2, -1))

    def testDivide(self):
        self.assertEqual(1, divide(2, 2))
        self.assertEqual(4, divide(2, 0.5))
        self.assertEqual(5, divide(5, 1))
        self.assertEqual('Cannot divide by Zero', divide(5, 0))

    def testExponent(self):
        self.assertEqual(32, exponent(2, 5))
        self.assertEqual(2, exponent(2, 1))
        self.assertEqual(2, exponent(4, 0.5))
        self.assertEqual(1, exponent(2, 0))

    def testMultiply(self):
        self.assertEqual(4, multiply(2, 2))
        self.assertEqual(0, multiply(5, 0))
        self.assertEqual(5, multiply(5, 1))

    def testSubtract(self):
        self.assertEqual(0, subtract(2, 2))
        self.assertEqual(5, subtract(5, 0))
        self.assertEqual(-1, subtract(2, 3))
'''
unittest.main()
        
if __name__ == '__main__':
    unittest.main()