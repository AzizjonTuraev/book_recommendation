import pandas as pd
import pickle
import numpy as np
from fastapi import HTTPException
import os

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
project_path = os.path.dirname(current_directory)

file_path = os.path.join(current_directory, "server_artifacts", "user_sim_matrix.pkl")
with open(file_path, "rb") as f:
    user_sim_df = pickle.load(f)

file_path = os.path.join(current_directory, "server_artifacts", "book_ratings.pkl")
with open(file_path, "rb") as f:
    book_ratings = pickle.load(f)

file_path = os.path.join(current_directory, "server_artifacts", "high_rated.pkl")
with open(file_path, "rb") as f:
    highly_rated_books = pickle.load(f)

file_path = os.path.join(current_directory, "server_artifacts", "low_rated.pkl")
with open(file_path, "rb") as f:
    lowly_rated_books = pickle.load(f)

file_path = os.path.join(current_directory, "server_artifacts", "book_metadata.pkl")
with open(file_path, "rb") as f:
    book_metadata = pickle.load(f)


def get_metadata(isbn_list) -> pd.DataFrame:
    return book_metadata.loc[isbn_list]

def get_high_rated(nums : int) -> pd.DataFrame:
    subset = highly_rated_books["ISBN"].head(nums).to_list()
    subset = get_metadata(subset)
    return subset 

def get_low_rated(nums : int) -> pd.DataFrame:
    subset = lowly_rated_books["ISBN"].head(nums).to_list()
    subset = get_metadata(subset)
    return subset 

def get_user_ids()-> np.ndarray:
    users = book_ratings["User-ID"].unique()
    users = np.sort(users)
    return users

def get_recommendation(user_id, num_recommendations=5) -> pd.DataFrame:

    all_users = get_user_ids()
    if not np.isin(user_id, all_users):
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found. Please enter an existing user ID.")

    # Find most similar users
    similar_users = user_sim_df[user_id].sort_values(ascending=False).iloc[1:6]

    # Get books rated highly by similar users
    similar_users_books = book_ratings[book_ratings["User-ID"].isin(similar_users.index)]
    
    # Find books the target user hasn't rated yet
    user_books = set(book_ratings[book_ratings["User-ID"] == user_id]["Book-Title"])
    candidate_books = similar_users_books[~similar_users_books["Book-Title"].isin(user_books)]
    
    # Aggregate ratings and sort by highest average rating
    book_recommendations = candidate_books.groupby("ISBN")["Book-Rating"].mean().sort_values(ascending=False).head(num_recommendations)
    book_recommendations = book_recommendations.index.tolist()
    book_recommendations = book_metadata.loc[book_recommendations]

    return book_recommendations

