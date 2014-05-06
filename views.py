from flask import render_template, flash, redirect
from app import app
from forms import txtFieldsCons, txtFieldsAgr, txtFieldsAgrPla
from pyswip import Prolog, Variable, Query
f = open('bc.pl','a')
prolog = Prolog()
prolog.consult('bc.pl')

def prolCons(n):
      i = 0
      print "hola"
      for result in prolog.query("por_nom(X)"):
          
          r =  result["X"]
	  print str(r)

@app.route('/')

@app.route('/index')
def index():
    
    return render_template("index.html")

@app.route('/consultar', methods = ('GET', 'POST'))
def consultar():
    respuesta = ''
    form = txtFieldsCons()
    if form.validate_on_submit():  

       if form.nombre.data != " " and form.pais.data == None and form.platillo.data == None and form.tipo.data == None and form.ingrPlat.data == None: 
          var = "por_nom("+form.nombre.data+")"  
          print var   
          for result in prolog.query(var):
              respuesta +=  result["X"]
          flash(respuesta)

       if form.nombre.data == None and form.pais.data != None  and form.platillo.data == None and form.tipo.data == None and form.ingrPlat.data == None: 
          for result in prolog.query("por_pais(X)"):
              respuesta +=  result["X"]
          flash(respuesta)
       
       if form.nombre.data == None and form.pais.data == None  and form.platillo.data == None and form.tipo.data != None and form.ingrPlat.data == None: 
          for result in prolog.query("por_tipo(X)"):
              respuesta +=  result["X"]
          flash(respuesta)
	
       if form.nombre.data != None and form.pais.data == None  and form.platillo.data == None and form.tipo.data == None and form.ingrPlat.data != None: 
          for result in prolog.query("ingred_plato(X,Y)"):
              respuesta +=  result["X","Y"]
          flash(respuesta)
       return redirect('/consultar')
    return render_template('consultar.html', form=form)

@app.route('/agregar', methods = ('GET', 'POST'))
def agregar():
    form = txtFieldsAgr()
    if form.validate_on_submit():
        f.write("rest("+form.nombre.data+","+form.tipo.data+","+form.ubic.data+","+form.tel.data+","+form.hora.data+").\n")
        f.close()
        flash('Restaurante Agregado')
        flash("Nombre: "+form.nombre.data)
        flash("Tipo: "+form.tipo.data)
        flash("Ubicacion: "+form.ubic.data)
        flash("Telefono: "+form.tel.data)
        flash("Horario: "+form.hora.data)  
        return redirect('/agregar')
    return render_template('agregar.html', form=form)

@app.route('/agregarPlatillo', methods = ('GET', 'POST'))
def agregarPlatillo():
    form = txtFieldsAgrPla()
    if form.validate_on_submit():
       f.write("plato("+form.platillo.data+","+form.sabor.data+","+form.paisPlat.data+","+form.ingr.data+","+form.restPlat.data+").\n") 
       f.close()
       flash('Platillo Agregado')
       flash("Restaurante: "+form.restPlat.data)
       flash("Platillo: "+form.platillo.data)
       flash("Sabor: "+form.sabor.data)
       flash("Ingrediente: "+form.ingr.data)
       flash("Pais: "+form.paisPlat.data)  
       return redirect('/agregarPlatillo')
    return render_template('agregarPlatillo.html', form=form)
