from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Quadrinho
from database import engine, Base, get_db
from repositories import  QuadrinhoRepository
from schemas import QuadrinhoRequest, QuadrinhoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/quadrinhos", response_model = QuadrinhoResponse, status_code=status.HTTP_201_CREATED)
def create(request: QuadrinhoRequest, db: Session = Depends(get_db)):
    quadrinho = QuadrinhoRepository.save(db, Quadrinho(**request.dict()))
    return QuadrinhoResponse.from_orm(quadrinho)

@app.get("/api/quadrinhos", response_model=list[QuadrinhoResponse])
def find_all(db: Session = Depends(get_db)):
    quadrinhos = QuadrinhoRepository.find_all(db)
    return[QuadrinhoResponse.from_orm(quadrinho) for quadrinho in quadrinhos]

@app.get("/api/quadrinhos/{id}", response_model = QuadrinhoResponse)
def find_by_id(id : int, db : Session =  Depends(get_db)):
    quadrinho = QuadrinhoRepository.find_by_id(db, id)
    if not quadrinho:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  detail = "HQ não encontrada"
        )
    return QuadrinhoResponse.from_orm(quadrinho)

@app.put("/api/quadrinhos/{id}", response_model = QuadrinhoResponse)
def update(id : int, request: QuadrinhoRequest, db : Session = Depends(get_db)):
    if not QuadrinhoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "HQ não encontrada"
        )
        quadrinho = QuadrinhoRepository.save(db, Curso(id = id, **request.dict()))
        return QuadrinhoResponse.from_orm(quadrinho)

@app.delete("/api/quadrinhos/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_by_id(id : int, db : Session = Depends(get_db)):
    if not QuadrinhoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "HQ não encontrada"
        )
    QuadrinhoRepository.delete_by_id(db, id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)


