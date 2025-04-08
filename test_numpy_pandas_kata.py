import numpy as np
import pandas as pd
import unittest

# Functions to implement
def create_numpy_array():
    """
    Create a 2D NumPy array with values from 1 to 9, reshaped into a 3x3 matrix.
    """
    pass  # Replace with your implementation

def calculate_array_stats(arr):
    """
    Given a NumPy array, return its mean, standard deviation, max, and min as a dictionary.
    Example: {'mean': 5.0, 'std': 2.0, 'max': 9, 'min': 1}
    """
    pass  # Replace with your implementation

def create_dataframe():
    """
    Create a Pandas DataFrame with columns 'Name' and 'Age', and add three rows of data.
    """
    pass  # Replace with your implementation

def filter_dataframe(df):
    """
    Given a Pandas DataFrame, filter rows where 'Age' is greater than 25 and return the filtered DataFrame.
    """
    pass  # Replace with your implementation

# Unit Tests
class TestNumPyPandasKata(unittest.TestCase):
    def test_create_numpy_array(self):
        arr = create_numpy_array()
        expected = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        np.testing.assert_array_equal(arr, expected, "The NumPy array is incorrect.")

    def test_calculate_array_stats(self):
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        stats = calculate_array_stats(arr)
        expected = {'mean': 5.0, 'std': np.std(arr), 'max': 9, 'min': 1}
        self.assertEqual(stats, expected, "The array statistics are incorrect.")

    def test_create_dataframe(self):
        df = create_dataframe()
        expected = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]})
        pd.testing.assert_frame_equal(df, expected, "The DataFrame is incorrect.")

    def test_filter_dataframe(self):
        df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]})
        filtered_df = filter_dataframe(df)
        expected = pd.DataFrame({'Name': ['Bob'], 'Age': [30]})
        pd.testing.assert_frame_equal(filtered_df.reset_index(drop=True), expected, "The filtered DataFrame is incorrect.")
# Unit Tests
class TestNumPyPandasKata(unittest.TestCase):
    def test_create_numpy_array(self):
        arr = create_numpy_array()
        expected = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        np.testing.assert_array_equal(arr, expected, "The NumPy array is incorrect.")

    def test_calculate_array_stats(self):
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        stats = calculate_array_stats(arr)
        expected = {'mean': 5.0, 'std': np.std(arr), 'max': 9, 'min': 1}
        self.assertEqual(stats, expected, "The array statistics are incorrect.")

    def test_create_dataframe(self):
        df = create_dataframe()
        expected = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]})
        pd.testing.assert_frame_equal(df, expected, "The DataFrame is incorrect.")

    def test_filter_dataframe(self):
        df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 30, 22]})
        filtered_df = filter_dataframe(df)
        expected = pd.DataFrame({'Name': ['Bob'], 'Age': [30]})
        pd.testing.assert_frame_equal(filtered_df.reset_index(drop=True), expected, "The filtered DataFrame is incorrect.")
if __name__ == "__main__":
    unittest.main()