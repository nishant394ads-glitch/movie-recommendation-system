import pandas as pd
 
print("="*60)
print("TASK 2: DATA CLEANING")
print("="*60)
 
# Load datasets
print("\n1. Loading datasets...")
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')
 
print(f"   Movies loaded: {movies.shape}")
print(f"   Ratings loaded: {ratings.shape}")
 
# Check for missing values
print("\n2. Checking for missing values...")
print(f"   Missing in movies: {movies.isnull().sum().sum()}")
print(f"   Missing in ratings: {ratings.isnull().sum().sum()}")
 
# Remove missing values
print("\n3. Removing missing values...")
movies = movies.dropna()
ratings = ratings.dropna()
 
# Remove duplicates
print("4. Removing duplicates...")
movies = movies.drop_duplicates()
ratings = ratings.drop_duplicates()
 
# Save cleaned data
print("\n5. Saving cleaned data...")
movies.to_csv('data/movies_cleaned.csv', index=False)
ratings.to_csv('data/ratings_cleaned.csv', index=False)
 
print("\n" + "="*60)
print("✓ DATA CLEANING COMPLETE!")
print("="*60)
print(f"Movies: {movies.shape[0]} records")
print(f"Ratings: {ratings.shape[0]} records")
print("\n✓ Saved: data/movies_cleaned.csv")
print("✓ Saved: data/ratings_cleaned.csv")