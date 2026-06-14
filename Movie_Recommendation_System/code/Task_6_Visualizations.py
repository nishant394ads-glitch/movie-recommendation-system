import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
print("="*60)
print("TASK 6: VISUALIZATIONS")
print("="*60)
 
# Load data
print("\n1. Loading data...")
ratings = pd.read_csv('data/ratings_cleaned.csv')
movies = pd.read_csv('data/movies_cleaned.csv')
movie_ratings = ratings.merge(movies, on='movieId')
 
# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 10)
 
# Create 4-panel chart
print("2. Creating 4-panel analysis dashboard...")
 
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Movie Recommendation System - Analysis Dashboard', fontsize=16, fontweight='bold')
 
# Chart 1: Rating Distribution
axes[0, 0].hist(ratings['rating'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Distribution of Movie Ratings', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Rating (Stars)')
axes[0, 0].set_ylabel('Number of Ratings')
axes[0, 0].grid(True, alpha=0.3)
 
# Chart 2: Top 10 Most Rated
top_movies = movie_ratings.groupby('title')['rating'].count().sort_values(ascending=False).head(10)
axes[0, 1].barh(range(len(top_movies)), top_movies.values, color='coral', edgecolor='black', alpha=0.7)
axes[0, 1].set_yticks(range(len(top_movies)))
axes[0, 1].set_yticklabels(top_movies.index, fontsize=9)
axes[0, 1].set_title('Top 10 Most Rated Movies', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Number of Ratings')
axes[0, 1].grid(True, alpha=0.3, axis='x')
 
# Chart 3: Average Rating Distribution
avg_ratings = movie_ratings.groupby('title')['rating'].mean()
axes[1, 0].hist(avg_ratings, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Distribution of Average Movie Ratings', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Average Rating (Stars)')
axes[1, 0].set_ylabel('Number of Movies')
axes[1, 0].grid(True, alpha=0.3)
 
# Chart 4: Top 10 Highest Rated
top_rated = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)
axes[1, 1].barh(range(len(top_rated)), top_rated.values, color='lightcoral', edgecolor='black', alpha=0.7)
axes[1, 1].set_yticks(range(len(top_rated)))
axes[1, 1].set_yticklabels(top_rated.index, fontsize=9)
axes[1, 1].set_title('Top 10 Highest Rated Movies', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Average Rating')
axes[1, 1].grid(True, alpha=0.3, axis='x')
 
# Save chart 1
plt.tight_layout()
plt.savefig('output/01_movie_analysis.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output/01_movie_analysis.png")
 
# Chart 2: User Activity
print("3. Creating user activity chart...")
fig, ax = plt.subplots(figsize=(12, 6))
 
user_counts = ratings.groupby('userId')['rating'].count()
ax.hist(user_counts, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax.set_title('User Rating Activity Distribution', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Ratings per User')
ax.set_ylabel('Number of Users')
ax.grid(True, alpha=0.3)
 
plt.tight_layout()
plt.savefig('output/02_user_activity.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output/02_user_activity.png")
 
# Chart 3: Genre Analysis
if 'genres' in movies.columns:
    print("4. Creating genre analysis chart...")
    fig, ax = plt.subplots(figsize=(12, 6))
    
    genres = movies['genres'].str.split('|').explode()
    genre_counts = genres.value_counts().head(15)
    
    ax.barh(range(len(genre_counts)), genre_counts.values, color='mediumpurple', edgecolor='black', alpha=0.7)
    ax.set_yticks(range(len(genre_counts)))
    ax.set_yticklabels(genre_counts.index, fontsize=10)
    ax.set_title('Top 15 Movie Genres', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Movies')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('output/03_genre_analysis.png', dpi=300, bbox_inches='tight')
    print("   ✓ Saved: output/03_genre_analysis.png")
 
print("\n" + "="*60)
print("✓ VISUALIZATIONS COMPLETE!")
print("="*60)
print("\nGenerated charts:")
print("   ✓ output/01_movie_analysis.png")
print("   ✓ output/02_user_activity.png")
print("   ✓ output/03_genre_analysis.png")