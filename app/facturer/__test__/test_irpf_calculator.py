
from app.facturer.__test__ import BaseTestClass


class IrpfCalculatorTestCase(BaseTestClass):
    def test_calculate_retention(self):
        calculo = self.irp_calculator.calculate_total_retentions(12.450)
        self.assertEqual(2988, calculo)
