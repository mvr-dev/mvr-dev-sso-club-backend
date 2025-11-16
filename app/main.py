# app/main.py
from fastapi import FastAPI
from api.routers.signin import router as signin_router


app = FastAPI()

app.include_router(signin_router, prefix="/api/v1", tags=["authentication"])

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