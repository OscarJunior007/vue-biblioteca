from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from entrypoints.libro_actions import setup_register_libros
from entrypoints.user_action import setup_users


app = FastAPI()
setup_register_libros(app)
setup_users(app)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import uvicorn


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)