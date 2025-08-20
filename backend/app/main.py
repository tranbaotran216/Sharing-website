from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .database import Base, engine
from .routes import books, projects


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Databse tables created successfully!")
    yield
    print("Application shutting down...")

app = FastAPI(title="Share everything API", lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is working correctly"}