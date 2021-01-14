import os
from pathlib import Path

current_file_path = os.path.abspath(__file__)
PROJECT_PATH = Path(current_file_path).parent.parent

# development env
MYSQL_PASS = 'mysql'
MYSQL_USER = 'mysql'
MYSQL_DB = 'test'
MYSQL_PORT = 3366
MYSQL_HOST = '127.0.0.1'

