# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Añade una clave secreta para las sesiones
db = SQLAlchemy(app)

class Correos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)


# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/form_create', methods=['GET', 'POST'])
def form_create():
    if request.method == 'POST':
        name=request.form['name']
        mail=request.form['mail']
        text=request.form['text']

        correo= Correos(name=name, mail=mail, text=text)
        db.session.add(correo)
        db.session.commit()
        return redirect('/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
