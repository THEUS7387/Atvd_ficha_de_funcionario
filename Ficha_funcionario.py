import os 
import csv
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: float

funcionarios = []

def mostrar_menu():
    print("\n--| SEJA BEM VINDO A DÊNDE TECH |--")
    print("1- Cadastrar funcionario")
    print("2- Listar funcionário")
    print("3- Atualizar funcionário")
    print("4- Excluir funcionário")
    print("5- Salvar dados em CSV ")
    print("6- Carregar de CSV")
    print("7- Sair")
    print()

def cadastrar():
    nome = input("Nome: ")
    cpf = input("Cpf: ")
    cargo = input("Cargo: ")
    salario = float(input("Salario: "))
    novo_funcionario = Funcionario(nome, cpf, cargo, salario)
    funcionarios.append(novo_funcionario)
    print("Funcionario cadastrado!")

def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for f in funcionarios:
        print(f"{f.nome} | CPF: {f.cpf} | Cargo: {f.cargo} | Salário: R${f.salario}")

def atualizar():
    cpf_busca = input("Digite o CPF do funcionario: ")
    for f in funcionarios:
        if f.cpf == cpf_busca:
            f.nome = input("Novo nome: ")
            f.cargo = input("Novo cargo: ")
            f.salario = float(input("Novo salario: "))
            print("Funcionario atualizado!")
            return
    print("Funcionario não encontrado.")

def deletar():
    cpf_busca = input("Digite o CPF do funcionario: ")
    for f in funcionarios:
        if f.cpf == cpf_busca:
            funcionarios.remove(f)
            print("Funcionario removido!")
            return
    print("Funcionario não encontrado.")

def salvar_csv():
    with open("funcionarios.csv", "w", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for f in funcionarios:
            escritor.writerow([f.nome, f.cpf, f.cargo, f.salario])
        print("Dados salvos no arquivo 'funcionarios.csv'.")

def carregar_csv():
    try:
        with open("funcionarios.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            funcionarios.clear()
            for linha in leitor:
                nome, cpf, cargo, salario = linha
                funcionarios.append(Funcionario(nome, cpf, cargo, float(salario)))
        print("Dados carregados do arquivo.")
    except FileNotFoundError:
        print("Arquivo 'funcionarios.csv' não encontrado.")

while True:
    mostrar_menu()
    opcao = input("Qual a opção desejada?: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        salvar_csv()
    elif opcao == "6":
        carregar_csv()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção invalida. Tente novamente.")
