from app.facturer.models import IrpfSection
from pymongo.errors import BulkWriteError


class IrpfCalculator:
    sections: list

    def __init__(self, collection) -> None:
        self.collection = collection
        self.create_base_irpfs()

    def load_irpf_sections(self) -> list:
        sections: list = []
        dbsections = self.collection.find({})
        for section in dbsections:
            sections.append(IrpfSection(
                section['from'], section['value'], section['to']))
        self.sections = sections
        return sections

    def create_base_irpfs(self) -> bool:
        try:
            self.collection.drop()
            self.collection.insert_many([
                {
                    'from': 0,
                    'to': 12450,
                    'value': 24.00
                },
                {
                    'from': 12450,
                    'to': 17707.20,
                    'value': 26
                },
                {
                    'from': 17707.20,
                    'to': 20200,
                    'value': 29
                },
                {
                    'from': 20200,
                    'to': 33007.20,
                    'value': 33.50
                },
                {
                    'from': 33007.20,
                    'to': 35200,
                    'value': 37
                },
                {
                    'from': 35200,
                    'to': 53407.20,
                    'value': 40
                },
                {
                    'from': 53407.20,
                    'to': 60000,
                    'value': 44
                },
                {
                    'from': 60000,
                    'to': 120000.20,
                    'value': 46
                },
            ])
        except BulkWriteError:
            return False

    def create_new_irpfs_section(self, irpf: IrpfSection) -> bool:
        try:
            self.collection.insert_one({
                'from': irpf.frm,
                'value': irpf.value,
                'to': irpf.to
            })
            return True
        except BulkWriteError:
            return False

    def calculate_total_retentions(self, ammount) -> int:
        i = 0
        retention = 0
        while ammount > 0:
            section: IrpfSection = self.sections[i]
            if ammount >= section.to:
                retention += section.to * (section.value/100)
            else:
                retention += ammount * (section.value/100)
            ammount = ammount - section.to
            i += 1
        return retention
