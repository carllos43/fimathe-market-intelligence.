import unittest
from fimathe_market_intelligence import analyze_multi_timeframe

class MultiTimeframeTests(unittest.TestCase):
    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError): analyze_multi_timeframe({})

if __name__ == "__main__": unittest.main()
