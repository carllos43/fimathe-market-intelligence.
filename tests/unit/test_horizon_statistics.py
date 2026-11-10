import unittest
from fimathe_market_intelligence import get_horizon, score_confluence, evaluate_historical_setups, wilson_interval


class HorizonTests(unittest.TestCase):
    def test_m15_horizon(self):
        result = get_horizon("M15")
        self.assertEqual(result["min_candles"], 3)
        self.assertEqual(result["max_candles"], 12)
        self.assertEqual(result["max_duration"], "3 h")

    def test_h1_horizon(self):
        result = get_horizon("H1")
        self.assertEqual(result["max_candles"], 12)
        self.assertEqual(result["max_duration"], "12 h")

    def test_unknown_timeframe_is_not_guessed(self):
        self.assertEqual(get_horizon("TICK")["status"], "not_evaluable")


class StatisticsTests(unittest.TestCase):
    def test_confluence_is_not_probability(self):
        result = score_confluence({"market_structure": True, "price_action_trigger": False})
        self.assertEqual(result["label"], "technical_confluence_score_not_win_probability")
        self.assertIn("Não representa percentual de acerto", result["warning"])

    def test_historical_records_need_oos_costs_and_sample(self):
        records = []
        for i in range(50):
            records.append({"timeframe": "M15", "setup_type": "breakout_retest", "market_regime": "bullish",
                            "instrument": "EURUSD", "outcome": "win" if i < 30 else "loss",
                            "costs_included": True, "out_of_sample": True})
        result = evaluate_historical_setups(records, timeframe="M15", setup_type="breakout_retest",
                                            market_regime="bullish", instrument="EURUSD")
        self.assertTrue(result["validated"])
        self.assertEqual(result["sample_size"], 50)
        self.assertAlmostEqual(result["win_rate"], 0.6)

    def test_missing_comparable_history_returns_no_rate(self):
        result = evaluate_historical_setups([], timeframe="H1", setup_type="reversal",
                                            market_regime="bearish")
        self.assertFalse(result["validated"])
        self.assertIsNone(result["win_rate"])

    def test_wilson_interval(self):
        low, high = wilson_interval(50, 100)
        self.assertLess(low, 0.5)
        self.assertGreater(high, 0.5)


if __name__ == "__main__":
    unittest.main()
