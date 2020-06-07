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


        
 
unittest.main()
        
if __name__ == '__main__':
    unittest.main()