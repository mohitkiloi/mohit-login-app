import unittest
import joblib
import pandas as pd
from detect_anomaly import preprocess

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = joblib.load("model.joblib")

    def test_single_prediction(self):
        test_log = {
            'status': 'failure',
            'screen_resolution': '1366x768',
            'user_agent': 'Mozilla/5.0',
            'location': 'Berlin, Germany'
        }
        features = preprocess(test_log)
        result = self.model.predict(features)
        self.assertIn(result[0], [-1, 1])

if __name__ == '__main__':
    unittest.main()