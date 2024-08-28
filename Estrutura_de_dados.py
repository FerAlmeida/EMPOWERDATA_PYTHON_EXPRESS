# ESTRUTURA DE DADOS COM PYTHON

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza"]

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza"]
print(convidados)

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza"]
print(convidados[1])

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza"]
print(convidados[0])

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza"]
print(convidados[3])

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, True, False]
print(convidados)

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, 80.77,True, False]
print(convidados[-2])

convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, 80.77, True, False]
print(convidados[-8])

convidados.append("elemento adicionado com append")
print(convidados)

convidados = convidados = ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, 80.77, True, False,"elemento adicionado com append"]
convidados.remove("elemento adicionado com append")
print(convidados)

mais_convidados = ["Fernando", "Pedro", "Gustavo","Ulisses"]
convidados.append(mais_convidados)
print(convidados)

convidados =  ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, 80.77, True, False,["Fernando", "Pedro", "Gustavo","Ulisses"]]
print(convidados[11][0])

convidados =  ["Ana Clara", "Maria Paula", "Julia Andrade", "Catarina Souza", 10, 20, 30, 40, 80.77, True, False,["Fernando", "Pedro", "Gustavo","Ulisses"]]
print(convidados[11][3])
