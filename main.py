from fastapi import FastAPI
import upload_file

app = FastAPI()

app.include_router(upload_file.router)