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