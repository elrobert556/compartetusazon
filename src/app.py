from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, logout_user, login_required
from config import config

#Controladores
from controllers.ControllerReceta import ControllerReceta
from controllers.ControllerUser import ControllerUser

#Modelos
from models.ModelUser import ModelUser
#from models.ModelRecetas import ModelReceta

#Entities
#from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return ControllerReceta.popular_recipes(db)

@app.route('/recetas')
def recetas():
    return ControllerReceta.listar_recetas(db)

@app.route('/recetas/<nombre_receta>')
def ver_receta(nombre_receta):
    return ControllerReceta.ver_receta(db, nombre_receta)

@app.route('/contact')
def contact():
    return render_template('auth/contact.html')


@app.route('/login', methods=['GET','POST'])
def login():
    return ControllerUser.verificar_usuario(db)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET','POST'])
def register():
    return ControllerUser.registrar_usuario(db)

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

@app.route('/home')
def home():
    return render_template('auth/index.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()