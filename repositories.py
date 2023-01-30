from sqlalchemy.orm import Session

from models import Quadrinho

class QuadrinhoRepository:
    @staticmethod
    def find_all(db : Session) -> list[Quadrinho]:
        return db.query(Quadrinho).all()

    @staticmethod
    def save(db : Session, quadrinho : Quadrinho) -> Quadrinho:
        if quadrinho.id:
            db.merge(quadrinho)
        else:
            db.add(quadrinho)
        db.commit()
        return quadrinho

    @staticmethod 
    def exists_by_id(db : Session, id : int) -> bool:
        return db.query(Quadrinho).filter(Quadrinho.id == id).first() is not None

    @staticmethod
    def delete_by_id(db : Session, id : int) -> None:
        quadrinho = db.query(Quadrinho).filter(Quadrinho.id == id).first()
        if quadrinho is not None:
            db.delete(quadrinho)
            db.commit()

