from flask import Flask, render_template, request
from models.person import PersonModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/flask_session'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'string key'

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/helloFlask')
def helloFlask():
    return "<h1>hello flask</h1> "

@app.route('/')
def main():
    a = 4 + 2
    return render_template('index.html', value=a)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/base/block')
def block():
    return render_template('block.html')

@app.route('/base/form')
def formulario():
    return render_template('form.html')

@app.route('/base/form', methods=['POST'])
def saveForm():

    nombre = request.form['nombre']
    apellidoPaterno = request.form['apellidoPaterno']
    apellidoMaterno = request.form['apellidoMaterno']
    nroDocumento = request.form['nroDocumento']

    person = PersonModel(nombre, apellidoPaterno, apellidoMaterno, nroDocumento)
    person.save_to_db()

    return render_template('form.html')

@app.route('/base/listaPersonas')
def getPersons():
    data = PersonModel.get_all_person()
    return render_template('tablep.html', data=data)


@app.route('/base/form/<int:idPerson>', methods=['GET','POST'])
def updatePerson(idPerson):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidoPaterno = request.form['apellidoPaterno']
        apellidoMaterno = request.form['apellidoMaterno']
        nroDocumento = request.form['nroDocumento']

        person = PersonModel(nombre, apellidoPaterno, apellidoMaterno, nroDocumento)

        person.update_person(idPerson,person)

    return render_template('formUpdate.html', idPerson=idPerson)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=7000, debug=True)