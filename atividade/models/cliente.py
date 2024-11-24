from models.abstracts.fisica import Fisica
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Cliente(Fisica):
    def __init__(self, protocolo_atendimento: str, cpf: str, rg: str, data_nascimento: str, sexo: Sexo, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(cpf, rg, data_nascimento, sexo, nome, telefone, email, endereco)
        self.protocolo_atendimento = protocolo_atendimento

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nProtocolo atendimento: {self.protocolo_atendimento}"
        )
