from app.facturer.irpfcalculator import IrpfCalculator
from app.facturer.models import IrpfSection
from app.facturer.core import FacturerProvider
from flask import Blueprint, request, jsonify
from app.facturer.database.database import database

mod = Blueprint('facturer', __name__, url_prefix='/facturer')

irpf_calculator: IrpfCalculator = IrpfCalculator(database.db.irpfsections)
factureProvider: FacturerProvider = FacturerProvider(irpf_calculator)


@mod.route('/', methods=['GET'])
def index():
    return 'hola facturer'


@mod.route('/irpf/sections', methods=['GET', 'PUT'])
def irpf_sections():
    if request.method == 'PUT':
        content = request.get_json()
        return content
    return jsonify([section.serialize() for section in irpf_calculator.load_irpf_sections()])


@mod.route('/irpf/create',  methods=['POST'])
def create_irpf_sections():
    content = request.get_json()
    irpf = IrpfSection(None, None)
    irpf.deserialize(content)
    if irpf_calculator.create_new_irpfs_section(irpf):
        return jsonify({"message": 'stored ok'})
    return jsonify({"message": "error saving"}), 422
