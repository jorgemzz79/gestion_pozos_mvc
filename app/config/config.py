import os

# Configuración de la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/sistema_pozos")
#DATABASE_URL = "mysql+pymysql://usuar:usuar@127.0.0.1:3306/sistema_pozos"  # type: ignore
