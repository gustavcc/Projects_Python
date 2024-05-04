import mysql.connector as mysql
from colorama import Fore
from os import system

class EmpresaBD():
    
    linha = '-'*40
    
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connect(
                host='localhost',
                username='root',
                password='admin',
                database='empresa')
            self.cursor = self.connection.cursor()
        except mysql.Error as e:
            print(Fore.RED,'\nErro na conexão do banco: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
        else:
            print(Fore.RED+'\nNão há conexão estabelecida!'+Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
    
    def criarTabelaBD(self):
        self.connect()
        try: 
            querry = f'''CREATE TABLE IF NOT EXISTS Funcionarios (
                matricula INT PRIMARY KEY UNIQUE,
                nome VARCHAR(45) NOT NULL,
                salario REAL NOT NULL
            );'''
            self.cursor.execute(querry)
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao criar tabela: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def cadastrarFuncBD(self,mat,nome,salario):
        self.connect()
        try:
            querry = '''INSERT INTO Funcionarios (matricula, nome, salario)
                            VALUES (%s,%s,%s);'''
            self.cursor.execute(querry,(mat,nome,salario))
            self.connection.commit()
            print(self.linha)
            print('\nFuncionário cadastrado com sucesso!\n')
            print(self.linha)
            print('Aperte qualquer tecla pra continuar...')
            input()
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao inserir registro: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def editarFuncBD(self,mat,nome,salario,mat_op):
        self.connect()
        try:
            querry = '''UPDATE Funcionarios SET matricula=%s, nome=%s,salario=%s WHERE matricula=%s;'''
            self.cursor.execute(querry,(mat,nome,salario, mat_op))
            self.connection.commit()
            print(self.linha)
            print('\nFuncionário editado com sucesso!\n')
            print(self.linha)
            print('Aperte qualquer tecla pra continuar...')
            input()
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao editar registro: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def excluirFuncBD(self,mat):
        self.connect()
        try:
            querry = '''DELETE FROM Funcionarios WHERE matricula=%s;'''
            self.cursor.execute(querry,(mat,))
            self.connection.commit()
            print(self.linha)
            print('\nFuncionário excluido com sucesso!\n')
            print(self.linha)
            print('Aperte qualquer tecla pra continuar...')
            input()
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao excluir registro: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def ordenarFuncBD(self,option):
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios ORDER BY matricula;'''
                self.cursor.execute(querry)
            elif option==2:
                querry = '''SELECT * FROM Funcionarios ORDER BY nome;'''
                self.cursor.execute(querry)
            funcOrdenado = self.cursor.fetchall()
            for func in funcOrdenado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao ordenar registros: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def pesquisarFuncBD(self,option,mat=None,nome=None):
        # se for nome, passsar mat como None la em funcionarios
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios WHERE matricula=%s;'''
                self.cursor.execute(querry,(mat,))
            elif option==2:
                querry = '''SELECT * FROM Funcionarios WHERE nome=%s;'''
                self.cursor.execute(querry,(nome,))
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcOrdenado = self.cursor.fetchall()
            for func in funcOrdenado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao ordenar registros: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def filtrarFuncBD(self,option=None):
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios WHERE salario>1000;'''
                self.cursor.execute(querry)
            elif option==2:
                querry = '''SELECT * FROM Funcionarios WHERE salario<1000;'''
                self.cursor.execute(querry)
            elif option==3:
                querry = '''SELECT * FROM Funcionarios WHERE salario=1000;'''
                self.cursor.execute(querry)
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcFiltrado = self.cursor.fetchall()
            for func in funcFiltrado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao ordenar registros: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def listarFuncBD(self,mat=None):
        self.connect()
        try:
            if mat:
                querry = '''SELECT * FROM Funcionarios WHERE matricula=%s;'''
                self.cursor.execute(querry,(mat,))
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcLista = self.cursor.fetchall()
            for func in funcLista:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'\nErro ao listar funcionarios: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def existeFuncBD(self,mat):
        self.connect()
        try:
            querry = '''SELECT * FROM Funcionarios;'''
            self.cursor.execute(querry)
            funcionarios = self.cursor.fetchall()
            existe = False
            for func in funcionarios:
                if mat == func[0]:
                    existe = True
            return existe
        except mysql.Error as e:
            print(Fore.RED,'\nNão existe funcionários: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def buscaFuncAtributo(self,mat):
        self.connect()
        try:
            querry = '''SELECT * FROM Funcionarios WHERE matricula=%s;'''
            self.cursor.execute(querry,(mat,))
            funcionario = self.cursor.fetchall()
            return funcionario[0]
        except mysql.Error as e:
            print(Fore.RED,'\nNão existe funcionários: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()
    
    def bancoVazio(self):
        self.connect()
        try:
            querry = '''SELECT * FROM Funcionarios;'''
            self.cursor.execute(querry)
            funcionarios = self.cursor.fetchall()
            if funcionarios:
                return False
            return True
            
        except mysql.Error as e:
            print(Fore.RED,'\nNão existe funcionários: ',e,Fore.RESET)
            print('Aperte qualquer tecla pra continuar...')
            input()
        finally:
            self.disconnect()

bd = EmpresaBD()
bd.buscaFuncAtributo(1)