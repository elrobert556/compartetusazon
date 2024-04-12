from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_usuario, email_usuario, password_usuario FROM usuarios WHERE email_usuario = '{}'".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id_usuario, email_usuario FROM usuarios WHERE id_usuario = '{}'".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_user = User(row[0], row[1], None)
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def registrar_usuario(cls, db, nombre, apellido, telefono, email, hashed_password):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO usuarios (nombre_usuario, apellido_usuario, telefono_usuario, email_usuario, password_usuario) VALUES (%s, %s,%s,%s,%s)"
            cursor.execute(sql, (nombre, apellido, telefono, email, hashed_password))
            db.connection.commit()
            return True  # Retorna True si el registro se realizó con éxito
        except Exception as ex:
            db.connection.rollback()
            return None  # Retorna None si se produce un error
        
    @classmethod
    def verificar_token(self, db, token):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT email_usuario FROM usuarios WHERE token_recuperacion = %s"
            cursor.execute(sql, (token,))
            user = cursor.fetchone()
            if user != None:
                return user,True
            else:
                return None, False
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def set_token(cls, db, token, email):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE usuarios SET token_recuperacion=%s WHERE email_usuario=%s"
            cursor.execute(sql, (token,email,))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            
    @classmethod
    def change_password(cls, db, pwd, token):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE usuarios SET password_usuario=%s WHERE token_recuperacion=%s"
            cursor.execute(sql, (pwd,token))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()