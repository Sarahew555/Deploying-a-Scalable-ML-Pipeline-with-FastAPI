import pytest
from sklearn.svm import SVC
from ml.model import train_model
from ml.data import process_data
from ml.model import compute_model_metrics
from ml.data import apply_label
from sklearn.metrics import fbeta_score, precision_score, recall_score

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model_returns_exp_algorithm():
    """
    Test 1 verifies that the trained model object is the same as the expected algorithm type.
    """
    X_test_train = np.array()
    y_test_train = np.array()
    trained_model = train_model(X_test_train, y_test_train)
    assert isinstance(trained_model, SVC)

# TODO: implement the second test. Change the function name and input as needed
def test_model_metrics_expected_values():
    """
    Test 2 verifies that the expected values for metrics are close to actual values.
    """
    y_true = np.array([1, 1, 0, 1, 0, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 1, 0, 1])

    expected_precision = precision_score(y_true, y_pred, zero_division=1)
    expected_recall = recall_score(y_true, y_pred, zero_division=1)
    expected_fbeta = fbeta_score(y_true, y_pred, zero_division=1)

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert np.isclose(precision, expected_precision, atol=1e-7)
    assert np.isclose(recall, expected_recall, atol=1e-7)
    assert np.isclose(fbeta, expected_fbeta, atol=1e-7)
    


# TODO: implement the third test. Change the function name and input as needed
def test_binary_label():
    """
    Test 3 checks that the binary label representing >50K returns the correct output
    """
    inference_input = [1]
    expected_output = ">50K"
    actual_output = apply_label(inference_input)
    assert actual_output == expected_output
