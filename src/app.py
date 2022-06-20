from flask import Flask
import controllers.aplication as aplication
import controllers.questoesController as questoesController

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET'])
def homePage():
    return aplication.indexHome()

@app.route('/questoes', methods=['GET', 'POST'])
def questoesPage():
    return questoesController.questoes(app.config['UPLOAD_FOLDER'])


if __name__ == '__main__':
    app.run(debug=True)