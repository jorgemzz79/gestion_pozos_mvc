import os

# Configuración de la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/sistema_pozos")
