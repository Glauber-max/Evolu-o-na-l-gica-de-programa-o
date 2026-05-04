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
    {"id": 6, "titulo": "Fundação", "autor": "Isaac Asimov", "genero": "Ficção Científica", "paginas": 240},
    {"id": 7, "titulo": "Duna", "autor": "Frank Herbert", "genero": "Ficção Científica", "paginas": 688},
    {"id": 8, "titulo": "O Alquimista", "autor": "Paulo Coelho", "genero": "Ficção", "paginas": 208},
    {"id": 9, "titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "genero": "Fantasia",
     "paginas": 223},
    {"id": 10, "titulo": "O Código Da Vinci", "autor": "Dan Brown", "genero": "Suspense", "paginas": 432},
    {"id": 11, "titulo": "O Iluminado", "autor": "Stephen King", "genero": "Terror", "paginas": 447},
    {"id": 12, "titulo": "It: A Coisa", "autor": "Stephen King", "genero": "Terror", "paginas": 1103},
    {"id": 13, "titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "genero": "Realismo Mágico",
     "paginas": 417},
    {"id": 14, "titulo": "A Revolução dos Bichos", "autor": "George Orwell", "genero": "Distopia", "paginas": 112},
    {"id": 15, "titulo": "O Sol é para Todos", "autor": "Harper Lee", "genero": "Clássico", "paginas": 376},
    {"id": 16, "titulo": "Frankenstein", "autor": "Mary Shelley", "genero": "Terror", "paginas": 288},
    {"id": 17, "titulo": "O Silmarillion", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "paginas": 365},
    {"id": 18, "titulo": "Eu, Robô", "autor": "Isaac Asimov", "genero": "Ficção Científica", "paginas": 256},
    {"id": 19, "titulo": "Grande Sertão: Veredas", "autor": "Guimarães Rosa", "genero": "Clássico", "paginas": 600},
    {"id": 20, "titulo": "Moby Dick", "autor": "Herman Melville", "genero": "Aventura", "paginas": 635}
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
        resultado = [l for l in resultado if autor.lower() in l["autor"].lower()]
    return resultado

#fazer uma rota post agora
@library.post("/livros/adicionar") # o metodo post pede um conjunto de informações definido pela basemodel e se o id da base da
def adicionar_livros(arquivos: Livro) -> dict: #base de dados existir, ele pega o ultimo e adiciona mais um(evitar erros no futuro)
    if len(livros) > 0:
        livros_novo = livros[-1]["id"] + 1
    else:
        livros_novo = 1
    novo_livro = arquivos.model_dump() #transforma em dict, se junta com o id e da um merge na base de dados
    novo_livro["id"] = livros_novo
    livros.append(novo_livro)
    return {"mensagem": f"adicionado com sucesso o livro {novo_livro}"}

#criar agora um metodo delete do http
@library.delete("/livros/{id}/eliminar") #rastreia o livro pedido pra delete, se nao encontrar da um 404
def eliminar_livros(id: int) -> dict:
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return livros
    raise HTTPException(status_code=404, detail={"failed": "livro not found"})

#vamos criar agora o metodo put pra editar dados, vamos precisar do id, e dos dados que se quer atualizar
@library.put("/livros/editar/{id}")
def editar_livros(id: int, dados: Livro):
    for livro in livros:
        if livro["id"] == id:
            dados_novos = dados.model_dump()
            livros[id] = dados_novos
    return livros