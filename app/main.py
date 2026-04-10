from fastapi import FastAPI
from api.routers.signin import router as signin_router
from api.routers.users import router as users_router
from api.routers.suggestions import router as suggestion_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signin_router, prefix="/api/v1", tags=["authentication"])
app.include_router(users_router, prefix="/api/v1", tags=["user_info"])
app.include_router(suggestion_router,prefix="/api/v1",tags=['suggestions'])

@app.get("/")
async def root():
    return {"message": "SSO API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",  
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )