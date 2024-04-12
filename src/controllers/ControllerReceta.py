from flask import render_template, request, redirect, url_for
from flask_login import current_user
from models.ModelRecetas import ModelReceta
import os, re
from werkzeug.utils import secure_filename


class ControllerReceta:
    @staticmethod
    def listar_recetas(db):
        recipes = ModelReceta.get_all_recipes(db)
        return render_template('auth/recetas.html', recipes=recipes)
    
    @staticmethod
    def listar_recetas_especiales(db):
        recipes = ModelReceta.receta_especial(db)
        return render_template('auth/especial.html', recipes=recipes)
    
    @staticmethod
    def popular_recipes(db):
        recipes = ModelReceta.popular_recipes(db)
        return render_template('auth/index.html', recipes=recipes)
    
    @staticmethod
    def ver_receta(db, nombre_receta):
        #Verificar la existencia de la receta en la bd
        receta, existe = ModelReceta.existe_receta(db, nombre_receta)
        if existe:
            #Buscar el usuario que publico la receta
            usuarioReceta = ModelReceta.usuario_receta(db, receta[0])
            comentarios = ModelReceta.comentarios(db, receta[0])
            usuario_logueado = current_user
            ModelReceta.increment_views(db, receta[0])
            return render_template('receta.html', recipe=receta, user=usuarioReceta, usuario=usuario_logueado, comments=comentarios)
        else:
            return "<h1>Receta no encontrada</h1>", 404
        
    @staticmethod
    def agregar_comentario(db):
        receta = request.form['nombre']
        id_usuario = request.form['usuario']
        id_receta = request.form['receta']
        comentario = request.form['comentario']
        try:
            ModelReceta.insert_comment(db, id_usuario, id_receta, comentario)
            return redirect(url_for('ver_receta', nombre_receta=receta))
        except Exception as ex:
            return "Error al agregar comentario: " + str(ex)
        
    @staticmethod
    def nueva_receta(db):
        if request.method == 'POST':
            #Titulo
            titulo = request.form['titulo_post']
            #Ruta
            titulo_formateado = titulo.lower().replace(' ', '-')
            ruta = re.sub(r'[^\w-]', '', titulo_formateado)
            #Imagen
            img_file = request.files['fileInput']
            folder_path = 'src/static/img/'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            filename = secure_filename(img_file.filename)
            if os.path.exists(os.path.join(folder_path, filename)):
                # Si el archivo ya existe, agregar un sufijo numérico único
                name, extension = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(folder_path, f"{name}_{counter}{extension}")):
                    counter += 1
                filename = f"{name}_{counter}{extension}"
            img_path = os.path.join(folder_path, filename)
            img_file.save(img_path)
            img = filename
            #Descripcion y pasos
            descripcion = request.form['descripcion']
            pasos = request.form['pasos']
            
            user = current_user
            id_user = user.id
            try:
                ModelReceta.publicar_receta(db,titulo,descripcion,pasos,id_user,ruta,img)
                return redirect(url_for('ver_receta', nombre_receta=ruta))
            except Exception as ex:
                return "Error al agregar comentario: " + str(ex)
        else:
            return render_template('auth/newRecipe.html')
        
    @staticmethod
    def me_gusta(db):
        icono = request.form['icono']
        if icono == "fa-solid":
            return "<h1>Se dio me gusta</h1>"
        else:
            return "<h1>Se quito el me gusta</h1>"