import unittest
import pandas as pd
import os

class TestStreamlitDashboard(unittest.TestCase):
    def test_alert_file_exists(self):
        self.assertTrue(os.path.exists("alert_report.csv"), "alert_report.csv does not exist!")

    def test_alert_file_not_empty(self):
        df = pd.read_csv("alert_report.csv")
        self.assertFalse(df.empty, "Alert report is empty — no suspicious data logged!")

    def test_alert_columns_present(self):
        expected_cols = {'timestamp', 'email', 'ip', 'reason', 'score'}
        df = pd.read_csv("alert_report.csv")
        self.assertTrue(expected_cols.issubset(df.columns), f"Missing columns in alert report! Found: {df.columns}")

    def test_score_valid_range(self):
        df = pd.read_csv("alert_report.csv")
        if not df.empty:
            self.assertTrue(df['score'].apply(lambda x: isinstance(x, (int, float))).all(), "Score column contains non-numeric values.")

if __name__ == '__main__':
    unittest.main()
