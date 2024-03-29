from flask_wtf import Form
from wtforms import TextField, RadioField
from wtforms.validators import DataRequired, Optional

class txtFieldsCons(Form):

    nombre = TextField('Nombre')    
    platillo = TextField('Platillo')
    ingrPlat = TextField('Ingrediente')
    ingr = TextField('Ingrediente')
    pais = TextField('Pais') 
    opc = TextField('*Opcional')

class txtFieldsAgr(Form):

    nombre = TextField('Nombre', validators = [DataRequired()])    
    tipo = TextField('Tipo', validators = [DataRequired()])
    ubic = TextField('Ubicacion', validators = [DataRequired()])
    tel = TextField('Telefono', validators = [DataRequired()])
    hora = TextField('Horario', validators = [DataRequired()])

class txtFieldsAgrPla(Form):

    restPlat = TextField('Restaurante', validators = [DataRequired()])
    platillo = TextField('Platillo', validators = [DataRequired()])
    ingr = TextField('Ingrediente', validators = [DataRequired()])
    nomPlat = TextField('Nombre', validators = [DataRequired()])
    sabor =  RadioField('Sabor', [None], choices=[('picante','Picante'),('salado','Salado'),('dulce','Dulce'),('agridulce','Agridulce'),('amargo','Amargo')])
    paisPlat = TextField('Pais', validators = [DataRequired()])
    opc = TextField('*Opcional')
