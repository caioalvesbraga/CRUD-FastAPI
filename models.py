from sqlalchemy import Column, Integer, String
from database import Base

class Quadrinho(Base):
    __tablename__ = "quadrinhos"

    id : int = Column(Integer, primary_key = True, index = True)
    autor : str = Column(String(100) , nullable = False)
    edicao : int = Column(Integer, nullable = False)
    publisher : str = Column(String(50), nullable = False)
    titulo : str = Column(String(100), nullable = False)
    
