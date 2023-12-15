from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests
from config import SHOPIFY_API_KEY, SHOPIFY_API_SECRET, SHOPIFY_REDIRECT_URI, DJANGO_API_BASE_URL

app = FastAPI()

# OAuth2 security for Shopify authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Video(BaseModel):
    id: int
    title: str
    url: str

class ProductVideo(BaseModel):
    product_id: int
    video_id: int

# Routes
@app.get("/")
async def read_root():
    return {"message": "Welcome to your Shopify app!"}

@app.get("/videos", response_model=List[Video])
async def get_videos():
    # Make a GET request to your Django REST API to fetch videos
    # Replace with your actual endpoint
    video_api_url = f"{DJANGO_API_BASE_URL}/video/api/videos/?format=json"
    
    # Use the Shopify API credentials from config.py
    headers = {
        "X-Shopify-Access-Token": f"{SHOPIFY_API_KEY}:{SHOPIFY_API_SECRET}",
    }

    # Make the request and process the response
    response = requests.get(video_api_url, headers=headers)
    response.raise_for_status()  # Check for errors
    videos = response.json()  # Assuming your API returns JSON
    return videos

@app.post("/associate-video", response_model=ProductVideo)
async def associate_video(video_id: int, product_id: int):
    # Make a POST request to your Django REST API to associate a video with a product
    # Replace with your actual endpoint
    associate_api_url = f"{DJANGO_API_BASE_URL}/video/api/associate/"
    data = {"video_id": video_id, "product_id": product_id}

    # Use the Shopify API credentials from config.py
    headers = {
        "X-Shopify-Access-Token": f"{SHOPIFY_API_KEY}:{SHOPIFY_API_SECRET}",
    }

    # Make the request and process the response
    response = requests.post(associate_api_url, json=data, headers=headers)
    response.raise_for_status()  # Check for errors
    product_video = response.json()  # Assuming your API returns JSON
    return product_video
