import add_col
import pytest
import pandas as pd

@pytest.fixture()
def df():
    pd.DataFrame({
            'col_a':['a','a','a'],
            'col_b':['b','b','b'],
            'col_c':['c','c','c'],
        })

@pytest.fixture()
def df_with_col_d():
    pd.DataFrame({
            'col_a':['a','a','a'],
            'col_b':['b','b','b'],
            'col_c':['c','c','c'],
            'col_d':['d','d','d'],

        })

def test_add_col(df,df_with_col_d):
    actual=add_col(df,'col_d','d')
    #excepted=df_with_col_d

    pd.testing.assert_frame_equal(actual,df_with_col_d)
