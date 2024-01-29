# Pipeline Python, MongoBD, MySQL

Repositório com a construção de um pipeline de dados usando MongoDB e MySQL

Este projeto foi desenvolvido usando o Gitpod. Por isso, ao replicar esse projeto no Gitpod, é importante rodar o seguinte comando:

Primeiro, teste se o MySQL já está configurado. Este teste pode ser realizado digitando `mysql` no terminal. Caso dê algum erro ao executar este comando, rode o comando abaixo, ele irá garantir que o MySQL esteja instalado no Gitpod.
```bash
gp validate
```

Em seguida, realize  a criação de um arquivo `.env` com as seguintes variáveis de ambiente:
```
MYSQL_HOST='localhost'
MYSQL_USER='nomedousuario'
MYSQL_PASSWORD='senhadousuario'
MONGO_URI='urldeconexaodabasededadosmongodb'
MONGO_DB_NAME='nomebasededadosmongo'
MONGO_COLLECTION_NAME='nomecolecaomongo'
```

Com este arquivo criado, é necessário realizar a configuração do usuário no MySQL.
Esta configuração pode ser feita através do Makefile, apenas digitando `make` no terminal.

Caso não seja possível utilizar o Makefile, as configurações pode ser feitas manualmente com os códigos abaixo:

```mysql
CREATE USER 'nomedousuario'@'localhost' IDENTIFIED BY 'senhadousuario';
GRANT ALL PRIVILEGES ON *.* TO 'nomedousuario'@'localhost';
EXIT
```

Por fim, ativar o ambiente virtual e rodar os scripts.

```bash
source venv/bin/activate
```