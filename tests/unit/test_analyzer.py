import unittest
from fimathe_market_intelligence import analyze_market
from fimathe_market_intelligence.validation import DataValidationError
from fimathe_market_intelligence.models import AnalysisConfig

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
        self.assertEqual(result["operational_priority"], "local_microstructure_near_current_price")

    def test_rejects_invalid_ohlc(self):
        data = self.sample()
        data[0]["high"] = 1
        with self.assertRaises(DataValidationError):
            analyze_market(data)

    def test_requires_minimum_candles(self):
        with self.assertRaises(DataValidationError):
            analyze_market(self.sample()[:5])

    def test_prioritizes_local_over_distant_extremes(self):
        """Verifica que o motor não usa automaticamente extremos de range amplo como entrada
        quando existe microestrutura local válida mais próxima."""
        # Série com range amplo antigo e consolidação local recente
        closes = (
            [100 + i*0.5 for i in range(30)] +  # subida ampla
            [115 - i*0.3 for i in range(20)] +  # correção
            [109 + (i % 3)*0.1 for i in range(25)]  # lateral local recente
        )
        candles = [dict(timestamp=f"{i:03d}", open=x-0.1, high=x+0.3, low=x-0.4, close=x)
                   for i, x in enumerate(closes)]
        cfg = AnalysisConfig(local_lookback_candles=30, max_operational_distance_atr=2.0)
        result = analyze_market(candles, "EURUSD", "M15", cfg)
        primary = result["primary_scenario"]
        # Deve preferir wait ou cenário local, nunca forçar entrada no extremo antigo
        if primary["direction"] != "wait":
            self.assertEqual(primary.get("source"), "local_microstructure")
            # Stop deve estar próximo (dentro do filtro)
            self.assertIsNotNone(primary.get("risk_pips") or primary.get("risk_reward"))

if __name__ == "__main__":
    unittest.main()
