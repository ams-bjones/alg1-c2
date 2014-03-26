import mean
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        inpu = [1,2,3,4,5]
        expCount = 5
        assert mean.count(inpu) == expCount #Test 1 Fails
    
    def test2(self):
        inpu = [1,2,3,4,5]
        expSum = 15
        assert mean.sumof(inpu) == expSum #Test 2 Fails    
    
    def test3(self):
        inpu = [1,2,3,4,5]
        expMean = 3
        assert mean.mean(inpu) == expMean #Test 3 Fails
        
    
    

        
if __name__ == '__main__':
    unittest.main()