from fastapi import FastAPI, HTTPException
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

#get normal
@library.get("/")
def home():
    return dadosIniciais

#get com path parameters
@library.get("/livros/{id}")
def book(id: int):
    for livro in livros:
        if livro["id"] == id:
            return livro
    raise HTTPException(status_code=404, detail={"failed": "book not found"})

#get com path parameters, e query parameters
@library.get("/livros")
def books(genero: str = None, autor: str = None):
    resultado = livros
    if genero:
        resultado = [l for l in resultado if l["genero"].lower() == genero.lower()]
    if autor:
        resultado = [l for l in resultado if l["autor"].lower() in autor.lower()]
    if not resultado and (genero or autor):
        return {"failed": "books not found, please seacrh with other query parameters"}
    else:
        return resultado


