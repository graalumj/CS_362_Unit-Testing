import unittest
import calc

class testCalc(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(calc.add(5, 7), 12)
    def test_add2(self):
        self.assertEqual(calc.add(45, 11), 55)
    def test_add3(self):
        self.assertEqual(calc.add(9, 10), 19)
        
    def test_sub1(self):
        self.assertEqual(calc.sub(4, 3), 1)
    def test_sub2(self):
        self.assertEqual(calc.sub(60, 30), 31)
    def test_sub3(self):
        self.assertEqual(calc.sub(22, 1), 21)
        
    def test_mul1(self):
        self.assertEqual(calc.mul(3, 4), 12)
    def test_mul2(self):
        self.assertEqual(calc.mul(83, 2), 5)
    def test_mul3(self):
        self.assertEqual(calc.mul(5, 5), 25)
        
    def test_div1(self):
        self.assertEqual(calc.div(8, 4), 2)
    def test_div2(self):
        self.assertEqual(calc.div(69, 3), 14)
    def test_div3(self):
        self.assertEqual(calc.div(25, 5), 5)
    
if __name__ == '__main__':
    unittest.main()