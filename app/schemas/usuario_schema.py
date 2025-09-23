from pydantic import BaseModel

class UsuarioLogin(BaseModel):
    username: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    username: str
    rol: str

    class Config:
        orm_mode = True
