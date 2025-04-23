from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import io

router = APIRouter()

# Load the CLIP model and processor once at module load
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

# Response model
class ImageSearchResult(BaseModel):
    product_id: int
    product_name: str
    similarity_score: float
    image_url: str

# Main search logic (placeholder for now)
def search_images(image: Image.Image):
    inputs = processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)

    # TODO: Compare `image_features` with your stored database features
    return [{
        "product_id": 1,
        "product_name": "Laptop",
        "similarity_score": 0.95,
        "image_url": "laptop.jpg"
    }]

# API endpoint
@router.post("/image-search", response_model=list[ImageSearchResult])
async def image_search(file: UploadFile = File(...)):
    print(f"Received image: {file.filename} ({file.content_type})")

    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(
            status_code=400,
            content={"detail": "Unsupported file type. Only JPEG and PNG are allowed."}
        )

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"detail": f"Failed to process image: {str(e)}"}
        )

    results = search_images(image)
    return results
