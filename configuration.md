Inicialmente realizar a inicialização do ambiente virtual python:

```bash
source venv/bin/activate
```

Caso o mysql não esteja configurado no ambiente do gitpod, rodar o seguinte comando:

```bash
gp validate
```

Abaixo, seguem as configurações para criação de um usuário no mysql se necessário:

```mysql
CREATE USER 'nomedousuario'@'localhost' IDENTIFIED BY 'senhadousuario';
GRANT ALL PRIVILEGES ON *.* TO 'nomedousuario'@'localhost';
EXIT
```

Também é necessário a criação de um arquivo .env com as seguintes variáveis
MYSQL_HOST="localhost"
MYSQL_USER="nomedousuario"
MYSQL_PASSWORD="senhadousuario"
MONGO_URI="urldeconexaodabasededadosmongodb"
