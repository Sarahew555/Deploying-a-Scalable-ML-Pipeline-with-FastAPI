import pytest
from ml.model import train_model, compute_model_metrics, inference
import numpy as np
import unittest
from unittest import mock
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
    y_true = np.array([0, 1, 0, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 1, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    self.assertAlmostEqual(precision, 1.0)
    self.assertAlmostEqual(recall, 1.0)    
    self.assertAlmostEqual(fbeta, 1.0)   


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    X_test = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    expected = np.array([0, 1, 0])
    mock_model = mock.Mock()
    mock_model.predict.return_value = expected
    actual = inference(mock_model, X_test)
    mock_model.predict.assert_called_once_with(X_test)
    np.testing.assert_array_equal(actual, expected)
