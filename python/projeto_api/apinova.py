from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#criar uma api simples que possua apenas o GET inicialmente, ela fornece dados de livros no geral e livros especificos,
#basicamente tras as informações desses livros em JSON, se não conseguir, retorna none e printa livro não encontrado

livros = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "paginas": 1200},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "genero": "Distopia", "paginas": 328},
    {"id": 3, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "paginas": 310},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Clássico", "paginas": 256},
    {"id": 5, "titulo": "Neuromancer", "autor": "William Gibson", "genero": "Cyberpunk", "paginas": 320},
]
dadosIniciais = [
    {"dados": "bom dia, essa é uma api de teste, que possui rotas apenas get atualmente"},
    {"docs": "temos as rotas nesse momento de /livros/id(coloque o id disponivel até 5) e rota /livros para ver todos"}
]
library = FastAPI()

#aqui seria como os dados serao adicionados no post
class Livro(BaseModel):
    titulo: str
    autor: str
    genero: str
    paginas: int

#get normal
@library.get("/")
def home() -> list[dict]:
    return dadosIniciais

#get com path parameters
@library.get("/livros/{id}")
def book(id: int) -> dict:
    for livro in livros:
        if livro["id"] == id:
            return livro
    raise HTTPException(status_code=404, detail={"failed": "book not found"})

#get com path parameters, e query parameters
@library.get("/livros")
def books(genero: str = None, autor: str = None) -> list[dict]:
    resultado = livros
    if genero:
        resultado = [l for l in resultado if l["genero"].lower() == genero.lower()]
    if autor:
        resultado = [l for l in resultado if l["autor"].lower() in autor.lower()]
    return resultado

#fazer uma rota post agora
@library.post("/adicionar")
def adicionar_livros(arquivos: Livro) -> dict:
    if len(livros) > 0:
        livros_novo = livros[-1]["id"] + 1
    else:
        livros_novo = 1
    novo_livro = arquivos.model_dump()
    novo_livro["id"] = livros_novo
    livros.append(novo_livro)
    return {"mensagem": f"adicionado com sucesso o livro {novo_livro}"}


