from models.abstracts.pessoa import Pessoa
from models.endereco import Endereco

class Juridica(Pessoa):
    def __init__(self, cnpj: str, inscricao_estadual: str, nome: str, telefone: str, email: str, endereco: Endereco):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição estadual: {self.inscricao_estadual}"
        )