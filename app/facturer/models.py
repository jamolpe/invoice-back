class IrpfSection:
    def __init__(self, frm, value, to=None):
        self.frm = frm
        self.value = value
        self.to = to

    def serialize(self):
        return {
            "from": self.frm,
            "value": self.value,
            "to": self.to
        }

    def deserialize(self, json):
        self.frm = json.get('from')
        self.value = json.get('value')
        self.to = json.get('to')
