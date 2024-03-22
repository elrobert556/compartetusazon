from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id_usuario, email_usuario, password_usuario) -> None:
        self.id = id_usuario
        self.email = email_usuario
        self.password = password_usuario
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)