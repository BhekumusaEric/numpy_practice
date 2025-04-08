import numpy as np
import pandas as pd

def numpy_questions():
    print("\n--- NumPy Questions ---")
    
    # Question 1
    print("\n1. What does the `np.array()` function do?")
    print("a) Creates a list")
    print("b) Creates a NumPy array")
    print("c) Creates a dictionary")
    print("d) Creates a tuple")
    answer = input("Your answer: ")
    if answer.lower() == 'b':
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) Creates a NumPy array.")
    
    # Question 2
    print("\n2. What is the shape of the array created by `np.zeros((3, 4))`?")
    print("a) (3, 4)")
    print("b) (4, 3)")
    print("c) (3,)")
    print("d) (4,)")
    answer = input("Your answer: ")
    if answer.lower() == 'a':
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) (3, 4).")
    
    # Coding Exercise
    print("\n3. Write a NumPy code snippet to create a 2D array with values from 1 to 9, reshaped into a 3x3 matrix.")
    print("Type your code below:")
    user_code = input(">>> ")
    try:
        exec(user_code)
        print("Code executed successfully!")
    except Exception as e:
        print(f"Error in your code: {e}")

def pandas_questions():
    print("\n--- Pandas Questions ---")
    
    # Question 1
    print("\n1. What does the `pd.DataFrame()` function do?")
    print("a) Creates a NumPy array")
    print("b) Creates a Pandas DataFrame")
    print("c) Creates a Pandas Series")
    print("d) Creates a dictionary")
    answer = input("Your answer: ")
    if answer.lower() == 'b':
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) Creates a Pandas DataFrame.")
    
    # Question 2
    print("\n2. What method is used to display the first few rows of a DataFrame?")
    print("a) .head()")
    print("b) .tail()")
    print("c) .info()")
    print("d) .describe()")
    answer = input("Your answer: ")
    if answer.lower() == 'a':
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) .head().")
    
    # Coding Exercise
    print("\n3. Write a Pandas code snippet to create a DataFrame with columns 'Name' and 'Age', and add three rows of data.")
    print("Type your code below:")
    user_code = input(">>> ")
    try:
        exec(user_code)
        print("Code executed successfully!")
    except Exception as e:
        print(f"Error in your code: {e}")

def main():
    print("Welcome to the NumPy and Pandas Assessment!")
    print("You will be tested on your knowledge of NumPy and Pandas.")
    
    numpy_questions()
    pandas_questions()
    
    print("\nAssessment Complete! Review your answers and keep practicing.")

if __name__ == "__main__":
    main()