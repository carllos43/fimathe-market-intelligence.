import unittest
from fimathe_market_intelligence import analyze_market
from fimathe_market_intelligence.validation import DataValidationError

class AnalyzerTests(unittest.TestCase):
    def sample(self):
        closes = [10,11,10.5,12,11.5,13,12.5,14,13.5,15,14.5,16,15.5,17,16.5,18,17.5,19,18.5,20,19.5,21]
        return [dict(timestamp=f"{i:03d}", open=x-.2, high=x+.4, low=x-.5, close=x) for i,x in enumerate(closes)]
    def test_returns_required_sections_and_no_fake_probability(self):
        result = analyze_market(self.sample(), "TEST", "H1")
        self.assertIn(result["market_regime"], ("bullish","bearish","sideways","transition","unknown"))
        self.assertFalse(result["statistics"]["validated"])
        self.assertIsNone(result["statistics"]["win_rate"])
        self.assertTrue(result["scenarios"])
        self.assertIn("horizon", result)
        self.assertIn("technical_confluence", result)
    def test_rejects_invalid_ohlc(self):
        data = self.sample()
        data[0]["high"] = 1
        with self.assertRaises(DataValidationError): analyze_market(data)
    def test_requires_minimum_candles(self):
        with self.assertRaises(DataValidationError): analyze_market(self.sample()[:5])

if __name__ == "__main__": unittest.main()
