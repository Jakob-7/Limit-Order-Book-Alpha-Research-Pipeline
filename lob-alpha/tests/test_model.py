import numpy as np

from models.logistic import LogisticLOBClassifier


def test_logistic_model_fit_predict():
    X = np.array(
        [
            [0.2, 0.1, 0.0, 1.0, 3.0, -0.2, 0.5],
            [-0.1, -0.2, 0.1, -1.0, 2.0, 0.3, -0.4],
        ]
    )
    y = np.array([1, 0])

    model = LogisticLOBClassifier()
    model.fit(X, y)

    preds = model.predict(X)
    probs = model.predict_proba(X)

    assert preds.shape == (2,)
    assert probs.shape == (2,)
    assert np.all(probs >= 0.0) and np.all(probs <= 1.0)
