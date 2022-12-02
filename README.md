### backend flask com swagger - README

### Montando projeto local

# Clone o repositório a partir com o comando:

git clone git@github.com:tuliotrefzger/Processo-Seletivo-GrupoVoga-Backend.git

# Instale os requerimentos presentes em requirements.txt com o comando:

pip install -r requirements.txt

# Inicialize o commando:

flask run

# Acesse o port 5000 abrindo o swagger:

http://localhost:5000/

# Teste os endpoints presentes em "user"

## Banco de Dados

### Executar os comandos ao modificar ou incluir modelos

```bash
flask db init  # so quando iniciar o banco
flask db migrate --message 'migration'
```
