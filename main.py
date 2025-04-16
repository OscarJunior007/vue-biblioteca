from fastapi import FastAPI,APIRouter
from entrypoints import libro_actions,user_action
from fastapi.middleware.cors import CORSMiddleware


def include_router(app):
    app.include_router(libro_actions.router)  
    app.include_router(user_action.router)  
  

    
    

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]
     
def start_application():
    app =  FastAPI()
    
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    include_router(app)
    return app  




app = start_application()




import uvicorn


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)