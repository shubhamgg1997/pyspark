import unittest 

def cal_total(a,b):
    return a+b

def cal_minus(a,b):
    return a-b    

class CalculateTotal(unittest.TestCase):

    def test_cal_total(self):
        total=cal_total(4,6)
        assert total==10
    
    def test_cal_minus(self):
        total=cal_minus(6,4)
        assert total==2


if __name__=="__main__":
    unittest.main()
