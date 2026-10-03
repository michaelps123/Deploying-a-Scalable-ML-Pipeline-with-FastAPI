import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import (
    compute_model_metrics,
    inference,
    load_model,
    save_model,
    train_model,
)



@pytest.fixture
def training_data():
    """
    Return a small binary-classification dataset for testing.
    """
    X = np.array([[0], [1], [2], [3], [4], [5]])
    y = np.array([0, 0, 0, 1, 1, 1])
    return X, y


# TODO: implement the first test. Change the function name and input as needed
def test_train_model_and_inference(training_data):
    """
    The trained model should return one valid prediction per row.
    """
    X, y = training_data

    model = train_model(X, y)
    predictions = inference(model, X)

    assert isinstance(model, RandomForestClassifier)
    assert predictions.shape == y.shape
    assert set(np.unique(predictions)).issubset({0, 1})


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Metric calculations should match known expected values.
    """
    y = np.array([0, 1, 1, 1])
    predictions = np.array([0, 1, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, predictions)

    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(2 / 3)
    assert fbeta == pytest.approx(0.8)


# TODO: implement the third test. Change the function name and input as needed
def test_save_and_load_model(training_data, tmp_path):
    """
    A serialized model should retain its predictions after loading.
    """
    X, y = training_data
    model = train_model(X, y)
    model_path = tmp_path / "test_model.pkl"

    save_model(model, model_path)
    loaded_model = load_model(model_path)

    assert model_path.exists()
    assert np.array_equal(
        inference(model, X),
        inference(loaded_model, X),
    )
