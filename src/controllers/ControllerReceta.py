from flask import render_template
from models.ModelRecetas import ModelReceta

class ControllerReceta:
    @staticmethod
    def listar_recetas(db):
        recipes = ModelReceta.get_all_recipes(db)
        return render_template('auth/recetas.html', recipes=recipes)
    
    @staticmethod
    def popular_recipes(db):
        recipes = ModelReceta.popular_recipes(db)
        return render_template('auth/index.html', recipes=recipes)
    
    @staticmethod
    def ver_receta(db, nombre_receta):
        receta, existe = ModelReceta.existe_receta(db, nombre_receta)
        if existe:
            ModelReceta.increment_views(db, receta[0])
            return render_template('receta.html', recipe=receta)
        else:
            return "<h1>Receta no encontrada</h1>", 404