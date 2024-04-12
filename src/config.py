class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'compartetusazon'
    
class EmailConfig:
    # Configuración de correo electrónico
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'compartetusazon@gmail.com'
    MAIL_PASSWORD = 'qphomyjdgjudqjer'

    
config={
    'development': DevelopmentConfig,
    'email': EmailConfig
}