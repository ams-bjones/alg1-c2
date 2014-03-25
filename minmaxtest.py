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

if __name__ == '__main__':
    unittest.main()