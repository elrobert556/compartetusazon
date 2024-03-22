from .entities.Recetas import Receta

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
            sql = "SELECT * FROM recetas WHERE ruta_receta = %s"
            cursor.execute(sql, (nombre_receta,))
            receta = cursor.fetchone()
            if receta:
                return receta, True  # Devuelve la receta y True si existe
            else:
                return None, False  # Devuelve None y False si no existe
        except Exception as ex:
            raise Exception(ex)