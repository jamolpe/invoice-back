
from typing import List
from app.facturer.irpfcalculator import IrpfCalculator


class FacturerProvider:

    def __init__(self, irpf_calculator) -> None:
        self.irpf_calculator = irpf_calculator
