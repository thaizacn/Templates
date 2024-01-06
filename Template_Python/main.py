from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import TemplateController

app = FastAPI()

app.add_middleware(
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializando rotas
app.include_router(TemplateController.router, prefix="/template")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)