#importar objeto

from aula5database import Database
from aula5objeto import Pessoa
from aula5pessoadao import PessoaDAO

#Exemplo uso
objeto = Pessoa(1, "Leandro")
print(objeto)
print(objeto.nome)

#Chama banco
db = Database()

#instanciar pessoadao
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
    print(pessoa)

#Criar objeto com atriz ator diretora
novo = Pessoa(0, "Gal Gadot")
novo = PessoaDAO.save(novo)

pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
    print(pessoa)