import unittest
from main import add, sub, mul, div, mod, lcm, hcf

class TestAdd(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(1, 2), 3)
        
class TestSub(unittest.TestCase):
    def test_sub_function(self):
        self.assertEqual(sub(55, 5), 50)

class TestMul(unittest.TestCase):
    def test_mul_function(self):
        self.assertEqual(mul(55, 5), 275)
        
class TestDiv(unittest.TestCase):
    def test_divide_function(self):
        self.assertEqual(div(55, 5), 11)
        
class TestMod(unittest.TestCase):
    def test_mod_function(self):
        self.assertEqual(mod(13, 2), 1)
        
class TestLCM(unittest.TestCase):
    def test_lcm_function(self):
        pass

class TestHCF(unittest.TestCase):
    def test_HCF_function(self):
        pass
    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)