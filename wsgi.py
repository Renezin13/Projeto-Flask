import sys
import os

# Caminho para o diretório do seu projeto
sys.path.insert(0, '/var/www/Projeto-Flask')

# Caminho para o ambiente virtual (não precisa do 'activate_this.py')
activate_this = '/var/www/Projeto-Flask/env/bin/activate_this.py'

# Importa o aplicativo Flask
from app import app as application