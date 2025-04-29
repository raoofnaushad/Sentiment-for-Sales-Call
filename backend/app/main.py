from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import sentiment


app = FastAPI()

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to AlertDriving API 🚀"}


# Include all routers
app.include_router(sentiment.router, prefix="/api/sentiment-analysis", tags=["analysis"])

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Set this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)