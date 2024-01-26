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
CREATE USER 'vinipmartins'@'localhost' IDENTIFIED BY 'mysql-123';
GRANT ALL PRIVILEGES ON *.* TO 'vinipmartins'@'localhost';
EXIT
```

