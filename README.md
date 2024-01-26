# Pipeline Python, MongoBD, MySQL

Repositório com a construção de um pipeline de dados usando MongoDB e MySQL

Este projeto foi desenvolvido usando o Gitpod. Por isso, ao replicar esse projeto no Gitpod, é importante rodar o seguinte comando:

```bash
gp validate
```
Este comando irá garantir que o MySQL esteja instalado.

Em seguida, realizar os seguintes comandos:

Inicialmente realizar a inicialização do ambiente virtual python:

```bash
source venv/bin/activate
```

Realizar as configurações para criação de um usuário no mysql se necessário:

```mysql
CREATE USER 'nomedousuario'@'localhost' IDENTIFIED BY 'senhadousuario';
GRANT ALL PRIVILEGES ON *.* TO 'nomedousuario'@'localhost';
EXIT
```

Também é necessário a criação de um arquivo .env com as seguintes variáveis que serão acessadas pelo código:
```
MYSQL_HOST="localhost"
MYSQL_USER="nomedousuario"
MYSQL_PASSWORD="senhadousuario"
MONGO_URI="urldeconexaodabasededadosmongodb"
```