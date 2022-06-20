from flask import request
import os

def validateFile(pathlc):
    file = request.files['questao']
    file.save(os.path.join(pathlc, file.filename))

    arquivo = open('uploads/'+ file.filename, 'r', encoding='utf-8')
    exe = open('helpers/execute.py', 'w')
    for i in arquivo.readlines():
        exe.write(i)
    
    exe.close()
    arquivo.close()

    controller = False
    try:
        from helpers.execute import execution
        controller = True
        return controller

    except ImportError:
        os.remove('uploads/' + file.filename)
        controller = False
        return controller
