from flask import Flask, jsonify
from dataclasses import dataclass
from vartastorage.vartastorage import VartaStorage
import time


app = Flask(__name__)

class ModbusData:
    soc: int
    grid_power: int
    state: int
    active_power: int
    apparent_power: int
    error_code: int
    total_charged_energy: int
    number_modules: int
    installed_capacity: int
    serial: str
    table_version: int
    software_version_ems: str
    software_version_ens: str
    software_version_inverter: str

varta = VartaStorage('127.0.0.1', 502, username="username", password="password", cgi=False)

def fetch_modbus_data():
    while True:
        try:
            global modbus_data
            modbus_data = varta.get_all_data_modbus()
        except Exception as e:
            print(f"Failed to fetch Modbus data: {e}")
        time.sleep(15) 

import threading
fetch_thread = threading.Thread(target=fetch_modbus_data)
fetch_thread.start()

@app.route('/api/modbus_data', methods=['GET'])
def get_modbus_data():
    try:
        global modbus_data
        return jsonify({
            'soc': modbus_data.soc,
            'grid_power': modbus_data.grid_power,
            'state': modbus_data.state,
            'active_power': modbus_data.active_power,
            'apparent_power': modbus_data.apparent_power,
            'error_code': modbus_data.error_code,
            'total_charged_energy': modbus_data.total_charged_energy,
            'number_modules': modbus_data.number_modules,
            'installed_capacity': modbus_data.installed_capacity,
            'serial': modbus_data.serial,
            'table_version': getattr(modbus_data, 'table_version', None),
            'software_version_ems': getattr(modbus_data, 'software_version_ems', None),
            'software_version_ens': getattr(modbus_data, 'software_version_ens', None),
            'software_version_inverter': getattr(modbus_data, 'software_version_inverter', None)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

