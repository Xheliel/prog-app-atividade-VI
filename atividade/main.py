from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enums.unidade_federal import UnidadeFederal
from models.abstracts.funcionario import Funcionario
from models.endereco import Endereco
from models.motoboy import Motoboy
import os

endereco = Endereco("X XXX XXXX XXXX", "XXX", "X XXXXX", "XXXXX XXX", "XXXXXXXX", UnidadeFederal.BAHIA)
motoboy = Motoboy("XXXXXXX", 2, Setor.OPERACOES, 2000, "XXXXXXXXXXX", "XXXXXXXXXXX", "XX XX XXXX", Sexo.MASCULINO, "XXXX", "XXXXXXXXXXX", "XXXXXXXXXXXXXXXXX", endereco)

os.system("clear")
print(motoboy)

