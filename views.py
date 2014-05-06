from flask import render_template, flash, redirect
from app import app
from forms import txtFieldsCons, txtFieldsAgr, txtFieldsAgrPla
from pyswip import Prolog, Variable, Query

prolog = Prolog()
prolog.consult('bc.pl')

def prolCons(n):
      i = 0
      for result in prolog.query("rest(X)"):
               r =  result["X"]
	       print str(r)

@app.route('/')

@app.route('/index')
def index():
    
    return render_template("index.html")

@app.route('/consultar', methods = ('GET', 'POST'))
def consultar():
    respuesta = " "
    
    form = txtFieldsCons()
    #if form.validate_on_submit():
        
    if form.nombre.data != " ":
       prolCons(1)
       flash(respuesta)
       return redirect('/consultar')
    return render_template('consultar.html', form=form)

@app.route('/agregar', methods = ('GET', 'POST'))
def agregar():
    respuesta = ""
    form = txtFieldsAgr()
    if form.validate_on_submit():

        print "hola"
        flash('buscando...')
        return redirect('/agregar')
    return render_template('agregar.html', form=form)

@app.route('/agregarPlatillo', methods = ('GET', 'POST'))
def agregarPlatillo():
    respuesta = ""
    form = txtFieldsAgrPla()
    if form.validate_on_submit():

        print "hola"
        flash('buscando...')
        return redirect('/agregarPlatillo')
    return render_template('agregarPlatillo.html', form=form)
