# Recipe.py

class Receta:
    def __init__(self, id_receta, titulo_receta , descripcion_receta, pasos_recetas, status_receta, id_usuario_receta, ruta_receta,vistas_receta,img_receta, total_favoritos):
        self.id = id_receta
        self.titulo = titulo_receta
        self.descripcion = descripcion_receta
        self.pasos = pasos_recetas
        self.status = status_receta
        self.usuario = id_usuario_receta
        self.ruta = ruta_receta
        self.vistas = vistas_receta
        self.img = img_receta
        self.fav = total_favoritos

    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.titulo}, description={self.descripcion}, name={self.pasos}, status={self.status}, user={self.usuario}, ruta={self.ruta}, vistas={self.vistas}, img={self.img}, fav={self.fav})"
