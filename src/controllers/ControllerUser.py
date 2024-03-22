from flask import render_template, flash, request, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user
from models.ModelUser import ModelUser
from models.entities.User import User

class ControllerUser:
        
    @staticmethod
    def verificar_usuario(db):
        if request.method == 'POST':
            user = User(0, request.form['email'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('home'))
                else:
                    flash("Invalid Password")
                    return render_template('auth/login.html')
            else:
                flash("User not Found")
                return render_template('auth/login.html')
        else:
            return render_template('auth/login.html')
        
    @staticmethod
    def registrar_usuario(db):
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            telefono = request.form['telefono']
            email = request.form['email']
            raw_password = request.form['password']
            confirm_password = request.form['confirm_password']
            # Verificar si las contraseñas coinciden
            if raw_password == confirm_password:
                # Las contraseñas coinciden, hashear la contraseña
                hashed_password = generate_password_hash(raw_password, method='pbkdf2:sha256', salt_length=16)
                
                # Llamada a la función del modelo para registrar el usuario
                new_user = ModelUser.registrar_usuario(db, nombre, apellido, telefono, email, hashed_password)
                
                if new_user is True:
                    # Redirigir a la página de inicio de sesión o a donde sea apropiado
                    return redirect(url_for('login'))
                else:
                    # Manejar el error en el registro
                    flash("Error al registrar el usuario")
                    return render_template('auth/register.html')
            else:
                flash("Las contraseñas no coinciden")
                return render_template('auth/register.html', nombre=nombre, apellido=apellido, telefono=telefono, email=email)
        else:
            # Renderizar el formulario de registro
            return render_template('auth/register.html')