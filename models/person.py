from db import db

class PersonModel(db.Model):
    __tablename__='person'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellidoPaterno = db.Column(db.String(100), unique=False, nullable=True) #unique=el campo sera unico o se podra repetir - nullable si el campo sera null o si sera obligatorio que tenga un valor
    apellidoMaterno = db.Column(db.String(100))
    nroDocumento = db.Column(db.String(100))

    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, nroDocumento):
        self.nombre = nombre # self.name = null, nombre = null -----> nombre = Juan --> seld.nombre = Juan
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.nroDocumento = nroDocumento

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_person(cls):
        return cls.query.all()

    @classmethod
    def update_person(cls, id, data):
        person = cls.query.filter_by(id=id).first() #filtra por id y trae el primero
        person.nombre = data.nombre
        person.apellidoPaterno = data.apellidoPaterno
        person.apellidoMaterno = data.apellidoMaterno
        person.nroDocumento = data.nroDocumento
        db.session.commit()
