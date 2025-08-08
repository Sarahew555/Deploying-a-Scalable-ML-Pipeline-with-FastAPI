import pytest
from sklearn.svm import SVC
from ml.model import train_model
from ml.data import process_data

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model_returns_exp_algorithm():
    """
    Test 1 verifies that the trained model object is the same as the expected algorithm type.
    """
    X, y = 
    model = train_model(X, y)
    assert isinstance(model, SVC)

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
