from abc import ABC
from models.abstracts.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.sexo import Sexo

class Fisica(Pessoa):
    def __init__(self, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG:{self.rg}"
            f"\nData de nascimento: {self.data_nascimento}"
            f"\nSexo: {self.sexo.name} - {self.sexo.char}"
        )

