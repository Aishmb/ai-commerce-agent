from fastapi import FastAPI
from app import qa, recommend, image_search

app = FastAPI()

# Include the routes for Q&A, Recommendations, and Image Search
app.include_router(qa.router)
app.include_router(recommend.router)
app.include_router(image_search.router)
