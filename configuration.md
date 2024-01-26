Inicialmente realizar a inicialização do ambiente virtual python:

'''bash
source venv/bin/activate
'''

Abaixo, seguem as configurações para criação de um usuário no mysql se necessário:

'''
sudo mysql

CREATE USER 'vinipmartins'@'localhost' IDENTIFIED BY 'mysql-123';
GRANT ALL PRIVILEGES ON *.* TO 'vinipmartins'@'localhost';
exit
'''

