from model.models import Endereco, PessoaBase
from typing import List,Optional
from sqlmodel import Field

###NAO SEI FAZER
class PessoaCreate(PessoaBase):
    pass 

class PessoaUpdate(PessoaBase):
    pass 

class EnderecoUpdate(Endereco):
    pass

class EnderecoCreate(Endereco):
    pass 
    