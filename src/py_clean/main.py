from fastapi import FastAPI
from py_clean.routes import router

app = FastAPI()
app.include_router(router=router)
