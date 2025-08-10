import pytest
from ml.model import train_model
# TODO: add necessary 

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    model = train_model(X_train, y_train)
    assert isinstance(model, xgb.XGBClassifier)


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
