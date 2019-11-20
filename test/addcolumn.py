import unittest
import pandas as pd 

def add_col(df,new_col_name,default_value):
    '''Add a coloumn with a default value'''

    df[new_col_name]=default_value

    return df
    
class Count(unittest.TestCase):

    def test_add_col(self):
        #setup
        df=pd.DataFrame({
            'col_a':['a','a','a'],
            'col_b':['b','b','b'],
            'col_c':['c','c','c'],
        })
        #call function
        actual=add_col(df,'col_d','d')

        #set expectations
        expected=pd.DataFrame({
            'col_a':['a','a','a'],
            'col_b':['b','b','b'],
            'col_c':['c','c','c'],
            'col_d':['d','d','d'],
        })

        #assertion
        pd.testing.assert_frame_equal(actual,expected)

if __name__=="__main__":
    unittest.main()



