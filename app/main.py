from fastapi import FastAPI
from api.routers.signin import router as signin_router
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
#2

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