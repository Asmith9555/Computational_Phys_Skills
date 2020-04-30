#Write a test function using assertRaises
import unittest
#Function
def division(a, b):
    return a/b
#Test
#TYC-B2: Wrie a code that passes c-level tests
class raiseTest(unittest.TestCase):
#TYC-C5: Write a test using assertRaises
    def test_1(self):
        self.assertRaises(ZeroDivisionError, division, 1,0)
    def test_2(self):
        self.assertEqual(division(1,1),1)
    def test_3(self):
        self.assertTrue(division(1,1)==1)
    def test_4(self):
        self.assertEqual(1/0.1,10)
if __name__ == '___main__':
    unittest.main()
# Then Run $python -m unittest "TYC-C5"
