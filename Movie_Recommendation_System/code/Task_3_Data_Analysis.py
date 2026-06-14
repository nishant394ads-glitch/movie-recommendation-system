import pandas as pd
 
print("="*60)
print("TASK 3: DATA ANALYSIS")
print("="*60)
 
# Load cleaned data
print("\n1. Loading cleaned data...")
movies = pd.read_csv('data/movies_cleaned.csv')
ratings = pd.read_csv('data/ratings_cleaned.csv')
 
# Merge data
print("2. Merging datasets...")
movie_ratings = ratings.merge(movies, on='movieId')
 
# Basic statistics
print("\n" + "="*60)
print("DATASET STATISTICS")
print("="*60)
 
total_users = ratings['userId'].nunique()
total_movies = movies['movieId'].nunique()
total_ratings = len(ratings)
 
print(f"\nTotal Users: {total_users}")
print(f"Total Movies: {total_movies}")
print(f"Total Ratings: {total_ratings}")
 
# Rating statistics
print("\n" + "-"*60)
print("RATING STATISTICS")
print("-"*60)
print(f"\nAverage Rating: {ratings['rating'].mean():.2f}/5.0")
print(f"Median Rating: {ratings['rating'].median():.1f}")
print(f"Min Rating: {ratings['rating'].min()}")
print(f"Max Rating: {ratings['rating'].max()}")
 
# Most rated movies
print("\n" + "-"*60)
print("TOP 10 MOST RATED MOVIES")
print("-"*60)
top_movies = movie_ratings.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
for idx, (title, count) in enumerate(top_movies.items(), 1):
    print(f"{idx}. {title}: {count} ratings")
 
# Highest rated movies
print("\n" + "-"*60)
print("TOP 10 HIGHEST RATED MOVIES")
print("-"*60)
top_rated = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
for idx, (title, rating) in enumerate(top_rated.items(), 1):
    print(f"{idx}. {title}: {rating:.2f}⭐")
 
# User behavior
print("\n" + "-"*60)
print("USER BEHAVIOR")
print("-"*60)
user_ratings = ratings.groupby('userId')['rating'].count()
print(f"\nAverage ratings per user: {user_ratings.mean():.0f}")
print(f"Max ratings by a user: {user_ratings.max()}")
print(f"Min ratings by a user: {user_ratings.min()}")
 
print("\n" + "="*60)
print("✓ DATA ANALYSIS COMPLETE!")
print("="*60)