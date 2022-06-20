from enum import unique
from flask import render_template, request
import random
import json

import helpers.validatefile as helpers

def index():
    listquestions = ''
    bd = open('models/bd.json', 'r', encoding='utf-8')
    bdUniqueValor = open('models/bdUniqueValor.json', 'w')
    dados = json.load(bd)
    questionNum = random.randint(0, 2)
    listquestions = dados[questionNum]

    json.dump(listquestions, bdUniqueValor)
    bd.close()
    bdUniqueValor.close()

    return render_template('questoes/index.html', questions = listquestions)

def testeFile(pathlc):
    result = helpers.validateFile(pathlc)
    bdUniqueValor = open('models/bdUniqueValor.json', 'r')
    uniqueQuestion = json.load(bdUniqueValor)

    return render_template('questoes/index.html', questions = uniqueQuestion , controller = result)


def questoes(pathlc):
    if request.method == 'GET':
        return index()
    elif request.method == 'POST':
        return testeFile(pathlc)
            