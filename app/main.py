# importar fastapi
from fastapi import FastAPI

# crear una instancia de FastAPI
app = FastAPI()


# definir una health endpoint
@app.get("/health")
async def health():
    return {"status": "healthy"}


# definir una root endpoint
@app.get("/")
async def root():
    return {"message": "Hello API World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
# para ejecutar la aplicación, use el siguiente comando:
# uvicorn app.main:app --reload
# o simplemente:
# python3 ./app/main.py
