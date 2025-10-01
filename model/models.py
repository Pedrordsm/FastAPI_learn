from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class PessoaBase(SQLModel):
    name: str = Field(min_length=2, max_length=120)
    idade: Optional[int] = Field(default=None, ge=0, le=200)
    email: Optional[str] = Field(max_length=120)

class Pessoa(PessoaBase, table=True):
    __tablename__ = Pessoa
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    enderecos: List["Endereco"] = Relationship(back_populates="pessoa")


class Endereco(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    logradouro: Optional[str] = Field(max_length=120)
    numero: Optional[int] = Field(default=None)
    estado: Optional[str] = Field(max_length=2, min_length=2)
    cidade: Optional[str] = Field(max_length=120)
    bairro: Optional[str] = Field(max_length=120)
    pessoa_id: Optional[int] = Field(default=None, foreign_key="pessoa.id")
    pessoa: Optional["Pessoa"] = Relationship(back_populates="enderecos")
