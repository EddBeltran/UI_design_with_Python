import pandas as pd
import numpy as np

def save_two_columns(filename, first_column_array, second_column_array):      
    df = pd.DataFrame({
        'Column 1': first_column_array,
        'Column 2': second_column_array
        })

    df.to_csv(filename, index=False)