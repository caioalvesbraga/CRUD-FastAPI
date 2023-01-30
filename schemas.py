from pydantic import BaseModel

class QuadrinhoBase(BaseModel):
    autor : str
    edicao : int
    publisher : str
    titulo : str

class QuadrinhoRequest(QuadrinhoBase):
    ...

class QuadrinhoResponse(QuadrinhoBase):
    id : int

    class Config:
        orm_mode = True
        
