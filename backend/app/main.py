 from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.api import auth, crowd_reports, predictions, stations, analytics

app = FastAPI(title="Crowd Predictor API")

# CORS (important for React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(crowd_reports.router)
app.include_router(predictions.router)
app.include_router(stations.router)
app.include_router(analytics.router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "Crowd Predictor API is running 🚀"}