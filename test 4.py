#fourth test case
import unittest
def mul(x,y):
    return x*y
class modetest(unittest.TestCase):
    def setUp(self):
       
        print("Setup executed")
    def testc(self):
       
        self.assertEqual(mul(3,3),3)
    def tearDown(self):
            
        print("tearDown executed")
        
unittest.main()
