import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
 
print("="*60)
print("TASK 4: RECOMMENDATION ALGORITHM")
print("="*60)
 
# Load data
print("\n1. Loading data...")
ratings = pd.read_csv('data/ratings_cleaned.csv')
movies = pd.read_csv('data/movies_cleaned.csv')
 
# Create user-movie matrix
print("2. Creating user-movie matrix...")
user_movie_matrix = ratings.pivot_table(
    index='userId',
    columns='movieId',
    values='rating'
)
user_movie_matrix = user_movie_matrix.fillna(0)
 
print(f"   Matrix shape: {user_movie_matrix.shape}")
print(f"   Users: {user_movie_matrix.shape[0]}")
print(f"   Movies: {user_movie_matrix.shape[1]}")
 
# Calculate user similarity
print("\n3. Calculating user similarity...")
user_similarity = cosine_similarity(user_movie_matrix)
 
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)
 
print(f"   Similarity matrix shape: {user_similarity_df.shape}")
 
# Save similarity matrix
print("\n4. Saving similarity matrix...")
user_similarity_df.to_csv('data/user_similarity.csv')
 
print("\n" + "="*60)
print("✓ ALGORITHM COMPLETE!")
print("="*60)
print("✓ Saved: data/user_similarity.csv")
 
# Show example
print("\nExample: Users most similar to User 1:")
if 1 in user_similarity_df.index:
    similar = user_similarity_df[1].sort_values(ascending=False)[1:6]
    for user_id, score in similar.items():
        print(f"   User {int(user_id)}: {score:.4f}")