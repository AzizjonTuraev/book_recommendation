from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from . import server_utils

# FastAPI app
app = FastAPI()

# Enable CORS (for frontend to communicate with API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for POST request
class UserRequest(BaseModel):
    user_id: int
    num_recommendations: int = 5

class NumRequest(BaseModel):
    nums: int = 5

@app.get("/")
def home():
    return {"message": "Welcome to the Book Recommendation API"}

@app.post("/high-rated")
def high_rated(request: NumRequest):
    """Get high-rated books."""
    nums = request.nums
    output = server_utils.get_high_rated(nums)
    if output.empty:
        return {"message": "No high-rated books found."}
    return output.to_dict(orient="records")  

@app.post("/low-rated")
def low_rated(request: NumRequest):
    """Get low-rated books."""
    nums = request.nums
    output = server_utils.get_low_rated(nums)
    if output.empty:
        return {"message": "No low-rated books found."}
    return output.to_dict(orient="records")

@app.get("/existing-users")
def existing_users():
    """Get a list of user IDs."""
    user_ids = server_utils.get_user_ids()
    if user_ids.size == 0:
        return {"message": "No users found."}
    return user_ids.tolist()
    # return user_ids.to_dict(orient="records")

@app.post("/recommend")
def recommend_books(request: UserRequest):
    """Recommend books for a given user ID."""
    user_id = request.user_id
    num_recommendations = request.num_recommendations

    try:
        recommendations = server_utils.get_recommendation(user_id, num_recommendations)
        return recommendations.to_dict(orient="records")  # Convert DataFrame to JSON
    except HTTPException as e:
        raise e  # Let FastAPI handle the exception and send the error response


