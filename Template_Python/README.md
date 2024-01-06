# Template Python 🚀

Este é um template reutilizável para iniciar projetos Python com FastAPI e Uvicorn. Ele fornece uma estrutura básica e configurações iniciais para começar a desenvolver APIs rapidamente.

## ⚙️ Configuração 

### 1. Clonar o Repositório

Clone este repositório para iniciar seu novo projeto Python com FastAPI e Uvicorn.

```bash
git clone https://github.com/thaizacn/Templates.git
cd Template_Python
```

### 2. Criando um ambiente virtual

```bash
python -m venv .venv
# No Windows
.\.venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instalar as dependencias 

```bash
pip install -r requirements.txt
```

### 4. Rodar a aplicação

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📄 Estrutura do Projeto

A estrutura do projeto segue um padrão comum para projetos FastAPI. As principais pastas são:

- app: Contém o código-fonte da aplicação FastAPI. <br>
- public: Contém arquivos estáticos e o arquivo HTML principal. <br>
- components: Local destinado para armazenar componentes reutilizáveis. <br>
- styles: Armazena arquivos de estilos.

## 🛠️ Tecnologias Utilizadas 

Os templates foram desenvolvidos utilizando as seguintes tecnologias:

- [FastAPI](https://fastapi.tiangolo.com/) Framework web moderno e rápido para Python.
- [Uvicorn](https://www.uvicorn.org/) ASGI server que permite rodar aplicações FastAPI.

## 🎁 Agradecimentos

Este template foi criado para facilitar o processo de início rápido de projetos Python com FastAPI e Uvicorn e poderá ser usado por qualquer um que, assim como eu, possua o desejo genuíno por mudar o mundo. Nós conseguimos. Juntos.

⌨️ com ❤️ por Thaiza Nascimento.
