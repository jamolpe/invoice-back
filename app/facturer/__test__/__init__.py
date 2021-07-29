from app.facturer.irpfcalculator import IrpfCalculator
import unittest


class BaseTestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.irp_calculator = IrpfCalculator()


if __name__ == '__main__':
    unittest.main()
