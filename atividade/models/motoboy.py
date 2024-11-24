from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco
from abc import abstractmethod

class Motoboy(Funcionario):
    def __init__(self, cnh: str, matricula: int, setor: Setor, salario: float, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(matricula, setor, salario, cpf, rg, data_nascimento, sexo, nome, telefone, email, endereco)
        self.cnh = cnh

    def salario_final(self):
        return self.salario
    


    
