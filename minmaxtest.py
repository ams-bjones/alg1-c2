import minmax
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        inpu = [1,2,3,4,5]
        expMin = 1
        assert minmax.mini(inpu) == expMin #Test 1 Fails
    
    def test2(self):
        inpu = [2,3,4,5,6]
        expMin = 2
        assert minmax.mini(inpu) == expMin #Test 2 Fails
    
    def test3(self):
        inpu = [5,4,3,2,1]
        expMin = 1
        assert minmax.mini(inpu) == expMin #Test 3 Fails
    
    def test4(self):
        inpu = [1,2,3,4,5]
        expMax = 5
        assert minmax.maxi(inpu) == expMax #Test 4 Fails
if __name__ == '__main__':
    unittest.main()