from flask import jsonify, request, url_for, current_app
from app import db
from app.models import MyTable 
from app.api import bp

import os, sys
import pathlib, multiprocessing
from platform import platform, machine, processor, system

@bp.route('/data', methods=['GET'])
def data():
    t = MyTable.query.all()
    table_data = {}
    for i in t:
        table_data[i.id] = { 'Item' : i.item, 'Value' : i.value, 'Time' : (i.stamp).strftime("%b %d %Y %H:%M:%S") }
    return jsonify(table_data)


@bp.route('/system', methods=['GET'])
def system():
    system_info = {}
    system_info['Operating System'] = platform()
    system_info['Platform System'] = sys.platform
    system_info['OS Name'] = os.name
    system_info['CPUs'] = multiprocessing.cpu_count()
    system_info['Current Directory'] = '/'.join(str(os.getcwd()).split('\\'))    

    return jsonify(system_info)
