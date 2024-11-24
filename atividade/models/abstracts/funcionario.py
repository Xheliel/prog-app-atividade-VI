from models.abstracts.fisica import Fisica
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from abc import ABC, abstractmethod

class Funcionario(Fisica):
    def __init__(self, matricula: int, setor: Setor, salario: float, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, nome: str, telefone: str, email: str, endereco: str):
        super().__init__(cpf, rg, data_nascimento, sexo, nome, telefone, email, endereco)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salario_final(self):
         pass

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nMatricula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}"
        )

