from .entities.Recetas import Receta, RecetaEspecial

class ModelReceta():
    
    @classmethod
    def get_all_recipes(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT recetas.*, COUNT(favoritos.id_favorito) AS total_favoritos
                    FROM recetas
                    LEFT JOIN favoritos ON recetas.id_receta = favoritos.id_receta_favorito WHERE status_receta = 1
                    GROUP BY recetas.id_receta;"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            recipes = []
            for row in rows:
                recipe = Receta(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                recipes.append(recipe)
            return recipes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def receta_especial(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM recetas_especiales"
            cursor.execute(sql)
            rows = cursor.fetchall()
            recipes = []
            for row in rows:
                recipe = RecetaEspecial(row[0], row[1], row[2], row[3])
                recipes.append(recipe)
            return recipes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def popular_recipes(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_receta, titulo_receta, descripcion_receta, img_receta, ruta_receta, (vistas_recetas * 0.7 + favoritos_receta * 0.3) AS puntaje_popularidad
                    FROM recetas WHERE status_receta = 1 ORDER BY  puntaje_popularidad DESC LIMIT 3;"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            recipes = []
            for row in rows:
                recipe = {
                    'id_receta': row[0],
                    'titulo_receta': row[1],
                    'descripcion_receta': row[2],
                    'img_receta': row[3],
                    'ruta_receta': row[4],
                }
                recipes.append(recipe)
            return recipes
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def increment_views(cls, db, recipe_id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE recetas SET vistas_recetas = vistas_recetas + 1 WHERE id_receta = %s"
            cursor.execute(sql, (recipe_id,))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
        
    @staticmethod
    def existe_receta(db, nombre_receta):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM recetas WHERE ruta_receta = %s AND status_receta=1"
            cursor.execute(sql, (nombre_receta,))
            receta = cursor.fetchone()
            if receta:
                return receta, True  # Devuelve la receta y True si existe
            else:
                return None, False  # Devuelve None y False si no existe
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def usuario_receta(cls, db, id_receta):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT nombre_usuario, apellido_usuario FROM usuarios INNER JOIN recetas ON usuarios.id_usuario = recetas.id_usuario_receta WHERE id_receta=%s;"
            cursor.execute(sql, (id_receta,))
            user = cursor.fetchone()
            return user
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def comentarios(cls, db, id_receta):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT nombre_usuario, apellido_usuario, comentarios.* FROM usuarios
                    INNER JOIN recetas ON usuarios.id_usuario = recetas.id_usuario_receta
                    INNER JOIN comentarios ON recetas.id_receta = comentarios.id_receta_comentario WHERE id_receta_comentario=%s;"""
            cursor.execute(sql, (id_receta,))
            rows = cursor.fetchall()
            comentarios = []
            for row in rows:
                comentario = {
                    'usuario': row[0] + ' ' + row[1],
                    'id_comentario': row[2],
                    'contenido': row[3],
                    'fecha': row[4]
                }
                comentarios.append(comentario)
            return comentarios
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def insert_comment(cls, db, id_usuario, id_receta, comentario):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO comentarios (id_usuario_comentario, id_receta_comentario, contenido_comentario) VALUES (%s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_receta, comentario))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
        
    @classmethod
    def publicar_receta(cls,db,titulo,descripcion,pasos,id_user,ruta,img):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO recetas (titulo_receta, descripcion_receta, pasos_recetas, id_usuario_receta, ruta_receta, img_receta) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (titulo,descripcion,pasos,id_user,ruta,img))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)